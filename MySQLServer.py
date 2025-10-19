#!/usr/bin/env python3
"""
Python script to create the alx_book_store database
"""

import MySQLdb
import sys

def create_database():
    """Create the alx_book_store database"""
    try:
        # Connect to MySQL server without specifying a database
        db = MySQLdb.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username if different
            passwd=""     # Replace with your MySQL password if set
        )
        
        # Create a cursor object
        cursor = db.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")
        
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)
        
    finally:
        # Close the database connection
        if 'db' in locals():
            db.close()

if __name__ == "__main__":
    create_database()