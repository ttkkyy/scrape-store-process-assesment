from fastapi import FastAPI, Request
from fastapi import APIRouter

import mysql.connector

from init import get_connection


router = APIRouter()

# API endpoint
@router.get("/outlets" )
def get_outlets():
    db = get_connection()
    cursor = db.cursor()
    try :
        cursor.execute("SELECT mc_id, mc_name , mc_address, mc_email, mc_latitude, mc_longitude , mc_telephone FROM mc_store")
        rows = cursor.fetchall()
        cursor.execute("select string_agg(mcf_cat_name, ', ') , mcf_store_id  from mc_store_fac group by mcf_store_id")
        rows_fac = cursor.fetchall()
        categories = {row[1]: row[0] for row in rows_fac}
        outlets = []
        for row in rows:
            outlets.append({
                "name": row[1],
                "address": row[2],
                "email": row[3],
                "lat": row[4],
                "lng": row[5],
                "telephone": row[6],
                "categories": categories.get(row[0], "")

            })
        return {"outlets": outlets}
    
    except mysql.connector.Error as err:
        db.rollback()
    finally:
        cursor.close()
        db.close() # Closes the connection each time
    