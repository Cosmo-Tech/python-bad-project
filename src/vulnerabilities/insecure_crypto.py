"""
This module contains examples of insecure cryptographic implementations.
These include weak algorithms, hardcoded keys, improper key management, and other cryptographic vulnerabilities.
"""

import base64
import hashlib
import os
import random
import string
import time
from typing import Dict, Tuple, Optional

# For demonstration only - these would normally be imported
# import cryptography
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.primitives import hashes, padding
# from cryptography.hazmat.backends import default_backend


# ISSUE: Using weak hash algorithms (MD5)
def hash_password_md5(password: str) -> str:
    """
    Hash a password using MD5 (insecure).
    MD5 is cryptographically broken and unsuitable for further use.
    """
    # Vulnerable: Using MD5 for password hashing
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    return md5_hash


# ISSUE: Using weak hash algorithms (SHA1)
def hash_password_sha1(password: str) -> str:
    """
    Hash a password using SHA1 (insecure).
    SHA1 is cryptographically broken and unsuitable for further use.
    """
    # Vulnerable: Using SHA1 for password hashing
    sha1_hash = hashlib.sha1(password.encode()).hexdigest()
    return sha1_hash


# ISSUE: Hashing without salt
def hash_password_without_salt(password: str) -> str:
    """
    Hash a password without using a salt (insecure).
    This makes the hash vulnerable to rainbow table attacks.
    """
    # Vulnerable: Hashing without salt
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    return sha256_hash


# ISSUE: Using a hardcoded salt
def hash_password_with_hardcoded_salt(password: str) -> str:
    """
    Hash a password with a hardcoded salt (insecure).
    Hardcoded salts defeat the purpose of salting.
    """
    # Vulnerable: Hardcoded salt
    salt = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    salted_password = password + salt
    sha256_hash = hashlib.sha256(salted_password.encode()).hexdigest()
    return sha256_hash


# ISSUE: Insufficient iterations for password hashing
def hash_password_insufficient_iterations(password: str, salt: str) -> str:
    """
    Hash a password with insufficient iterations (insecure).
    Too few iterations make brute-force attacks easier.
    """
    # Vulnerable: Too few iterations (should be at least 100,000 for PBKDF2)
    iterations = 100
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations)
    return base64.b64encode(dk).decode()


# ISSUE: Hardcoded encryption key
def encrypt_data_with_hardcoded_key(data: str) -> str:
    """
    Encrypt data with a hardcoded key (insecure).
    Hardcoded keys can be extracted from the source code.
    """
    # Vulnerable: Hardcoded encryption key
    key = b"ThisIsAHardcodedKeyForEncryption!"
    
    # Simple XOR encryption for demonstration (also insecure)
    encrypted = bytearray()
    for i, char in enumerate(data.encode()):
        encrypted.append(char ^ key[i % len(key)])
    
    return base64.b64encode(encrypted).decode()


# ISSUE: Using a predictable IV (Initialization Vector)
def encrypt_with_predictable_iv(data: str, key: bytes) -> str:
    """
    Encrypt data with a predictable IV (insecure).
    IVs should be random and unpredictable.
    """
    # Vulnerable: Predictable IV
    iv = b"\x00" * 16  # All zeros
    
    # Simplified encryption for demonstration
    # In a real implementation, this would use a proper cipher mode
    encrypted = bytearray()
    for i, char in enumerate(data.encode()):
        encrypted.append(char ^ iv[i % len(iv)] ^ key[i % len(key)])
    
    return base64.b64encode(encrypted).decode()


# ISSUE: Using ECB mode for encryption
def encrypt_with_ecb_mode(data: str, key: bytes) -> bytes:
    """
    Encrypt data using ECB mode (insecure).
    ECB mode does not provide semantic security.
    
    Note: This is a simplified demonstration. In a real implementation,
    you would use the cryptography library.
    """
    # Vulnerable: Using ECB mode
    # This is a simplified demonstration of ECB mode's weakness
    
    # Pad the data to be a multiple of 16 bytes
    padded_data = data.encode()
    if len(padded_data) % 16 != 0:
        padded_data += b"\x00" * (16 - (len(padded_data) % 16))
    
    # Simplified ECB encryption (for demonstration only)
    encrypted = bytearray()
    for i in range(0, len(padded_data), 16):
        block = padded_data[i:i+16]
        # In ECB, identical plaintext blocks encrypt to identical ciphertext blocks
        # This is a major weakness
        encrypted_block = bytes([b ^ k for b, k in zip(block, key[:16])])
        encrypted.extend(encrypted_block)
    
    return encrypted


# ISSUE: Weak random number generation
def generate_weak_random_token(length: int = 32) -> str:
    """
    Generate a token using weak random number generation (insecure).
    """
    # Vulnerable: Using random instead of secrets
    chars = string.ascii_letters + string.digits
    token = ''.join(random.choice(chars) for _ in range(length))
    return token


# ISSUE: Time-based token generation
def generate_time_based_token() -> str:
    """
    Generate a token based on the current time (insecure).
    Time-based tokens are predictable.
    """
    # Vulnerable: Using time as a source of randomness
    timestamp = str(time.time())
    token = hashlib.sha256(timestamp.encode()).hexdigest()
    return token


# ISSUE: Insecure password verification (timing attack vulnerability)
def verify_password_insecure(stored_hash: str, provided_password: str) -> bool:
    """
    Verify a password in a way that's vulnerable to timing attacks.
    """
    # Vulnerable: Timing attack possible
    calculated_hash = hashlib.sha256(provided_password.encode()).hexdigest()
    return calculated_hash == stored_hash


# ISSUE: Using a non-cryptographic hash function
def hash_data_non_crypto(data: str) -> int:
    """
    Hash data using a non-cryptographic hash function (insecure for security purposes).
    """
    # Vulnerable: Using a non-cryptographic hash function
    hash_value = 0
    for char in data:
        hash_value = (hash_value * 31 + ord(char)) & 0xFFFFFFFF
    return hash_value


# ISSUE: Implementing a custom encryption algorithm
def custom_encryption_algorithm(data: str, key: str) -> str:
    """
    Implement a custom encryption algorithm (insecure).
    Custom cryptographic algorithms are likely to have vulnerabilities.
    """
    # Vulnerable: Custom encryption algorithm
    key_bytes = key.encode()
    data_bytes = data.encode()
    encrypted = bytearray()
    
    for i, byte in enumerate(data_bytes):
        key_byte = key_bytes[i % len(key_bytes)]
        # Custom algorithm: rotate bits and XOR with key
        rotated = ((byte << 3) | (byte >> 5)) & 0xFF
        encrypted_byte = rotated ^ key_byte
        encrypted.append(encrypted_byte)
    
    return base64.b64encode(encrypted).decode()


# BETTER ALTERNATIVE: Secure password hashing with Argon2

def hash_password_secure(password: str) -> Dict[str, str]:
    """
    Hash a password securely using Argon2id.
    
    Note: This is a simplified demonstration. In a real implementation,
    you would use the argon2-cffi library.
    """
    # Generate a random salt
    salt = os.urandom(16)
    salt_b64 = base64.b64encode(salt).decode()
    
    # In a real implementation, you would use:
    # import argon2
    # ph = argon2.PasswordHasher()
    # hash = ph.hash(password)
    
    # Simplified for demonstration
    # Pretend we're using Argon2id with secure parameters
    hash_b64 = base64.b64encode(
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    ).decode()
    
    return {
        "algorithm": "argon2id",
        "salt": salt_b64,
        "hash": hash_b64,
        "parameters": {
            "memory_cost": 65536,  # 64 MB
            "time_cost": 3,        # 3 iterations
            "parallelism": 4       # 4 threads
        }
    }


def verify_password_secure(stored_password_data: Dict[str, str], provided_password: str) -> bool:
    """
    Verify a password securely against a stored hash.
    
    Note: This is a simplified demonstration. In a real implementation,
    you would use the argon2-cffi library.
    """
    # In a real implementation, you would use:
    # import argon2
    # ph = argon2.PasswordHasher()
    # try:
    #     ph.verify(stored_password_data["hash"], provided_password)
    #     return True
    # except argon2.exceptions.VerifyMismatchError:
    #     return False
    
    # Simplified for demonstration
    salt = base64.b64decode(stored_password_data["salt"])
    stored_hash = stored_password_data["hash"]
    
    # Calculate hash of provided password
    calculated_hash = base64.b64encode(
        hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, 100000)
    ).decode()
    
    # Constant-time comparison to prevent timing attacks
    return constant_time_compare(stored_hash, calculated_hash)


def constant_time_compare(a: str, b: str) -> bool:
    """
    Compare two strings in constant time to prevent timing attacks.
    """
    if len(a) != len(b):
        return False
    
    result = 0
    for x, y in zip(a, b):
        result |= ord(x) ^ ord(y)
    
    return result == 0


# BETTER ALTERNATIVE: Secure encryption with AES-GCM

def encrypt_data_secure(data: str, key: Optional[bytes] = None) -> Dict[str, str]:
    """
    Encrypt data securely using AES-GCM.
    
    Note: This is a simplified demonstration. In a real implementation,
    you would use the cryptography library.
    """
    # Generate a random key if none is provided
    if key is None:
        key = os.urandom(32)  # 256-bit key
    
    # Generate a random nonce/IV
    nonce = os.urandom(12)  # 96-bit nonce is recommended for AES-GCM
    
    # In a real implementation, you would use:
    # from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    # aesgcm = AESGCM(key)
    # ciphertext = aesgcm.encrypt(nonce, data.encode(), None)
    
    # Simplified for demonstration
    # Pretend we're using AES-GCM
    ciphertext = b"encrypted_data_placeholder"
    
    return {
        "algorithm": "AES-GCM",
        "key": base64.b64encode(key).decode(),
        "nonce": base64.b64encode(nonce).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode()
    }


def decrypt_data_secure(encrypted_data: Dict[str, str], key: bytes) -> str:
    """
    Decrypt data that was encrypted with AES-GCM.
    
    Note: This is a simplified demonstration. In a real implementation,
    you would use the cryptography library.
    """
    # In a real implementation, you would use:
    # from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    # aesgcm = AESGCM(key)
    # nonce = base64.b64decode(encrypted_data["nonce"])
    # ciphertext = base64.b64decode(encrypted_data["ciphertext"])
    # plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    # return plaintext.decode()
    
    # Simplified for demonstration
    return "decrypted_data_placeholder"


# BETTER ALTERNATIVE: Secure random token generation

def generate_secure_token(length: int = 32) -> str:
    """
    Generate a cryptographically secure random token.
    """
    import secrets
    
    # Use secrets module for cryptographically strong random numbers
    token_bytes = secrets.token_bytes(length)
    return base64.urlsafe_b64encode(token_bytes).decode().rstrip('=')


# BETTER ALTERNATIVE: Secure key derivation from a password

def derive_key_from_password(password: str, salt: Optional[bytes] = None) -> Tuple[bytes, bytes]:
    """
    Derive a cryptographic key from a password using PBKDF2.
    """
    if salt is None:
        salt = os.urandom(16)
    
    # Use a high number of iterations
    iterations = 100000
    
    # Derive a 256-bit key
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations)
    
    return key, salt