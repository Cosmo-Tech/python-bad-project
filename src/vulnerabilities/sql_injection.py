"""
This module contains examples of SQL injection vulnerabilities.
SQL injection occurs when user input is directly incorporated into SQL queries without proper sanitization.
"""

import sqlite3
import mysql.connector
from typing import List, Dict, Any, Optional


# ISSUE: Basic SQL injection vulnerability with string concatenation
def get_user_by_id_vulnerable(user_id: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve a user by ID from the database.
    Contains a SQL injection vulnerability due to string concatenation.
    
    Example exploit: user_id = "1; DROP TABLE users; --"
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Vulnerable: Direct string concatenation
    query = "SELECT * FROM users WHERE id = " + user_id
    
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            return {
                "id": result[0],
                "username": result[1],
                "email": result[2]
            }
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        conn.close()


# ISSUE: SQL injection in a WHERE clause with string formatting
def search_users_vulnerable(username: str) -> List[Dict[str, Any]]:
    """
    Search for users by username.
    Contains a SQL injection vulnerability due to string formatting.
    
    Example exploit: username = "a' OR '1'='1"
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Vulnerable: String formatting
    query = f"SELECT * FROM users WHERE username LIKE '%{username}%'"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        users = []
        for row in results:
            users.append({
                "id": row[0],
                "username": row[1],
                "email": row[2]
            })
        
        return users
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()


# ISSUE: SQL injection in an ORDER BY clause
def get_sorted_products_vulnerable(sort_column: str) -> List[Dict[str, Any]]:
    """
    Get products sorted by the specified column.
    Contains a SQL injection vulnerability in the ORDER BY clause.
    
    Example exploit: sort_column = "name; DROP TABLE products; --"
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Vulnerable: Unsanitized input in ORDER BY
    query = f"SELECT * FROM products ORDER BY {sort_column}"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        products = []
        for row in results:
            products.append({
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "category": row[3]
            })
        
        return products
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()


# ISSUE: SQL injection in a LIMIT clause
def get_limited_results_vulnerable(limit: str) -> List[Dict[str, Any]]:
    """
    Get a limited number of results from the database.
    Contains a SQL injection vulnerability in the LIMIT clause.
    
    Example exploit: limit = "5; DROP TABLE logs; --"
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Vulnerable: Unsanitized input in LIMIT
    query = f"SELECT * FROM logs ORDER BY timestamp DESC LIMIT {limit}"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        logs = []
        for row in results:
            logs.append({
                "id": row[0],
                "message": row[1],
                "timestamp": row[2]
            })
        
        return logs
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()


# ISSUE: SQL injection with multiple parameters
def filter_products_vulnerable(category: str, min_price: str) -> List[Dict[str, Any]]:
    """
    Filter products by category and minimum price.
    Contains SQL injection vulnerabilities with multiple parameters.
    
    Example exploit: category = "Electronics' OR '1'='1"
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Vulnerable: Multiple unsanitized inputs
    query = f"SELECT * FROM products WHERE category = '{category}' AND price >= {min_price}"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        products = []
        for row in results:
            products.append({
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "category": row[3]
            })
        
        return products
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()


# ISSUE: SQL injection in an INSERT statement
def add_user_vulnerable(username: str, email: str) -> bool:
    """
    Add a new user to the database.
    Contains a SQL injection vulnerability in an INSERT statement.
    
    Example exploit: username = "hacker', 'hacker@evil.com'); DROP TABLE users; --"
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Vulnerable: Unsanitized input in INSERT
    query = f"INSERT INTO users (username, email) VALUES ('{username}', '{email}')"
    
    try:
        cursor.execute(query)
        conn.commit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()


# ISSUE: SQL injection in a different database connector (MySQL)
def get_mysql_data_vulnerable(table_name: str) -> List[Dict[str, Any]]:
    """
    Get data from a MySQL database table.
    Contains a SQL injection vulnerability with a different database connector.
    
    Example exploit: table_name = "users; DROP TABLE users; --"
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="example"
        )
        cursor = conn.cursor()
        
        # Vulnerable: Unsanitized table name
        query = f"SELECT * FROM {table_name}"
        
        cursor.execute(query)
        results = cursor.fetchall()
        
        data = []
        for row in results:
            data.append({
                "id": row[0],
                "name": row[1],
                "value": row[2]
            })
        
        return data
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()


# ISSUE: Second-order SQL injection
def create_user_report_vulnerable(username: str) -> str:
    """
    Create a report for a user.
    Contains a second-order SQL injection vulnerability.
    The username is stored in the database and later used in a query.
    
    Example exploit: username = "admin'; --"
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # First, store the username (potentially malicious)
    insert_query = f"INSERT INTO user_reports (username, created_at) VALUES ('{username}', datetime('now'))"
    
    try:
        cursor.execute(insert_query)
        report_id = cursor.lastrowid
        conn.commit()
        
        # Later, use the stored username in another query (second-order injection)
        report_query = f"SELECT * FROM users WHERE username = (SELECT username FROM user_reports WHERE id = {report_id})"
        
        cursor.execute(report_query)
        result = cursor.fetchone()
        
        if result:
            return f"Report created for user: {result[1]}"
        return "User not found"
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        return f"Error creating report: {e}"
    finally:
        conn.close()


# BETTER ALTERNATIVE: Using parameterized queries

def get_user_by_id_safe(user_id: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve a user by ID from the database using parameterized queries.
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Safe: Using parameterized query
    query = "SELECT * FROM users WHERE id = ?"
    
    try:
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        
        if result:
            return {
                "id": result[0],
                "username": result[1],
                "email": result[2]
            }
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        conn.close()


def search_users_safe(username: str) -> List[Dict[str, Any]]:
    """
    Search for users by username using parameterized queries.
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Safe: Using parameterized query with wildcards
    query = "SELECT * FROM users WHERE username LIKE ?"
    
    try:
        cursor.execute(query, (f"%{username}%",))
        results = cursor.fetchall()
        
        users = []
        for row in results:
            users.append({
                "id": row[0],
                "username": row[1],
                "email": row[2]
            })
        
        return users
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()


def filter_products_safe(category: str, min_price: str) -> List[Dict[str, Any]]:
    """
    Filter products by category and minimum price using parameterized queries.
    """
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Safe: Using parameterized query with multiple parameters
    query = "SELECT * FROM products WHERE category = ? AND price >= ?"
    
    try:
        cursor.execute(query, (category, min_price))
        results = cursor.fetchall()
        
        products = []
        for row in results:
            products.append({
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "category": row[3]
            })
        
        return products
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()


# BETTER ALTERNATIVE: Using an ORM (Object-Relational Mapping)

# Example with SQLAlchemy (commented out to avoid dependency)
"""
from sqlalchemy import create_engine, Column, Integer, String, Float, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    category = Column(String)

def get_products_with_orm(category: str, min_price: float) -> List[Dict[str, Any]]:
    engine = create_engine('sqlite:///example.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Safe: Using ORM methods
        products = session.query(Product).filter(
            Product.category == category,
            Product.price >= min_price
        ).all()
        
        return [
            {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "category": product.category
            }
            for product in products
        ]
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        session.close()
"""


# BETTER ALTERNATIVE: Validating and sanitizing input

def get_sorted_products_safe(sort_column: str) -> List[Dict[str, Any]]:
    """
    Get products sorted by the specified column with input validation.
    """
    # Validate the sort column against a whitelist of allowed columns
    allowed_columns = ['id', 'name', 'price', 'category']
    
    if sort_column not in allowed_columns:
        print(f"Invalid sort column: {sort_column}")
        sort_column = 'id'  # Default to a safe column
    
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Safe: Using validated input
    query = f"SELECT * FROM products ORDER BY {sort_column}"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        products = []
        for row in results:
            products.append({
                "id": row[0],
                "name": row[1],
                "price": row[2],
                "category": row[3]
            })
        
        return products
    except Exception as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()