"""
This module contains examples of mutable default arguments that should be flagged by SonarQube.
In Python, default argument values are evaluated only once at function definition time,
not each time the function is called. This can lead to unexpected behavior when using
mutable objects like lists, dictionaries, or sets as default arguments.
"""

import datetime


# ISSUE: Mutable list as default argument
def append_to_list(item, item_list=[]):
    """
    Append an item to a list.
    Contains an issue because it uses a mutable list as a default argument.
    """
    item_list.append(item)
    return item_list


# ISSUE: Mutable dictionary as default argument
def add_user_to_group(user_id, group_id, group_map={}):
    """
    Add a user to a group.
    Contains an issue because it uses a mutable dictionary as a default argument.
    """
    if group_id not in group_map:
        group_map[group_id] = []
    
    group_map[group_id].append(user_id)
    return group_map


# ISSUE: Mutable set as default argument
def add_tag(tag, tag_set=set()):
    """
    Add a tag to a set of tags.
    Contains an issue because it uses a mutable set as a default argument.
    """
    tag_set.add(tag)
    return tag_set


# ISSUE: Mutable default in a class method
class UserSession:
    """A class representing a user session with a mutable default argument issue."""
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.login_time = datetime.datetime.now()
    
    def add_activities(self, activities, activity_log=[]):
        """
        Add activities to the user's activity log.
        Contains an issue because it uses a mutable list as a default argument.
        """
        for activity in activities:
            activity_log.append({
                'user_id': self.user_id,
                'activity': activity,
                'timestamp': datetime.datetime.now()
            })
        
        return activity_log


# ISSUE: Nested mutable defaults
def add_employee(name, department, employee_data={'departments': {}}):
    """
    Add an employee to a department.
    Contains an issue because it uses a nested mutable dictionary as a default argument.
    """
    if department not in employee_data['departments']:
        employee_data['departments'][department] = []
    
    employee_data['departments'][department].append(name)
    return employee_data


# ISSUE: Mutable default with conditional modification
def process_request(request_id, params=None, cache={}):
    """
    Process a request with optional caching.
    Contains an issue because it uses a mutable dictionary as a default argument.
    """
    if params is None:
        params = {}
    
    if request_id in cache:
        return cache[request_id]
    
    # Process the request
    result = f"Processed request {request_id} with params {params}"
    
    # Cache the result
    cache[request_id] = result
    
    return result


# ISSUE: Multiple mutable defaults
def configure_application(app_name, settings={}, users=[], features=set()):
    """
    Configure an application with settings, users, and features.
    Contains an issue because it uses multiple mutable objects as default arguments.
    """
    settings['app_name'] = app_name
    users.append('admin')
    features.add('basic')
    
    return {
        'settings': settings,
        'users': users,
        'features': features
    }


# ISSUE: Mutable default with external function call
def get_default_config():
    """Return a default configuration dictionary."""
    return {'debug': False, 'log_level': 'INFO'}

def initialize_service(service_name, config=get_default_config()):
    """
    Initialize a service with a configuration.
    Contains an issue because the default argument is the result of a function call,
    which is evaluated only once at definition time.
    """
    config['service_name'] = service_name
    return config


# ISSUE: Mutable default in a decorator
def cache_result(func, cache={}):
    """
    A decorator that caches function results.
    Contains an issue because it uses a mutable dictionary as a default argument.
    """
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    return wrapper


# BETTER ALTERNATIVE: Using None as default and creating a new mutable object inside the function

def append_to_list_correctly(item, item_list=None):
    """
    Append an item to a list, creating a new list if none is provided.
    """
    if item_list is None:
        item_list = []
    
    item_list.append(item)
    return item_list


def add_user_to_group_correctly(user_id, group_id, group_map=None):
    """
    Add a user to a group, creating a new group map if none is provided.
    """
    if group_map is None:
        group_map = {}
    
    if group_id not in group_map:
        group_map[group_id] = []
    
    group_map[group_id].append(user_id)
    return group_map


def add_tag_correctly(tag, tag_set=None):
    """
    Add a tag to a set of tags, creating a new set if none is provided.
    """
    if tag_set is None:
        tag_set = set()
    
    tag_set.add(tag)
    return tag_set


class UserSessionCorrect:
    """A class representing a user session with proper handling of mutable defaults."""
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.login_time = datetime.datetime.now()
    
    def add_activities(self, activities, activity_log=None):
        """
        Add activities to the user's activity log, creating a new log if none is provided.
        """
        if activity_log is None:
            activity_log = []
        
        for activity in activities:
            activity_log.append({
                'user_id': self.user_id,
                'activity': activity,
                'timestamp': datetime.datetime.now()
            })
        
        return activity_log


def initialize_service_correctly(service_name, config=None):
    """
    Initialize a service with a configuration, creating a new config if none is provided.
    """
    if config is None:
        config = get_default_config()
    
    config['service_name'] = service_name
    return config


# BETTER ALTERNATIVE: Using a factory function for complex defaults

def default_employee_data():
    """Factory function to create a default employee data structure."""
    return {'departments': {}}

def add_employee_correctly(name, department, employee_data=None):
    """
    Add an employee to a department, using a factory function for the default.
    """
    if employee_data is None:
        employee_data = default_employee_data()
    
    if department not in employee_data['departments']:
        employee_data['departments'][department] = []
    
    employee_data['departments'][department].append(name)
    return employee_data


# BETTER ALTERNATIVE: Using functools.lru_cache for caching instead of mutable defaults

import functools

@functools.lru_cache(maxsize=128)
def cached_function(arg):
    """
    A function that caches its results using lru_cache instead of mutable defaults.
    """
    print(f"Computing result for {arg}")
    return arg * 2


# Demonstration of the issue with mutable defaults

def demonstrate_mutable_default_issue():
    """
    Demonstrate the issue with mutable default arguments.
    """
    # First call creates a new list [1]
    result1 = append_to_list(1)
    print(f"First call: {result1}")  # Output: [1]
    
    # Second call appends to the SAME list: [1, 2]
    result2 = append_to_list(2)
    print(f"Second call: {result2}")  # Output: [1, 2]
    
    # Third call appends to the SAME list again: [1, 2, 3]
    result3 = append_to_list(3)
    print(f"Third call: {result3}")  # Output: [1, 2, 3]
    
    # Even when we provide a new list, the next call without an argument
    # will still use the original default list
    result4 = append_to_list(4, [])
    print(f"Fourth call (with empty list): {result4}")  # Output: [4]
    
    result5 = append_to_list(5)
    print(f"Fifth call: {result5}")  # Output: [1, 2, 3, 5]


def demonstrate_correct_implementation():
    """
    Demonstrate the correct implementation without mutable default issues.
    """
    # First call creates a new list [1]
    result1 = append_to_list_correctly(1)
    print(f"First call: {result1}")  # Output: [1]
    
    # Second call creates a NEW list: [2]
    result2 = append_to_list_correctly(2)
    print(f"Second call: {result2}")  # Output: [2]
    
    # Third call creates a NEW list again: [3]
    result3 = append_to_list_correctly(3)
    print(f"Third call: {result3}")  # Output: [3]
    
    # We can still provide our own list
    result4 = append_to_list_correctly(4, [])
    print(f"Fourth call (with empty list): {result4}")  # Output: [4]
    
    # And subsequent calls still create new lists
    result5 = append_to_list_correctly(5)
    print(f"Fifth call: {result5}")  # Output: [5]


if __name__ == "__main__":
    print("Demonstrating the issue with mutable default arguments:")
    demonstrate_mutable_default_issue()
    
    print("\nDemonstrating the correct implementation:")
    demonstrate_correct_implementation()