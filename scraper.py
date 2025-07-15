import mysql.connector
import json
import re
import sys
from requests_html import HTMLSession
from init import get_connection
# Create a session
session = HTMLSession()

def split_address(address):
    """
    Splits a Malaysian address string into address_line, postcode, city, and state.
    Assumes the address ends with postcode, city, state, Malaysia.
    """
    # Remove 'Malaysia' if it's present
    address = address.replace(', Malaysia', '').strip()

    # Try to match the postcode (5 digits) followed by city and state
    parts = [part.strip() for part in address.split(',')]

    # Find postcode (5-digit number)
    postcode_index = None
    for i, part in enumerate(parts):
        if re.fullmatch(r'\d{5}', part):
            postcode_index = i
            break

    if postcode_index is not None and len(parts) > postcode_index + 2:
        address_line = ', '.join(parts[:postcode_index])
        postcode = parts[postcode_index]
        city = parts[postcode_index + 1]
        state = parts[postcode_index + 2]
    else:
        # Fallback if format is unexpected
        address_line = address
        postcode = ''
        city = ''
        state = ''

    return address_line, postcode, city, state


def store_to_db(store_data):
    db = get_connection() 
    cursor = db.cursor()
    try:
        # Check if the store already exists
        store_name = store_data["name"]
        cursor.execute('SELECT mc_id FROM mc_store WHERE mc_name = %s', (store_name,))
        existing_store = cursor.fetchone()
        if existing_store:
            return

        cursor.execute('''
            INSERT INTO mc_store (mc_name, mc_address, mc_address_line ,mc_state, mc_city, mc_postcode, mc_email, mc_latitude, mc_longitude, mc_telephone)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
            store_data["name"],
            store_data["address"],
            store_data["address_line"],
            store_data["state"],
            store_data["city"],
            store_data["postcode"],
            store_data["email"],
            float(store_data["lat"]),
            float(store_data["lng"]),
            str(store_data["telephone"])
        ))
        store_id = cursor.lastrowid

        for category in store_data["categories"]:
            cursor.execute('''
                INSERT INTO mc_store_fac (mcf_cat_id, mcf_cat_name, mcf_store_id)
                VALUES (%s, %s, %s)
            ''', (
                category["cat_id"],
                category["cat_name"],
                store_id
            ))

        db.commit()

    except mysql.connector.Error as err:
        db.rollback()
    finally:
        cursor.close()
        db.close() # Closes the connection each time

def web_scrape() :
    url = 'https://www.mcdonalds.com.my/storefinder/index.php'
    data = {
        'ajax' : '1',
        'action': 'get_nearby_stores',
        'lat' : '',
        'lng' : '',
        'state' : '',
        'distance': '100000',
        'state': 'Kuala Lumpur',
        'address': 'Kuala Lumpur, Malaysia',
        'issuggestion' :0,
        'islocateus': 0
    }

    response = session.post(url, data=data)
    if (response.status_code != 200):
        raise
    mcd_data = json.loads(response.content.decode('utf-8-sig'))

    for store in mcd_data['stores']:
        # Extract and clean the address
        address_line, postcode, city, state = split_address(store['address'])
        
        # Prepare data for database insertion
        store_data = {
            "name": store["name"],
            "address":  store["address"],
            "address_line": address_line,
            "telephone": store["telephone"],
            "email": store["email"],
            "website": store["website"],
            "fax": store["fax"],
            "description": store["description"],
            "lat": store["lat"],
            "lng": store["lng"],
            "default_media": store.get("default_media", ""),
            "postcode": postcode,
            "state": state,
            "city": city,
            "categories": store["cat"]
        }
        
        store_to_db(store_data)
