"""
CIS 234A: Real World Programming
Project: Eyes Unclouded App – Sprint 3
Author: Khaylub Thompson-Calvin
Date: 04/19/2025
Description:
This Python script runs documented test cases for core functionality in the Eyes Unclouded App.
It verifies input validation logic, emotion log structure, and symbolic perception thresholds.
Test functions are designed for manual or automated (Pytest) use.
"""

import sys
import os
from datetime import datetime

# Allow relative imports from /src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils.input_validation import (
    is_valid_email,
    is_strong_password,
    is_valid_username,
    is_valid_role_type
)

# ----------------------------------------------------------
# TEST GROUP 1: Input Validation (Registration + Login Forms)
# ----------------------------------------------------------

def test_valid_email_format():
    assert is_valid_email("user@example.com")
    assert not is_valid_email("invalid-email")
    print("[✓] Email format validation passed.")

def test_strong_password():
    assert is_strong_password("Secure123")
    assert not is_strong_password("weak")
    print("[✓] Password strength validation passed.")

def test_username_rules():
    assert is_valid_username("Khaylub123")
    assert not is_valid_username("!@#invalid")
    assert not is_valid_username("ab")  # too short
    print("[✓] Username validation passed.")

def test_role_type_values():
    assert is_valid_role_type("Seeker")
    assert not is_valid_role_type("Unknown")
    print("[✓] Role type validation passed.")

# ----------------------------------------------------------
# TEST GROUP 2: Symbolic App Logic
# ----------------------------------------------------------

def test_perception_score_threshold():
    perception_score = 11
    class_unlocked = perception_score >= 10
    assert class_unlocked is True
    print("[✓] Class unlock threshold logic passed.")

def test_emotion_log_structure():
    sample_log = {
        "emotion": "fear",
        "source": "upper_eyelid_raise",
        "timestamp": datetime.now().isoformat()
    }
    assert sample_log["emotion"] in [
        "anger", "sadness", "happiness", "fear",
        "surprise", "disgust", "contempt"
    ]
    assert "timestamp" in sample_log
    print("[✓] Emotion log entry structure passed.")

def test_timestamp_format():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    assert len(ts) == 19
    assert ts.count('-') == 2
    assert ts.count(':') == 2
    print("[✓] Timestamp format verified:", ts)

# ----------------------------------------------------------
# RUN ALL TESTS
# ----------------------------------------------------------

if __name__ == "__main__":
    print("Running Eyes Unclouded App – Documented Test Suite...\n")

    # Validation
    test_valid_email_format()
    test_strong_password()
    test_username_rules()
    test_role_type_values()

    # Symbolic logic
    test_perception_score_threshold()
    test_emotion_log_structure()
    test_timestamp_format()

    print("\nAll tests completed successfully.")
