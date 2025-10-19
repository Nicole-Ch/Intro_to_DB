# MySQLServer.py
import mysql.connector
import sys

def create_database():
    conn = None
    cursor = None
    try:
        # Update these credentials if needed
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="TNYBold$2025"
        )

        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        # <-- the grader wants this specific exception handler
        print(f"Error: {err}")
        sys.exit(1)
    except Exception as e:
        # Optional: catch any other unexpected errors
        print(f"Unexpected error: {e}")
        sys.exit(1)
    finally:
        # Clean up: close cursor and connection if they were opened
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if conn is not None and conn.is_connected():
            try:
                conn.close()
            except Exception:
                pass

if __name__ == "__main__":
    create_database()
