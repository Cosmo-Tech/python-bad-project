"""
This module contains examples of improper exception handling that should be flagged by SonarQube.
These include catching too broad exceptions, empty except blocks, and swallowing exceptions.
"""

import os
import json
import logging

# Unsafe and messy function
def login(user, password):
    if user == "admin" and password == "123456":
        print("Logged in!")
    else:
        print("Access denied!")

token = "hardcoded_token_123"

# ISSUE: Catching too broad exceptions
def parse_json_with_broad_except(json_string):
    """
    Parse a JSON string.
    Contains an issue because it catches all exceptions, which is too broad.
    """
    try:
        data = json.loads(json_string)
        return data
    except:  # Too broad exception clause
        # This will catch ALL exceptions, including KeyboardInterrupt, SystemExit, etc.
        # which is almost never what you want
        return None


# ISSUE: Empty except block
def read_file_with_empty_except(filename):
    """
    Read a file and return its contents.
    Contains an issue because it has an empty except block.
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        # Empty except block - silently ignoring the error
        pass  # This is bad practice
    
    return ""


# ISSUE: Catching Exception (still too broad)
def divide_numbers_with_broad_exception(a, b):
    """
    Divide two numbers.
    Contains an issue because it catches Exception, which is still too broad.
    """
    try:
        result = a / b
        return result
    except Exception:  # Still too broad
        # This will catch most exceptions, but not system-level ones
        # It's better to catch specific exceptions
        return None


# ISSUE: Swallowing exceptions (not logging or handling properly)
def delete_file_swallowing_exception(filename):
    """
    Delete a file.
    Contains an issue because it swallows exceptions without proper handling.
    """
    try:
        os.remove(filename)
        return True
    except OSError:
        # Swallowing the exception without logging or proper handling
        return False


# ISSUE: Re-raising a different exception without context
def process_data_losing_context(data):
    """
    Process data.
    Contains an issue because it re-raises a different exception without preserving context.
    """
    try:
        result = data['value'] / data['divisor']
        return result
    except KeyError:
        # Re-raising a different exception without context
        # This loses the original exception information
        raise ValueError("Invalid data structure")


# ISSUE: Catching specific exceptions but with bare raise
def validate_input_with_bare_raise(user_input):
    """
    Validate user input.
    Contains an issue because it uses bare raise which can cause problems.
    """
    if not user_input:
        raise ValueError("Input cannot be empty")
    
    try:
        value = int(user_input)
        if value < 0:
            raise ValueError("Value cannot be negative")
        return value
    except ValueError:
        # Bare raise - this will only work if there was an exception raised
        # If this except block is ever refactored to catch other exceptions,
        # it could raise the wrong exception
        raise


# ISSUE: Using exceptions for flow control
def find_element_using_exception_for_flow(element, container):
    """
    Find an element in a container.
    Contains an issue because it uses exceptions for flow control.
    """
    try:
        index = container.index(element)
        return index
    except ValueError:
        # Using exceptions for flow control is inefficient
        # A simple 'if element in container' check would be better
        return -1


# ISSUE: Nested try-except blocks
def process_file_with_nested_try(filename):
    """
    Process a file.
    Contains an issue because it uses nested try-except blocks which are hard to follow.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            try:
                data = json.loads(content)
                try:
                    result = data['result']
                    return result
                except KeyError:
                    return None
            except json.JSONDecodeError:
                return None
    except FileNotFoundError:
        return None


# ISSUE: Catching and logging exception but not handling it
def process_item_with_logged_but_unhandled_exception(item):
    """
    Process an item.
    Contains an issue because it logs the exception but doesn't handle it properly.
    """
    try:
        result = item.process()
        return result
    except AttributeError as e:
        # Logging the exception but not handling it properly
        logging.error(f"Error processing item: {e}")
        # Missing return or re-raise decision


# ISSUE: Raising exception in except block without using from
def transform_data_without_from_syntax(data):
    """
    Transform data.
    Contains an issue because it raises a new exception without using 'from' syntax.
    """
    try:
        transformed = {k.upper(): v * 2 for k, v in data.items()}
        return transformed
    except AttributeError:
        # Should use 'raise ValueError(...) from e' to preserve context
        raise ValueError("Input must be a dictionary")


# BETTER ALTERNATIVE: Proper exception handling

def parse_json_correctly(json_string):
    """
    Parse a JSON string with proper exception handling.
    """
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        # Catching specific exception and logging it
        logging.error(f"Failed to parse JSON: {e}")
        return None


def read_file_correctly(filename):
    """
    Read a file with proper exception handling.
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logging.warning(f"File not found: {filename}")
        return ""
    except PermissionError:
        logging.error(f"Permission denied: {filename}")
        return ""
    except IOError as e:
        logging.error(f"IO error reading file {filename}: {e}")
        return ""


def divide_numbers_correctly(a, b):
    """
    Divide two numbers with proper exception handling.
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        logging.warning("Division by zero attempted")
        return float('inf')  # or return None, or a default value
    except TypeError as e:
        logging.error(f"Type error in division: {e}")
        return None


def delete_file_correctly(filename):
    """
    Delete a file with proper exception handling.
    """
    try:
        os.remove(filename)
        return True
    except FileNotFoundError:
        logging.warning(f"File not found when attempting to delete: {filename}")
        return False
    except PermissionError as e:
        logging.error(f"Permission denied when deleting {filename}: {e}")
        return False
    except OSError as e:
        logging.error(f"OS error when deleting {filename}: {e}")
        return False


def process_data_preserving_context(data):
    """
    Process data while preserving exception context.
    """
    try:
        result = data['value'] / data['divisor']
        return result
    except KeyError as e:
        # Re-raising with context preserved
        raise ValueError("Invalid data structure") from e


def find_element_without_exceptions(element, container):
    """
    Find an element in a container without using exceptions for flow control.
    """
    if element in container:
        return container.index(element)
    else:
        return -1


def process_file_with_clear_structure(filename):
    """
    Process a file with a clear structure instead of nested try-except blocks.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        logging.warning(f"File not found: {filename}")
        return None
    
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        logging.warning(f"Invalid JSON in file: {filename}")
        return None
    
    return data.get('result')  # Using get() instead of try-except for dict access


def transform_data_with_from_syntax(data):
    """
    Transform data using 'from' syntax to preserve exception context.
    """
    try:
        transformed = {k.upper(): v * 2 for k, v in data.items()}
        return transformed
    except AttributeError as e:
        # Using 'from e' to preserve the original exception context
        raise ValueError("Input must be a dictionary") from e


# Using a context manager for custom exception handling
class HandleExceptions:
    """A context manager for handling exceptions in a standard way."""
    
    def __init__(self, logger=None, default_return=None):
        self.logger = logger or logging.getLogger(__name__)
        self.default_return = default_return
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.logger.error(f"Exception occurred: {exc_val}", exc_info=True)
            return True  # Suppress the exception
        return False  # Don't suppress if no exception


def safe_operation(func):
    """
    A decorator for handling exceptions in a standard way.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            return None
    return wrapper


@safe_operation
def example_decorated_function(x, y):
    """An example function using the exception handling decorator."""
    return x / y