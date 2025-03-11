"""
This module contains examples of off-by-one errors that should be flagged by SonarQube.
These include array indexing issues, loop boundary errors, and buffer overflows.
"""


# ISSUE: Off-by-one error in array indexing
def get_last_element(array):
    """
    Attempt to get the last element of an array.
    Contains an off-by-one error using len(array) instead of len(array) - 1.
    """
    if not array:
        return None
    
    # Off-by-one error: This will cause an IndexError
    return array[len(array)]  # Should be array[len(array) - 1]


# ISSUE: Off-by-one error in loop boundary
def sum_array(array):
    """
    Sum all elements in an array.
    Contains an off-by-one error in the loop boundary.
    """
    total = 0
    
    # Off-by-one error: Loop will miss the last element
    for i in range(0, len(array) - 1):  # Should be range(0, len(array))
        total += array[i]
    
    return total


# ISSUE: Off-by-one error in string slicing
def get_first_n_chars(text, n):
    """
    Get the first n characters of a string.
    Contains an off-by-one error in string slicing.
    """
    if not text:
        return ""
    
    # Off-by-one error: Will return n+1 characters
    return text[0:n+1]  # Should be text[0:n]


# ISSUE: Off-by-one error in array initialization
def create_matrix(rows, cols, initial_value=0):
    """
    Create a matrix with the specified dimensions.
    Contains an off-by-one error in matrix initialization.
    """
    matrix = []
    
    # Off-by-one error: Creates rows+1 rows
    for i in range(rows + 1):  # Should be range(rows)
        row = [initial_value] * cols
        matrix.append(row)
    
    return matrix


# ISSUE: Off-by-one error in buffer allocation
def copy_data(source, max_length):
    """
    Copy data from source up to max_length.
    Contains an off-by-one error in buffer allocation.
    """
    # Off-by-one error: Buffer is too small
    buffer = [0] * max_length  # Should be [0] * (max_length + 1) to include null terminator
    
    for i in range(min(len(source), max_length)):
        buffer[i] = source[i]
    
    return buffer


# ISSUE: Off-by-one error in binary search
def binary_search(sorted_array, target):
    """
    Perform binary search on a sorted array.
    Contains an off-by-one error in the high index initialization.
    """
    if not sorted_array:
        return -1
    
    low = 0
    # Off-by-one error: high should be len(sorted_array) - 1
    high = len(sorted_array)  # Should be len(sorted_array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # This can cause IndexError when mid = len(sorted_array)
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


# ISSUE: Off-by-one error in range check
def is_valid_index(array, index):
    """
    Check if an index is valid for an array.
    Contains an off-by-one error in the range check.
    """
    # Off-by-one error: Should be index < len(array)
    return 0 <= index <= len(array)  # Should be 0 <= index < len(array)


# ISSUE: Off-by-one error in pagination
def paginate_results(results, page_size, page_number):
    """
    Paginate results based on page size and page number.
    Contains an off-by-one error in calculating the start index.
    """
    total_results = len(results)
    
    # Off-by-one error: Page numbers should start at 0 or the calculation should be different
    start_index = page_number * page_size  # If page_number is 1-based, should be (page_number - 1) * page_size
    end_index = min(start_index + page_size, total_results)
    
    # This can return an empty list for the last page if page_number is 1-based
    return results[start_index:end_index]


# ISSUE: Off-by-one error in calculating array capacity
def ensure_capacity(array, min_capacity):
    """
    Ensure an array has at least the specified capacity.
    Contains an off-by-one error in calculating the new capacity.
    """
    current_capacity = len(array)
    
    if current_capacity >= min_capacity:
        return array
    
    # Off-by-one error: New capacity calculation
    new_capacity = min_capacity  # Should typically be min_capacity * 2 or similar growth factor
    
    # Create new array with increased capacity
    new_array = [None] * new_capacity
    
    # Copy elements from old array to new array
    for i in range(current_capacity):
        new_array[i] = array[i]
    
    return new_array


# BETTER ALTERNATIVE: Correct implementations

def get_last_element_correct(array):
    """Correctly get the last element of an array."""
    if not array:
        return None
    
    return array[len(array) - 1]


def sum_array_correct(array):
    """Correctly sum all elements in an array."""
    total = 0
    
    for i in range(len(array)):
        total += array[i]
    
    # Alternative using Python's built-in sum function
    # total = sum(array)
    
    return total


def binary_search_correct(sorted_array, target):
    """Correctly perform binary search on a sorted array."""
    if not sorted_array:
        return -1
    
    low = 0
    high = len(sorted_array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


def is_valid_index_correct(array, index):
    """Correctly check if an index is valid for an array."""
    return 0 <= index < len(array)


def paginate_results_correct(results, page_size, page_number):
    """Correctly paginate results based on page size and page number (0-based)."""
    total_results = len(results)
    
    start_index = page_number * page_size
    end_index = min(start_index + page_size, total_results)
    
    return results[start_index:end_index]