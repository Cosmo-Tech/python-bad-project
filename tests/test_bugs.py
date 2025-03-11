"""
This module contains tests for the bugs module.
These tests are intentionally incomplete to demonstrate lack of test coverage.
"""

import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bugs.off_by_one import (
    get_last_element, sum_array, get_first_n_chars, create_matrix,
    get_last_element_correct, sum_array_correct
)
from src.bugs.mutable_defaults import (
    append_to_list, add_user_to_group, add_tag,
    append_to_list_correctly, add_user_to_group_correctly
)


class TestOffByOne(unittest.TestCase):
    """Tests for off_by_one.py module."""
    
    def test_get_last_element_empty(self):
        """Test get_last_element with empty array."""
        self.assertIsNone(get_last_element([]))
    
    def test_get_last_element_correct_empty(self):
        """Test get_last_element_correct with empty array."""
        self.assertIsNone(get_last_element_correct([]))
    
    def test_get_last_element_correct(self):
        """Test get_last_element_correct with valid array."""
        self.assertEqual(get_last_element_correct([1, 2, 3]), 3)
    
    # ISSUE: Missing test for get_last_element with valid array
    # This would catch the off-by-one error
    
    def test_sum_array_correct(self):
        """Test sum_array_correct with valid array."""
        self.assertEqual(sum_array_correct([1, 2, 3, 4]), 10)
    
    # ISSUE: Missing test for sum_array
    # This would catch the off-by-one error
    
    # ISSUE: Missing tests for other functions in off_by_one.py
    # This demonstrates incomplete test coverage


class TestMutableDefaults(unittest.TestCase):
    """Tests for mutable_defaults.py module."""
    
    def test_append_to_list_correctly_new_list(self):
        """Test append_to_list_correctly creates a new list each time."""
        result1 = append_to_list_correctly(1)
        result2 = append_to_list_correctly(2)
        
        self.assertEqual(result1, [1])
        self.assertEqual(result2, [2])
        self.assertNotEqual(id(result1), id(result2))
    
    def test_append_to_list_correctly_with_list(self):
        """Test append_to_list_correctly with provided list."""
        my_list = [1, 2, 3]
        result = append_to_list_correctly(4, my_list)
        
        self.assertEqual(result, [1, 2, 3, 4])
        self.assertEqual(id(result), id(my_list))
    
    # ISSUE: Missing test for append_to_list
    # This would demonstrate the mutable default issue
    
    def test_add_user_to_group_correctly(self):
        """Test add_user_to_group_correctly creates a new dict each time."""
        result1 = add_user_to_group_correctly(1, "admin")
        result2 = add_user_to_group_correctly(2, "user")
        
        self.assertEqual(result1, {"admin": [1]})
        self.assertEqual(result2, {"user": [2]})
        self.assertNotEqual(id(result1), id(result2))
    
    # ISSUE: Missing test for add_user_to_group
    # This would demonstrate the mutable default issue
    
    # ISSUE: Missing tests for other functions in mutable_defaults.py
    # This demonstrates incomplete test coverage


if __name__ == '__main__':
    unittest.main()