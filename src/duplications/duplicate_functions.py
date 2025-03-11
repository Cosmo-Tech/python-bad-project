"""
This module contains examples of duplicate functions that should be flagged by SonarQube.
Code duplication is a code smell that makes maintenance more difficult and increases the risk of bugs.
"""

import math
import time
from typing import List, Dict, Any, Optional, Tuple


# ISSUE: Duplicate functions with minor variations

# First version of the function
def calculate_order_total_v1(items: List[Dict[str, Any]], tax_rate: float) -> float:
    """
    Calculate the total cost of an order including tax.
    """
    subtotal = 0.0
    
    for item in items:
        item_price = item["price"]
        item_quantity = item["quantity"]
        item_total = item_price * item_quantity
        subtotal += item_total
    
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    return round(total, 2)


# Second version of the function with minor differences
def calculate_cart_total(cart_items: List[Dict[str, Any]], tax_percentage: float) -> float:
    """
    Calculate the total cost of a shopping cart including tax.
    """
    subtotal = 0.0
    
    for item in cart_items:
        item_price = item["price"]
        item_quantity = item["quantity"]
        item_total = item_price * item_quantity
        subtotal += item_total
    
    tax = subtotal * tax_percentage
    total = subtotal + tax
    
    return round(total, 2)


# ISSUE: Duplicate functions with different parameter names

# First version of the function
def get_user_full_name(first_name: str, last_name: str) -> str:
    """
    Get a user's full name by combining first and last name.
    """
    if not first_name and not last_name:
        return ""
    
    if not first_name:
        return last_name
    
    if not last_name:
        return first_name
    
    return f"{first_name} {last_name}"


# Second version of the function with different parameter names
def format_person_name(given_name: str, family_name: str) -> str:
    """
    Format a person's name by combining given name and family name.
    """
    if not given_name and not family_name:
        return ""
    
    if not given_name:
        return family_name
    
    if not family_name:
        return given_name
    
    return f"{given_name} {family_name}"


# ISSUE: Duplicate functions with different return types

# First version of the function returning a float
def calculate_circle_area_float(radius: float) -> float:
    """
    Calculate the area of a circle and return as a float.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    area = math.pi * radius * radius
    return area


# Second version of the function returning a rounded integer
def calculate_circle_area_int(radius: float) -> int:
    """
    Calculate the area of a circle and return as an integer.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    area = math.pi * radius * radius
    return round(area)


# ISSUE: Duplicate functions in different classes

class UserManager:
    """Manages user operations."""
    
    def find_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """
        Find a user by their email address.
        """
        # Simulate database lookup
        print(f"Looking up user with email: {email}")
        time.sleep(0.1)
        
        # This is a simplified example
        if "@" in email:
            return {
                "id": 123,
                "email": email,
                "name": "John Doe",
                "created_at": "2023-01-01"
            }
        
        return None


class CustomerRepository:
    """Manages customer data."""
    
    def find_customer_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """
        Find a customer by their email address.
        """
        # Simulate database lookup
        print(f"Looking up customer with email: {email}")
        time.sleep(0.1)
        
        # This is a simplified example
        if "@" in email:
            return {
                "id": 123,
                "email": email,
                "name": "John Doe",
                "created_at": "2023-01-01"
            }
        
        return None


# ISSUE: Duplicate validation logic

def validate_username(username: str) -> Tuple[bool, str]:
    """
    Validate a username.
    """
    if not username:
        return False, "Username cannot be empty"
    
    if len(username) < 3:
        return False, "Username must be at least 3 characters long"
    
    if len(username) > 20:
        return False, "Username cannot be longer than 20 characters"
    
    if not username.isalnum():
        return False, "Username can only contain letters and numbers"
    
    return True, "Username is valid"


def validate_product_code(product_code: str) -> Tuple[bool, str]:
    """
    Validate a product code.
    """
    if not product_code:
        return False, "Product code cannot be empty"
    
    if len(product_code) < 3:
        return False, "Product code must be at least 3 characters long"
    
    if len(product_code) > 20:
        return False, "Product code cannot be longer than 20 characters"
    
    if not product_code.isalnum():
        return False, "Product code can only contain letters and numbers"
    
    return True, "Product code is valid"


# ISSUE: Duplicate error handling

def fetch_user_data_v1(user_id: int) -> Dict[str, Any]:
    """
    Fetch user data from an API.
    """
    try:
        # Simulate API call
        print(f"Fetching data for user: {user_id}")
        time.sleep(0.1)
        
        # Simulate successful response
        return {
            "id": user_id,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    except ConnectionError:
        print("Connection error occurred")
        return {"error": "Failed to connect to the server"}
    except TimeoutError:
        print("Request timed out")
        return {"error": "Request timed out"}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"error": "An unexpected error occurred"}


def fetch_product_data(product_id: int) -> Dict[str, Any]:
    """
    Fetch product data from an API.
    """
    try:
        # Simulate API call
        print(f"Fetching data for product: {product_id}")
        time.sleep(0.1)
        
        # Simulate successful response
        return {
            "id": product_id,
            "name": "Sample Product",
            "price": 29.99
        }
    except ConnectionError:
        print("Connection error occurred")
        return {"error": "Failed to connect to the server"}
    except TimeoutError:
        print("Request timed out")
        return {"error": "Request timed out"}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"error": "An unexpected error occurred"}


# ISSUE: Duplicate data processing logic

def process_user_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process raw user data into a standardized format.
    """
    processed_data = {}
    
    # Extract and transform basic info
    processed_data["id"] = raw_data.get("user_id") or raw_data.get("id")
    processed_data["full_name"] = f"{raw_data.get('first_name', '')} {raw_data.get('last_name', '')}".strip()
    processed_data["email"] = raw_data.get("email", "").lower()
    
    # Process address
    address_parts = []
    if raw_data.get("address_line1"):
        address_parts.append(raw_data["address_line1"])
    if raw_data.get("address_line2"):
        address_parts.append(raw_data["address_line2"])
    if raw_data.get("city"):
        city_state = raw_data["city"]
        if raw_data.get("state"):
            city_state += f", {raw_data['state']}"
        address_parts.append(city_state)
    if raw_data.get("postal_code"):
        address_parts.append(raw_data["postal_code"])
    if raw_data.get("country"):
        address_parts.append(raw_data["country"])
    
    processed_data["address"] = ", ".join(address_parts)
    
    # Process phone number
    phone = raw_data.get("phone") or raw_data.get("phone_number") or ""
    processed_data["phone"] = phone.replace("-", "").replace(" ", "")
    
    return processed_data


def process_customer_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process raw customer data into a standardized format.
    """
    processed_data = {}
    
    # Extract and transform basic info
    processed_data["id"] = raw_data.get("customer_id") or raw_data.get("id")
    processed_data["full_name"] = f"{raw_data.get('first_name', '')} {raw_data.get('last_name', '')}".strip()
    processed_data["email"] = raw_data.get("email", "").lower()
    
    # Process address
    address_parts = []
    if raw_data.get("address_line1"):
        address_parts.append(raw_data["address_line1"])
    if raw_data.get("address_line2"):
        address_parts.append(raw_data["address_line2"])
    if raw_data.get("city"):
        city_state = raw_data["city"]
        if raw_data.get("state"):
            city_state += f", {raw_data['state']}"
        address_parts.append(city_state)
    if raw_data.get("postal_code"):
        address_parts.append(raw_data["postal_code"])
    if raw_data.get("country"):
        address_parts.append(raw_data["country"])
    
    processed_data["address"] = ", ".join(address_parts)
    
    # Process phone number
    phone = raw_data.get("phone") or raw_data.get("phone_number") or ""
    processed_data["phone"] = phone.replace("-", "").replace(" ", "")
    
    return processed_data


# BETTER ALTERNATIVE: Refactored functions to eliminate duplication

def calculate_total(items: List[Dict[str, Any]], tax_rate: float) -> float:
    """
    Calculate the total cost of items including tax.
    """
    subtotal = sum(item["price"] * item["quantity"] for item in items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    return round(total, 2)


def format_name(first: str, last: str) -> str:
    """
    Format a name by combining first and last parts.
    """
    if not first and not last:
        return ""
    
    if not first:
        return last
    
    if not last:
        return first
    
    return f"{first} {last}"


def calculate_circle_area(radius: float, round_to_int: bool = False) -> float:
    """
    Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle
        round_to_int: Whether to round the result to the nearest integer
        
    Returns:
        The area of the circle
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    area = math.pi * radius * radius
    
    if round_to_int:
        return round(area)
    
    return area


class Repository:
    """Generic repository for data access."""
    
    def find_by_email(self, email: str, entity_type: str = "user") -> Optional[Dict[str, Any]]:
        """
        Find an entity by email address.
        
        Args:
            email: The email address to search for
            entity_type: The type of entity (user, customer, etc.)
            
        Returns:
            The entity data if found, None otherwise
        """
        # Simulate database lookup
        print(f"Looking up {entity_type} with email: {email}")
        time.sleep(0.1)
        
        # This is a simplified example
        if "@" in email:
            return {
                "id": 123,
                "email": email,
                "name": "John Doe",
                "created_at": "2023-01-01",
                "type": entity_type
            }
        
        return None


def validate_alphanumeric_code(code: str, code_type: str = "code") -> Tuple[bool, str]:
    """
    Validate an alphanumeric code.
    
    Args:
        code: The code to validate
        code_type: The type of code (username, product code, etc.)
        
    Returns:
        A tuple of (is_valid, message)
    """
    if not code:
        return False, f"{code_type.capitalize()} cannot be empty"
    
    if len(code) < 3:
        return False, f"{code_type.capitalize()} must be at least 3 characters long"
    
    if len(code) > 20:
        return False, f"{code_type.capitalize()} cannot be longer than 20 characters"
    
    if not code.isalnum():
        return False, f"{code_type.capitalize()} can only contain letters and numbers"
    
    return True, f"{code_type.capitalize()} is valid"


def fetch_data_with_error_handling(entity_id: int, entity_type: str = "user") -> Dict[str, Any]:
    """
    Fetch data from an API with standardized error handling.
    
    Args:
        entity_id: The ID of the entity to fetch
        entity_type: The type of entity (user, product, etc.)
        
    Returns:
        The entity data or an error response
    """
    try:
        # Simulate API call
        print(f"Fetching data for {entity_type}: {entity_id}")
        time.sleep(0.1)
        
        # Simulate successful response based on entity type
        if entity_type == "user":
            return {
                "id": entity_id,
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        elif entity_type == "product":
            return {
                "id": entity_id,
                "name": "Sample Product",
                "price": 29.99
            }
        else:
            return {
                "id": entity_id,
                "type": entity_type
            }
    except ConnectionError:
        print("Connection error occurred")
        return {"error": "Failed to connect to the server"}
    except TimeoutError:
        print("Request timed out")
        return {"error": "Request timed out"}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"error": "An unexpected error occurred"}


def process_entity_data(raw_data: Dict[str, Any], entity_type: str = "user") -> Dict[str, Any]:
    """
    Process raw entity data into a standardized format.
    
    Args:
        raw_data: The raw data to process
        entity_type: The type of entity (user, customer, etc.)
        
    Returns:
        The processed data
    """
    processed_data = {}
    
    # Extract and transform basic info
    id_field = f"{entity_type}_id" if entity_type != "user" else "user_id"
    processed_data["id"] = raw_data.get(id_field) or raw_data.get("id")
    processed_data["full_name"] = f"{raw_data.get('first_name', '')} {raw_data.get('last_name', '')}".strip()
    processed_data["email"] = raw_data.get("email", "").lower()
    
    # Process address
    address_parts = []
    if raw_data.get("address_line1"):
        address_parts.append(raw_data["address_line1"])
    if raw_data.get("address_line2"):
        address_parts.append(raw_data["address_line2"])
    if raw_data.get("city"):
        city_state = raw_data["city"]
        if raw_data.get("state"):
            city_state += f", {raw_data['state']}"
        address_parts.append(city_state)
    if raw_data.get("postal_code"):
        address_parts.append(raw_data["postal_code"])
    if raw_data.get("country"):
        address_parts.append(raw_data["country"])
    
    processed_data["address"] = ", ".join(address_parts)
    
    # Process phone number
    phone = raw_data.get("phone") or raw_data.get("phone_number") or ""
    processed_data["phone"] = phone.replace("-", "").replace(" ", "")
    
    # Add entity type
    processed_data["type"] = entity_type
    
    return processed_data