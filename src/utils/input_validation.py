"""
input_validation.py

Author: Khaylub Thompson-Calvin
Date: 04/19/2025
Description:
This module provides reusable input validation functions for form fields, 
registration, login, and system inputs in the Eyes Unclouded App.
"""

import re

def is_valid_email(email: str) -> bool:
    """Check if the email has a valid format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return re.match(pattern, email) is not None

def is_strong_password(password: str) -> bool:
    """Validate password strength (8+ chars, 1 number, 1 uppercase)."""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    return True

def is_valid_username(username: str) -> bool:
    """Check if the username is alphanumeric and 3-20 chars long."""
    return username.isalnum() and (3 <= len(username) <= 20)

def is_valid_role_type(role: str) -> bool:
    """Ensure role type is one of the predefined values."""
    valid_roles = ['Seeker', 'Strategist', 'Mentor', 'Cipher', 'Observer', 'Warden']
    return role in valid_roles



