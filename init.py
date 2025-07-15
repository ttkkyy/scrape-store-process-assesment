import mysql.connector
import os 
# from mysql.connector import pooling
import psycopg2
from dotenv import load_dotenv
load_dotenv()

# Create a connection pool (recommended for web apps)

# db_config = {
#     'host': os.getenv('DB_HOST'),
#     'user': os.getenv('DB_USER'),
#     'password': os.getenv('DB_PASS'),
#     'database': os.getenv('DB_SERVER'),
# }

# # Set up a connection pool with max 5 connections
# connection_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

BASE_SQL_PATH = "db/base.sql"

def run_sql_file(cursor, filepath):
    with open(filepath, 'r') as f:
        sql = f.read()
        cursor.execute(sql)

def get_connection():
    """Retrieve a pooled connection to the database."""
    return psycopg2.connect(os.getenv("DATABASE_URL"))

def init_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        try:
            # Try a quick query to test if the tables exist
            cursor.execute("SELECT 1 FROM mc_store LIMIT 1;")
            cursor.execute("SELECT 1 FROM mc_store_fac LIMIT 1;")
        except psycopg2.Error:
            run_sql_file(cursor, BASE_SQL_PATH)
            conn.commit()            
        finally:
            cursor.close()
            conn.close()

    except Exception as e:
       raise