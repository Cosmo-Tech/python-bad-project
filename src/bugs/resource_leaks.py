"""
This module contains examples of resource leaks that should be flagged by SonarQube.
These include unclosed files, database connections, and other resources that should be properly managed.
"""

import os
import sqlite3
import threading
import tempfile
from contextlib import contextmanager


# ISSUE: File resource leak - file not closed
def read_file_with_leak(filename):
    """
    Read a file and return its contents.
    Contains a resource leak because the file is not closed.
    """
    # Resource leak: file is opened but never closed
    file = open(filename, 'r')
    content = file.read()
    
    # Missing file.close()
    
    return content


# ISSUE: Database connection leak
def query_database_with_leak(db_path, query):
    """
    Execute a query on a SQLite database.
    Contains a resource leak because the connection is not closed.
    """
    # Resource leak: connection is opened but never closed
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Missing cursor.close()
    # Missing connection.close()
    
    return results


# ISSUE: Multiple resource leaks in exception handling
def process_data_with_leak(input_file, output_file):
    """
    Process data from input file and write to output file.
    Contains resource leaks in exception handling.
    """
    input_handle = None
    output_handle = None
    
    try:
        input_handle = open(input_file, 'r')
        output_handle = open(output_file, 'w')
        
        for line in input_handle:
            processed_line = line.strip().upper()
            output_handle.write(processed_line + '\n')
            
        # If an exception occurs, the files won't be closed
        
    except Exception as e:
        print(f"Error processing files: {e}")
        
        # Missing proper cleanup in exception handler
        
    # Files should be closed in a finally block
    
    return True


# ISSUE: Thread resource leak
def create_thread_with_leak():
    """
    Create a worker thread.
    Contains a resource leak because the thread is not joined.
    """
    def worker():
        """Worker function that simulates long-running task."""
        import time
        print("Worker thread starting")
        time.sleep(2)
        print("Worker thread finished")
    
    # Resource leak: thread is created but never joined
    thread = threading.Thread(target=worker)
    thread.start()
    
    # Missing thread.join()
    
    print("Main thread continuing")
    return thread


# ISSUE: Temporary file resource leak
def create_temp_file_with_leak():
    """
    Create a temporary file.
    Contains a resource leak because the file is not deleted.
    """
    # Resource leak: temporary file is created but not deleted
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(b"This is temporary data")
    temp_file_path = temp_file.name
    temp_file.close()
    
    # Missing os.unlink(temp_file_path)
    
    return temp_file_path


# ISSUE: Lock resource leak
def use_lock_with_leak(shared_resource):
    """
    Use a lock to protect a shared resource.
    Contains a resource leak because the lock is not released.
    """
    lock = threading.Lock()
    
    # Resource leak: lock is acquired but never released
    lock.acquire()
    
    # Modify shared resource
    shared_resource.append("Modified by thread")
    
    # Missing lock.release()
    
    return shared_resource


# ISSUE: Context manager not used for resource management
def process_multiple_files_with_leak(file_list):
    """
    Process multiple files.
    Contains resource leaks because files are not properly managed.
    """
    results = []
    
    for filename in file_list:
        # Resource leak: file is opened but not guaranteed to be closed
        file = open(filename, 'r')
        
        try:
            content = file.read()
            results.append(len(content))
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            # If an exception occurs, the file won't be closed
        
        # File should be closed in a finally block or using a context manager
    
    return results


# ISSUE: Resource leak in generator function
def read_large_file_with_leak(filename):
    """
    Generator to read a large file line by line.
    Contains a resource leak because the file is not closed when the generator is garbage collected.
    """
    # Resource leak: file might not be closed if the generator is not fully consumed
    file = open(filename, 'r')
    
    try:
        for line in file:
            yield line.strip()
    except Exception as e:
        print(f"Error reading file: {e}")
        # If an exception occurs, the file won't be closed
    
    # Missing finally block to close the file


# BETTER ALTERNATIVE: Proper resource management with context managers

def read_file_correctly(filename):
    """
    Read a file and return its contents using a context manager.
    """
    # Using 'with' statement ensures the file is closed properly
    with open(filename, 'r') as file:
        content = file.read()
    
    return content


def query_database_correctly(db_path, query):
    """
    Execute a query on a SQLite database using context managers.
    """
    # Using 'with' statement ensures the connection is closed properly
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
    
    return results


def process_data_correctly(input_file, output_file):
    """
    Process data from input file and write to output file with proper resource management.
    """
    try:
        with open(input_file, 'r') as input_handle:
            with open(output_file, 'w') as output_handle:
                for line in input_handle:
                    processed_line = line.strip().upper()
                    output_handle.write(processed_line + '\n')
    except Exception as e:
        print(f"Error processing files: {e}")
        return False
    
    return True


def create_thread_correctly():
    """
    Create a worker thread with proper joining.
    """
    def worker():
        """Worker function that simulates long-running task."""
        import time
        print("Worker thread starting")
        time.sleep(2)
        print("Worker thread finished")
    
    thread = threading.Thread(target=worker)
    thread.start()
    thread.join()  # Wait for the thread to complete
    
    print("Main thread continuing")
    return thread


def create_temp_file_correctly():
    """
    Create a temporary file with proper cleanup.
    """
    # Using context manager for temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(b"This is temporary data")
        temp_file_path = temp_file.name
        # File will be automatically deleted when the context manager exits
    
    return temp_file_path


def use_lock_correctly(shared_resource):
    """
    Use a lock to protect a shared resource with proper release.
    """
    lock = threading.Lock()
    
    # Using context manager for lock
    with lock:
        # Modify shared resource
        shared_resource.append("Modified by thread")
    
    return shared_resource


# Custom context manager for resource management
@contextmanager
def managed_resource(resource_name):
    """
    A context manager for generic resource management.
    """
    print(f"Acquiring {resource_name}")
    resource = {"name": resource_name, "state": "active"}
    
    try:
        yield resource
    finally:
        print(f"Releasing {resource_name}")
        resource["state"] = "released"


def use_managed_resource():
    """
    Use a custom context manager for resource management.
    """
    with managed_resource("database_connection") as conn:
        print(f"Using {conn['name']} in state {conn['state']}")
        # Use the resource...
    
    # Resource is automatically released when the context manager exits