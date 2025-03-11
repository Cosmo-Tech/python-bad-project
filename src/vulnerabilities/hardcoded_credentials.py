"""
This module contains examples of hardcoded credentials.
Hardcoded credentials are a security vulnerability because they can be extracted from source code,
binaries, or memory dumps, leading to unauthorized access.
"""

import base64
import os
import requests
from typing import Dict, Any, Optional, List


# ISSUE: Hardcoded database credentials
def connect_to_database_vulnerable() -> Dict[str, Any]:
    """
    Connect to a database using hardcoded credentials.
    """
    # Vulnerable: Hardcoded database credentials
    host = "db.example.com"
    username = "admin"
    password = "s3cr3tP@ssw0rd"  # Hardcoded password
    database = "customer_data"
    
    connection_string = f"postgresql://{username}:{password}@{host}/{database}"
    
    print(f"Connecting to database: {host}/{database}")
    # In a real implementation, this would establish a database connection
    
    return {
        "status": "connected",
        "host": host,
        "database": database,
        "user": username
    }


# ISSUE: Hardcoded API key
def make_api_request_vulnerable(endpoint: str) -> Dict[str, Any]:
    """
    Make an API request using a hardcoded API key.
    """
    # Vulnerable: Hardcoded API key
    api_key = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p"  # Hardcoded API key
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    url = f"https://api.example.com/{endpoint}"
    
    try:
        response = requests.get(url, headers=headers)
        return {
            "status_code": response.status_code,
            "data": response.json() if response.status_code == 200 else None
        }
    except Exception as e:
        print(f"API request failed: {e}")
        return {"status_code": 500, "data": None}


# ISSUE: Hardcoded AWS credentials
def upload_to_s3_vulnerable(file_path: str, bucket_name: str) -> bool:
    """
    Upload a file to an S3 bucket using hardcoded AWS credentials.
    """
    # Vulnerable: Hardcoded AWS credentials
    aws_access_key = "AKIAIOSFODNN7EXAMPLE"  # Hardcoded AWS access key
    aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # Hardcoded AWS secret key
    
    # In a real implementation, this would use boto3 to upload the file
    print(f"Uploading {file_path} to S3 bucket {bucket_name}")
    print(f"Using AWS credentials: {aws_access_key[:5]}...{aws_access_key[-5:]}")
    
    # Simulate upload
    if os.path.exists(file_path):
        return True
    else:
        print(f"File not found: {file_path}")
        return False


# ISSUE: Hardcoded encryption key
def encrypt_data_vulnerable(data: str) -> str:
    """
    Encrypt data using a hardcoded encryption key.
    """
    # Vulnerable: Hardcoded encryption key
    encryption_key = b"ThisIsAHardcodedEncryptionKey123"  # Hardcoded encryption key
    
    # Simple XOR encryption for demonstration (also insecure)
    encrypted = bytearray()
    for i, char in enumerate(data.encode()):
        encrypted.append(char ^ encryption_key[i % len(encryption_key)])
    
    return base64.b64encode(encrypted).decode()


# ISSUE: Hardcoded JWT secret
def generate_jwt_token_vulnerable(user_id: str, role: str) -> str:
    """
    Generate a JWT token using a hardcoded secret.
    """
    # Vulnerable: Hardcoded JWT secret
    jwt_secret = "jwt_super_secret_key_do_not_share"  # Hardcoded JWT secret
    
    # In a real implementation, this would use a JWT library
    # This is a simplified demonstration
    
    # Create a simple header and payload
    header = base64.b64encode(b'{"alg":"HS256","typ":"JWT"}').decode()
    payload = base64.b64encode(f'{{"user_id":"{user_id}","role":"{role}"}}'.encode()).decode()
    
    # Create a simple signature (not a real JWT implementation)
    signature = base64.b64encode(
        f"{header}.{payload}.{jwt_secret}".encode()
    ).decode()
    
    return f"{header}.{payload}.{signature}"


# ISSUE: Hardcoded OAuth client secret
def get_oauth_token_vulnerable(username: str, password: str) -> Dict[str, Any]:
    """
    Get an OAuth token using hardcoded client credentials.
    """
    # Vulnerable: Hardcoded OAuth client credentials
    client_id = "oauth_client_id"  # Hardcoded client ID
    client_secret = "oauth_client_secret_value"  # Hardcoded client secret
    
    auth_url = "https://auth.example.com/oauth/token"
    
    payload = {
        "grant_type": "password",
        "username": username,
        "password": password,
        "client_id": client_id,
        "client_secret": client_secret
    }
    
    try:
        response = requests.post(auth_url, data=payload)
        return response.json() if response.status_code == 200 else {"error": "Authentication failed"}
    except Exception as e:
        print(f"OAuth request failed: {e}")
        return {"error": str(e)}


# ISSUE: Hardcoded SSH private key
def connect_to_server_vulnerable(server_ip: str) -> bool:
    """
    Connect to a server using a hardcoded SSH private key.
    """
    # Vulnerable: Hardcoded SSH private key
    ssh_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1JrJANAAq/vd4IQvjsYOTVRKnRKDHJvzQIyB0jIJxKLxWLEE
pqQz+frmu7qEZ9xM7+3hutQmQa0jgAOdCHPQmfJ4D1hXg4XxhjC+ZF8u9WlhVERP
2nxrHbXs8tLGEXwXjZ3uRk8c9HW5GhYZ3W7ij8mLYuGUNKZz8ROvGhuSIqzm1fcP
E9Jn9d7CXbPnhXUxkR/cCUXrKXZ5BGCEEw5yLLHbDw4y7zNWoLxPFGKPw+Lnr4bA
dJ8dBTpwXSDYLaEzr9Y5QLiEkW859jSDH1LgTYojLIki0vLNhcTrJGVv8eJEYQXN
ZYfJ5E6vTenJ7Rh5JYIiqNJbLI6Ug/r8QwIDAQABAoIBAQCyX5w2E9aL+ZDR8Jm5
NKYkJPOq/yP9i9+qr4QwHs9x3sZeArRQFtilHJFrCHOnUaXZ6Xoe+jXVm+Q+8Eal
PPDrRGaRtC91uA9TnORgZDEkKdXWp6K9HJnwjJJaHJZPQwzWvDgNOKKawlXyWEXs
0pY6nKxSCVgJZ9bZFU7MQBnQFhcHNMnRzCr9Jb/eXNFZ4iOiVHUQvvCrWKOYCZFZ
LuEPqzCRWYnwUPJnE+o0jFsQCQjZXu8O0V3IHNAUHVnJ4AEjwRHGXnFR0+nVT9Oa
dZstv8GJ28Wa+MXtGbhY/iFG5JRYVCpVYLTVjlKL9RwLM5U5KO5EfFQy0M/Gw7YY
RknhAoGBAP4tdWlZ8UTT9OUUNkkOQjHsm8xjLWsf8qCZlYwUkrZhCJ8YxTQi9Pqf
5eFHQCuD5gKj+nOBwXjxXBUJYP8W0R1P0e4YK3vVgOxQJIgKYu0JqJcnuPsEZ8Gu
NtBc0BlRiVYNv9CpC/6Zt/1iIy8BHVvMYzXpOYKbSKSNzrWa4cMJAoGBANYrfGvz
l7TMNKj5JwDNJ8mwCCJTFZbSUjmbtCMn/Nj4K7nH1hP6aNb9MEIYQjKQeWGVcTFB
bLzQ0UOa7kZUuPDFG4+TRvz6sVZjYzBX0J4/4gle2LzQCt+/m9fPJEQw9j6v4x9B
nANcPvVR2ReCZzGSBGJmCXnHDANaTXdLLAhLAoGAJQMOVuxYOSdnZ9UZ0yjjjZT8
sFxJQwXwqSTzwi2TRUcC5+OvQK3bKVQoL8ggkX8IOK2e3K/omQkUSfCdJK5iBHnP
SUuMCTNmUzB7UrQECJCRGJvJYA8K7fPJxfJkWV5yPYEyKMmKKXEZKZKjKEfDNfmF
aTuLE4FNnzXjJMJe3kECgYEAqghDDsIXljOvRToKSbVCcMc4iYHkGqQB5TRPUbS6
LE2TvHI0hlvX7xzIYFXvlkDzliRQlkBLUQfSHDzPWAcTQ1OZUF1XOjgibCb6kBkj
oPSRXJDYCUXAYgSVQxbSdUBwGKpQNo6wIJQyK+vVPcMgr4Pmf+8crxEkwFa6rNY5
D+sCgYAHJWW7mAIjXJETGQG5HXwYFAKGnH2XQDQvBLHiCF7Hl+QnUTTvSHvMkIeO
LfUmLwh/7XT9ZJ7Jop3R5QsQcBXoSVR/f7/VKpFQF1rGYCQXJVmNEJkEYlGQzrXZ
K5jQCdpVmhB9JYP3hCTdZbCIKwpqkHKPylJQBYI/0tHRWEiWvg==
-----END RSA PRIVATE KEY-----"""  # Hardcoded SSH private key
    
    # In a real implementation, this would use paramiko or a similar library
    # to establish an SSH connection
    
    print(f"Connecting to server: {server_ip}")
    print("Using hardcoded SSH private key")
    
    # Simulate connection
    return True


# ISSUE: Hardcoded basic authentication
def access_protected_resource_vulnerable(resource_path: str) -> Dict[str, Any]:
    """
    Access a protected resource using hardcoded basic authentication credentials.
    """
    # Vulnerable: Hardcoded basic authentication credentials
    username = "admin"
    password = "admin123"  # Hardcoded password
    
    # Create basic auth header
    auth_string = f"{username}:{password}"
    auth_base64 = base64.b64encode(auth_string.encode()).decode()
    
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/json"
    }
    
    url = f"https://api.example.com/{resource_path}"
    
    try:
        response = requests.get(url, headers=headers)
        return {
            "status_code": response.status_code,
            "data": response.json() if response.status_code == 200 else None
        }
    except Exception as e:
        print(f"Request failed: {e}")
        return {"status_code": 500, "data": None}


# ISSUE: Hardcoded SMTP credentials
def send_email_vulnerable(to_email: str, subject: str, body: str) -> bool:
    """
    Send an email using hardcoded SMTP credentials.
    """
    # Vulnerable: Hardcoded SMTP credentials
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "notifications@example.com"
    smtp_password = "emailP@ssw0rd"  # Hardcoded password
    
    # In a real implementation, this would use smtplib to send an email
    
    print(f"Sending email to: {to_email}")
    print(f"Subject: {subject}")
    print(f"Using SMTP server: {smtp_server}:{smtp_port}")
    print(f"Using SMTP credentials: {smtp_username}")
    
    # Simulate sending email
    return True


# BETTER ALTERNATIVE: Using environment variables

def connect_to_database_secure() -> Dict[str, Any]:
    """
    Connect to a database using credentials from environment variables.
    """
    # Secure: Using environment variables
    host = os.environ.get("DB_HOST", "localhost")
    username = os.environ.get("DB_USERNAME")
    password = os.environ.get("DB_PASSWORD")
    database = os.environ.get("DB_NAME")
    
    if not all([username, password, database]):
        raise ValueError("Database credentials not properly configured in environment variables")
    
    connection_string = f"postgresql://{username}:{password}@{host}/{database}"
    
    print(f"Connecting to database: {host}/{database}")
    # In a real implementation, this would establish a database connection
    
    return {
        "status": "connected",
        "host": host,
        "database": database,
        "user": username
    }


# BETTER ALTERNATIVE: Using a configuration file

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a file.
    """
    import json
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return {}


def make_api_request_secure(endpoint: str, config_path: str) -> Dict[str, Any]:
    """
    Make an API request using credentials from a configuration file.
    """
    config = load_config(config_path)
    api_key = config.get("api_key")
    
    if not api_key:
        raise ValueError("API key not found in configuration")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    url = f"https://api.example.com/{endpoint}"
    
    try:
        response = requests.get(url, headers=headers)
        return {
            "status_code": response.status_code,
            "data": response.json() if response.status_code == 200 else None
        }
    except Exception as e:
        print(f"API request failed: {e}")
        return {"status_code": 500, "data": None}


# BETTER ALTERNATIVE: Using a secrets manager

def get_secret(secret_name: str) -> Optional[str]:
    """
    Get a secret from a secrets manager.
    
    In a real implementation, this would use a service like AWS Secrets Manager,
    HashiCorp Vault, or a similar solution.
    """
    # Simplified demonstration
    # In a real implementation, this would call a secrets manager API
    
    print(f"Retrieving secret: {secret_name}")
    
    # Simulate retrieving a secret
    if secret_name == "db_password":
        return "retrieved_password_from_secrets_manager"
    elif secret_name == "api_key":
        return "retrieved_api_key_from_secrets_manager"
    else:
        print(f"Secret not found: {secret_name}")
        return None


def encrypt_data_secure(data: str) -> str:
    """
    Encrypt data using a key from a secrets manager.
    """
    encryption_key_b64 = get_secret("encryption_key")
    
    if not encryption_key_b64:
        raise ValueError("Encryption key not found in secrets manager")
    
    encryption_key = base64.b64decode(encryption_key_b64)
    
    # Simple XOR encryption for demonstration (also insecure)
    encrypted = bytearray()
    for i, char in enumerate(data.encode()):
        encrypted.append(char ^ encryption_key[i % len(encryption_key)])
    
    return base64.b64encode(encrypted).decode()


# BETTER ALTERNATIVE: Using instance metadata for cloud credentials

def get_aws_credentials_from_metadata() -> Dict[str, str]:
    """
    Get AWS credentials from instance metadata.
    
    This is a simplified demonstration. In a real implementation,
    you would use the AWS SDK which handles this automatically.
    """
    # Simplified demonstration
    # In a real implementation on AWS, you would use:
    # import boto3
    # session = boto3.Session()
    # credentials = session.get_credentials()
    
    print("Retrieving AWS credentials from instance metadata")
    
    # Simulate retrieving credentials
    return {
        "access_key": "retrieved_access_key_from_metadata",
        "secret_key": "retrieved_secret_key_from_metadata",
        "token": "retrieved_session_token_from_metadata"
    }


def upload_to_s3_secure(file_path: str, bucket_name: str) -> bool:
    """
    Upload a file to an S3 bucket using credentials from instance metadata.
    """
    # In a real implementation, you would use:
    # import boto3
    # s3 = boto3.client('s3')
    # s3.upload_file(file_path, bucket_name, os.path.basename(file_path))
    
    print(f"Uploading {file_path} to S3 bucket {bucket_name}")
    print("Using AWS credentials from instance metadata")
    
    # Simulate upload
    if os.path.exists(file_path):
        return True
    else:
        print(f"File not found: {file_path}")
        return False