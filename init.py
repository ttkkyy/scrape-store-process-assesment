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

def table_exists(cursor, table_name):
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = %s
        );
    """, (table_name,))
    return cursor.fetchone()[0]

def init_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        store_exists = table_exists(cursor, 'mc_store')
        fac_exists = table_exists(cursor, 'mc_store_fac')
        if not (store_exists and fac_exists):
            try:
                run_sql_file(cursor, BASE_SQL_PATH)
                conn.commit()       
            except Exception as e:
                conn.rollback()     
                raise 
            finally:
                cursor.close()
                conn.close()

    except Exception as e:
       raise