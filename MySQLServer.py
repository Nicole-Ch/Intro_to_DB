# MySQLServer.py
import mysql.connector
from mysql.connector import Error
import sys

def create_database():
    try:
        # Replace user/password/host if needed
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="TNYBold$2025"
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except Error as err:
        print(f"Error: {err}")
        sys.exit(1)
    finally:
        try:
            if cursor:
                cursor.close()
        except NameError:
            pass
        try:
            if conn and conn.is_connected():
                conn.close()
        except NameError:
            pass

if __name__ == "__main__":
    create_database()
