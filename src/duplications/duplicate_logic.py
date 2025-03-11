"""
This module contains examples of duplicate logic patterns that should be flagged by SonarQube.
These include repeated code blocks, similar algorithms, and other duplicated logic patterns.
"""

import datetime
import json
import os
import random
import time
from typing import List, Dict, Any, Optional, Tuple, Union


# ISSUE: Duplicate logic in conditional branches

def process_payment_v1(payment_method: str, amount: float) -> Dict[str, Any]:
    """
    Process a payment using different payment methods.
    Contains duplicate logic in conditional branches.
    """
    transaction_id = f"TXN-{random.randint(10000, 99999)}"
    timestamp = datetime.datetime.now().isoformat()
    
    if payment_method == "credit_card":
        # Process credit card payment
        print(f"Processing credit card payment of ${amount:.2f}")
        time.sleep(0.5)  # Simulate processing time
        
        # Log the transaction
        print(f"Logging transaction {transaction_id}")
        
        # Send confirmation email
        print("Sending confirmation email")
        
        # Update account balance
        print("Updating account balance")
        
        return {
            "transaction_id": transaction_id,
            "payment_method": payment_method,
            "amount": amount,
            "status": "completed",
            "timestamp": timestamp
        }
    
    elif payment_method == "paypal":
        # Process PayPal payment
        print(f"Processing PayPal payment of ${amount:.2f}")
        time.sleep(0.5)  # Simulate processing time
        
        # Log the transaction
        print(f"Logging transaction {transaction_id}")
        
        # Send confirmation email
        print("Sending confirmation email")
        
        # Update account balance
        print("Updating account balance")
        
        return {
            "transaction_id": transaction_id,
            "payment_method": payment_method,
            "amount": amount,
            "status": "completed",
            "timestamp": timestamp
        }
    
    elif payment_method == "bank_transfer":
        # Process bank transfer
        print(f"Processing bank transfer of ${amount:.2f}")
        time.sleep(0.5)  # Simulate processing time
        
        # Log the transaction
        print(f"Logging transaction {transaction_id}")
        
        # Send confirmation email
        print("Sending confirmation email")
        
        # Update account balance
        print("Updating account balance")
        
        return {
            "transaction_id": transaction_id,
            "payment_method": payment_method,
            "amount": amount,
            "status": "completed",
            "timestamp": timestamp
        }
    
    else:
        return {
            "transaction_id": transaction_id,
            "payment_method": payment_method,
            "amount": amount,
            "status": "failed",
            "timestamp": timestamp,
            "error": "Unsupported payment method"
        }


# ISSUE: Duplicate logic in try-except blocks

def load_user_data(user_id: int) -> Optional[Dict[str, Any]]:
    """
    Load user data from a JSON file.
    Contains duplicate logic in try-except blocks.
    """
    file_path = f"data/users/{user_id}.json"
    
    try:
        if not os.path.exists(file_path):
            print(f"User data file not found: {file_path}")
            return None
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        return data
    except json.JSONDecodeError:
        print(f"Invalid JSON in user data file: {file_path}")
        return None
    except PermissionError:
        print(f"Permission denied when reading user data file: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading user data: {e}")
        return None


def load_product_data(product_id: int) -> Optional[Dict[str, Any]]:
    """
    Load product data from a JSON file.
    Contains duplicate logic in try-except blocks.
    """
    file_path = f"data/products/{product_id}.json"
    
    try:
        if not os.path.exists(file_path):
            print(f"Product data file not found: {file_path}")
            return None
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        return data
    except json.JSONDecodeError:
        print(f"Invalid JSON in product data file: {file_path}")
        return None
    except PermissionError:
        print(f"Permission denied when reading product data file: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading product data: {e}")
        return None


# ISSUE: Duplicate logic in loops

def calculate_order_statistics_v1(orders: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calculate statistics for a list of orders.
    Contains duplicate logic in loops.
    """
    total_amount = 0
    total_items = 0
    total_tax = 0
    total_shipping = 0
    
    # Calculate totals
    for order in orders:
        total_amount += order["amount"]
        total_items += order["items"]
        total_tax += order["tax"]
        total_shipping += order["shipping"]
    
    # Calculate averages
    avg_amount = total_amount / len(orders) if orders else 0
    avg_items = total_items / len(orders) if orders else 0
    avg_tax = total_tax / len(orders) if orders else 0
    avg_shipping = total_shipping / len(orders) if orders else 0
    
    return {
        "avg_amount": round(avg_amount, 2),
        "avg_items": round(avg_items, 2),
        "avg_tax": round(avg_tax, 2),
        "avg_shipping": round(avg_shipping, 2)
    }


def calculate_product_statistics(products: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calculate statistics for a list of products.
    Contains duplicate logic in loops.
    """
    total_price = 0
    total_cost = 0
    total_weight = 0
    total_stock = 0
    
    # Calculate totals
    for product in products:
        total_price += product["price"]
        total_cost += product["cost"]
        total_weight += product["weight"]
        total_stock += product["stock"]
    
    # Calculate averages
    avg_price = total_price / len(products) if products else 0
    avg_cost = total_cost / len(products) if products else 0
    avg_weight = total_weight / len(products) if products else 0
    avg_stock = total_stock / len(products) if products else 0
    
    return {
        "avg_price": round(avg_price, 2),
        "avg_cost": round(avg_cost, 2),
        "avg_weight": round(avg_weight, 2),
        "avg_stock": round(avg_stock, 2)
    }


# ISSUE: Duplicate logic in string formatting

def format_user_address(user: Dict[str, Any]) -> str:
    """
    Format a user's address as a string.
    Contains duplicate logic in string formatting.
    """
    address_parts = []
    
    # Add name
    name = f"{user.get('first_name', '')} {user.get('last_name', '')}".strip()
    if name:
        address_parts.append(name)
    
    # Add street address
    street = user.get('street_address', '')
    if street:
        address_parts.append(street)
    
    # Add apartment/unit
    apartment = user.get('apartment', '')
    if apartment:
        address_parts.append(f"Apt {apartment}")
    
    # Add city, state, zip
    city = user.get('city', '')
    state = user.get('state', '')
    zip_code = user.get('zip_code', '')
    
    city_state_zip = ""
    if city:
        city_state_zip = city
    if state:
        city_state_zip += f", {state}" if city_state_zip else state
    if zip_code:
        city_state_zip += f" {zip_code}" if city_state_zip else zip_code
    
    if city_state_zip:
        address_parts.append(city_state_zip)
    
    # Add country
    country = user.get('country', '')
    if country:
        address_parts.append(country)
    
    return "\n".join(address_parts)


def format_shipping_address(shipping: Dict[str, Any]) -> str:
    """
    Format a shipping address as a string.
    Contains duplicate logic in string formatting.
    """
    address_parts = []
    
    # Add recipient name
    name = f"{shipping.get('recipient_first_name', '')} {shipping.get('recipient_last_name', '')}".strip()
    if name:
        address_parts.append(name)
    
    # Add street address
    street = shipping.get('street_address', '')
    if street:
        address_parts.append(street)
    
    # Add apartment/unit
    apartment = shipping.get('apartment', '')
    if apartment:
        address_parts.append(f"Apt {apartment}")
    
    # Add city, state, zip
    city = shipping.get('city', '')
    state = shipping.get('state', '')
    zip_code = shipping.get('zip_code', '')
    
    city_state_zip = ""
    if city:
        city_state_zip = city
    if state:
        city_state_zip += f", {state}" if city_state_zip else state
    if zip_code:
        city_state_zip += f" {zip_code}" if city_state_zip else zip_code
    
    if city_state_zip:
        address_parts.append(city_state_zip)
    
    # Add country
    country = shipping.get('country', '')
    if country:
        address_parts.append(country)
    
    return "\n".join(address_parts)


# ISSUE: Duplicate logic in data validation

def validate_user_input(data: Dict[str, Any]) -> List[str]:
    """
    Validate user input data.
    Contains duplicate validation logic.
    """
    errors = []
    
    # Validate name
    if not data.get('first_name'):
        errors.append("First name is required")
    
    if not data.get('last_name'):
        errors.append("Last name is required")
    
    # Validate email
    email = data.get('email', '')
    if not email:
        errors.append("Email is required")
    elif '@' not in email or '.' not in email:
        errors.append("Email is invalid")
    
    # Validate age
    age = data.get('age')
    if age is None:
        errors.append("Age is required")
    elif not isinstance(age, int):
        errors.append("Age must be a number")
    elif age < 18:
        errors.append("You must be at least 18 years old")
    elif age > 120:
        errors.append("Age is invalid")
    
    # Validate password
    password = data.get('password', '')
    if not password:
        errors.append("Password is required")
    elif len(password) < 8:
        errors.append("Password must be at least 8 characters long")
    elif not any(c.isupper() for c in password):
        errors.append("Password must contain at least one uppercase letter")
    elif not any(c.islower() for c in password):
        errors.append("Password must contain at least one lowercase letter")
    elif not any(c.isdigit() for c in password):
        errors.append("Password must contain at least one number")
    
    return errors


def validate_product_input(data: Dict[str, Any]) -> List[str]:
    """
    Validate product input data.
    Contains duplicate validation logic.
    """
    errors = []
    
    # Validate name
    if not data.get('name'):
        errors.append("Product name is required")
    
    if not data.get('sku'):
        errors.append("SKU is required")
    
    # Validate description
    description = data.get('description', '')
    if not description:
        errors.append("Description is required")
    elif len(description) < 10:
        errors.append("Description must be at least 10 characters long")
    
    # Validate price
    price = data.get('price')
    if price is None:
        errors.append("Price is required")
    elif not isinstance(price, (int, float)):
        errors.append("Price must be a number")
    elif price < 0:
        errors.append("Price cannot be negative")
    elif price > 10000:
        errors.append("Price is too high")
    
    # Validate stock
    stock = data.get('stock')
    if stock is None:
        errors.append("Stock is required")
    elif not isinstance(stock, int):
        errors.append("Stock must be a whole number")
    elif stock < 0:
        errors.append("Stock cannot be negative")
    
    return errors


# ISSUE: Duplicate logic in file operations

def save_user_data(user_id: int, data: Dict[str, Any]) -> bool:
    """
    Save user data to a JSON file.
    Contains duplicate file operation logic.
    """
    directory = "data/users"
    file_path = f"{directory}/{user_id}.json"
    
    # Ensure directory exists
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except Exception as e:
            print(f"Error creating directory: {e}")
            return False
    
    # Save data to file
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving user data: {e}")
        return False


def save_product_data(product_id: int, data: Dict[str, Any]) -> bool:
    """
    Save product data to a JSON file.
    Contains duplicate file operation logic.
    """
    directory = "data/products"
    file_path = f"{directory}/{product_id}.json"
    
    # Ensure directory exists
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except Exception as e:
            print(f"Error creating directory: {e}")
            return False
    
    # Save data to file
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving product data: {e}")
        return False


# BETTER ALTERNATIVE: Refactored code to eliminate duplication

def process_payment_better(payment_method: str, amount: float) -> Dict[str, Any]:
    """
    Process a payment using different payment methods.
    Refactored to eliminate duplicate logic.
    """
    transaction_id = f"TXN-{random.randint(10000, 99999)}"
    timestamp = datetime.datetime.now().isoformat()
    
    # Check if payment method is supported
    supported_methods = ["credit_card", "paypal", "bank_transfer"]
    if payment_method not in supported_methods:
        return {
            "transaction_id": transaction_id,
            "payment_method": payment_method,
            "amount": amount,
            "status": "failed",
            "timestamp": timestamp,
            "error": "Unsupported payment method"
        }
    
    # Process payment (method-specific logic would go here)
    print(f"Processing {payment_method} payment of ${amount:.2f}")
    time.sleep(0.5)  # Simulate processing time
    
    # Common post-payment operations
    print(f"Logging transaction {transaction_id}")
    print("Sending confirmation email")
    print("Updating account balance")
    
    return {
        "transaction_id": transaction_id,
        "payment_method": payment_method,
        "amount": amount,
        "status": "completed",
        "timestamp": timestamp
    }


def load_data_from_json(entity_type: str, entity_id: int) -> Optional[Dict[str, Any]]:
    """
    Load data from a JSON file.
    Generic function that handles different entity types.
    """
    file_path = f"data/{entity_type}s/{entity_id}.json"
    
    try:
        if not os.path.exists(file_path):
            print(f"{entity_type.capitalize()} data file not found: {file_path}")
            return None
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        return data
    except json.JSONDecodeError:
        print(f"Invalid JSON in {entity_type} data file: {file_path}")
        return None
    except PermissionError:
        print(f"Permission denied when reading {entity_type} data file: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading {entity_type} data: {e}")
        return None


def calculate_statistics(items: List[Dict[str, Any]], fields: List[str]) -> Dict[str, float]:
    """
    Calculate statistics for a list of items.
    Generic function that works with different item types and fields.
    """
    totals = {field: 0 for field in fields}
    
    # Calculate totals
    for item in items:
        for field in fields:
            totals[field] += item.get(field, 0)
    
    # Calculate averages
    averages = {}
    for field in fields:
        avg = totals[field] / len(items) if items else 0
        averages[f"avg_{field}"] = round(avg, 2)
    
    return averages


def format_address(address_data: Dict[str, Any], name_prefix: str = "") -> str:
    """
    Format an address as a string.
    Generic function that works with different address data structures.
    """
    address_parts = []
    
    # Add name (with configurable prefix for different field names)
    first_name_field = f"{name_prefix}first_name" if name_prefix else "first_name"
    last_name_field = f"{name_prefix}last_name" if name_prefix else "last_name"
    
    name = f"{address_data.get(first_name_field, '')} {address_data.get(last_name_field, '')}".strip()
    if name:
        address_parts.append(name)
    
    # Add street address
    street = address_data.get('street_address', '')
    if street:
        address_parts.append(street)
    
    # Add apartment/unit
    apartment = address_data.get('apartment', '')
    if apartment:
        address_parts.append(f"Apt {apartment}")
    
    # Add city, state, zip
    city = address_data.get('city', '')
    state = address_data.get('state', '')
    zip_code = address_data.get('zip_code', '')
    
    city_state_zip = ""
    if city:
        city_state_zip = city
    if state:
        city_state_zip += f", {state}" if city_state_zip else state
    if zip_code:
        city_state_zip += f" {zip_code}" if city_state_zip else zip_code
    
    if city_state_zip:
        address_parts.append(city_state_zip)
    
    # Add country
    country = address_data.get('country', '')
    if country:
        address_parts.append(country)
    
    return "\n".join(address_parts)


def validate_input(data: Dict[str, Any], validation_rules: Dict[str, Dict[str, Any]]) -> List[str]:
    """
    Validate input data against a set of rules.
    Generic function that works with different data types and validation rules.
    """
    errors = []
    
    for field, rules in validation_rules.items():
        value = data.get(field)
        
        # Required check
        if rules.get('required', False) and (value is None or value == ''):
            errors.append(f"{rules.get('label', field)} is required")
            continue
        
        # Skip further validation if value is empty and not required
        if value is None or value == '':
            continue
        
        # Type check
        expected_type = rules.get('type')
        if expected_type:
            if expected_type == 'string' and not isinstance(value, str):
                errors.append(f"{rules.get('label', field)} must be a string")
            elif expected_type == 'number' and not isinstance(value, (int, float)):
                errors.append(f"{rules.get('label', field)} must be a number")
            elif expected_type == 'integer' and not isinstance(value, int):
                errors.append(f"{rules.get('label', field)} must be a whole number")
            elif expected_type == 'email' and (not isinstance(value, str) or '@' not in value or '.' not in value):
                errors.append(f"{rules.get('label', field)} is invalid")
        
        # Min/max checks for strings
        if isinstance(value, str):
            min_length = rules.get('min_length')
            if min_length is not None and len(value) < min_length:
                errors.append(f"{rules.get('label', field)} must be at least {min_length} characters long")
            
            max_length = rules.get('max_length')
            if max_length is not None and len(value) > max_length:
                errors.append(f"{rules.get('label', field)} cannot be longer than {max_length} characters")
        
        # Min/max checks for numbers
        if isinstance(value, (int, float)):
            min_value = rules.get('min_value')
            if min_value is not None and value < min_value:
                errors.append(f"{rules.get('label', field)} must be at least {min_value}")
            
            max_value = rules.get('max_value')
            if max_value is not None and value > max_value:
                errors.append(f"{rules.get('label', field)} cannot be greater than {max_value}")
        
        # Custom validation
        custom_validator = rules.get('validator')
        if custom_validator and callable(custom_validator):
            result = custom_validator(value)
            if result is not True:
                errors.append(result if isinstance(result, str) else f"{rules.get('label', field)} is invalid")
    
    return errors


def save_data_to_json(entity_type: str, entity_id: int, data: Dict[str, Any]) -> bool:
    """
    Save data to a JSON file.
    Generic function that handles different entity types.
    """
    directory = f"data/{entity_type}s"
    file_path = f"{directory}/{entity_id}.json"
    
    # Ensure directory exists
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except Exception as e:
            print(f"Error creating directory: {e}")
            return False
    
    # Save data to file
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving {entity_type} data: {e}")
        return False


# Example usage of the refactored functions

def example_usage():
    """Example usage of the refactored functions."""
    
    # Process payment
    payment_result = process_payment_better("credit_card", 99.99)
    print(payment_result)
    
    # Load data
    user_data = load_data_from_json("user", 123)
    product_data = load_data_from_json("product", 456)
    
    # Calculate statistics
    orders = [
        {"amount": 100, "items": 5, "tax": 8, "shipping": 10},
        {"amount": 200, "items": 10, "tax": 16, "shipping": 15}
    ]
    order_stats = calculate_statistics(orders, ["amount", "items", "tax", "shipping"])
    print(order_stats)
    
    # Format address
    address_data = {
        "first_name": "John",
        "last_name": "Doe",
        "street_address": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip_code": "12345",
        "country": "USA"
    }
    formatted_address = format_address(address_data)
    print(formatted_address)
    
    # Validate input
    user_validation_rules = {
        "first_name": {"required": True, "type": "string", "label": "First name"},
        "email": {"required": True, "type": "email", "label": "Email address"},
        "age": {"required": True, "type": "integer", "min_value": 18, "max_value": 120, "label": "Age"}
    }
    
    user_input = {
        "first_name": "Jane",
        "email": "jane@example.com",
        "age": 25
    }
    
    validation_errors = validate_input(user_input, user_validation_rules)
    if validation_errors:
        print("Validation errors:", validation_errors)
    else:
        print("Input is valid")
    
    # Save data
    save_result = save_data_to_json("user", 123, user_input)
    print(f"Save result: {save_result}")


if __name__ == "__main__":
    example_usage()