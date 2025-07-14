import mysql.connector
import os 
from mysql.connector import pooling
from dotenv import load_dotenv
load_dotenv()

# Create a connection pool (recommended for web apps)

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'database': os.getenv('DB_SERVER'),
}
print (db_config)
# Set up a connection pool with max 5 connections
connection_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

def get_connection():
    """Retrieve a pooled connection to the database."""
    return connection_pool.get_connection()