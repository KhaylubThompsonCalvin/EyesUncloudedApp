# CIS234A: Real World Programming
# Project: Food Pantry Notification System – Sprint 1
# Author: Khaylub Thompson-Calvin
# Date: 4/14/2025
# Description:
# This file documents terminal-based test cases and functional checks
# for verifying Flask + MongoDB integration, endpoints, UI behavior,
# and secure registration/login system.
# ***********************************************************************

# Philosophy:
# Clean, modular, testable code for real-world systems.

# --------------------------------------------------------
# Test Case 1: Navigate to Project Directory
# --------------------------------------------------------
# Command:
# cd "E:\CloudData\Desktop\School Computer Inforrmation Systems\CIS234A_Real_World_Programming\Calendar_Weeks\Real World Programming Team Project\Assignment1>"
#  Verifies local folder structure and sprint repo setup.

# --------------------------------------------------------
# Test Case 2: Activate Virtual Environment
# --------------------------------------------------------
# Command:
# .\venv\Scripts\Activate
#  Check: Terminal prompt changes to (venv)
#  If venv doesn’t exist, run: python -m venv venv

# --------------------------------------------------------
# Test Case 3: Install Requirements
# --------------------------------------------------------
# Command:
# pip install -r requirements.txt
#   Check:
# - Flask
# - flask_pymongo
# - dnspython
# Confirm with: pip list

# --------------------------------------------------------
# Test Case 4: Run Flask App
# --------------------------------------------------------
# Command:
# python app.py
#  Check:
# * Running on http://localhost:5001/ or http://localhost:5001/
# Browser loads default route or HTML page

# --------------------------------------------------------
# Test Case 5: Registration Endpoint (POST)
# --------------------------------------------------------
# Command:
# curl -X POST http://localhost:3000/register -H "Content-Type: application/json" \
# -d "{\"name\": \"Khaylub\", \"username\": \"Khaylub\", \"email\": \"Khaylub.thompsoncalvin@pcc.edu\", \"password\": \"pass123\", \"confirm_password\": \"pass123\"}"
# Check: {"message": "Registration successful"}

# --------------------------------------------------------
# Test Case 6: Login Endpoint (POST)
# --------------------------------------------------------
# Command:
# curl -X POST http://localhost:3000/login -H "Content-Type: application/json" \
# -d "{\"email\": \"Khaylub.thompsoncalvin@pcc.edu\", \"password\": \"pass123\"}"
# Check: {"message": "Login successful"}
# Try incorrect password:
# {"error": "Invalid credentials"}

# --------------------------------------------------------
# Test Case 7: MongoDB Validation (Duplicates)
# --------------------------------------------------------
# Command: (register again with same email)
# Check: {"error": "Email or username already exists"}

# --------------------------------------------------------
# Test Case 8: Notifications Blueprint (GET)
# --------------------------------------------------------
# Command:
# curl http://localhost:5001/notifications/test
# Check: {"message": "Notifications module is working"}

# --------------------------------------------------------
# Test Case 9: HTML Form Rendering (GET)
# --------------------------------------------------------
# URLS:
# http://localhost:5001/register
# http://localhost:5001/login
# Check: Pages load, form fields appear

# --------------------------------------------------------
# Test Case 10: PowerShell Invoke-RestMethod (Optional)
# --------------------------------------------------------
# Command:
# Invoke-RestMethod -Uri "http://localhost:5001/login" -Method Post -Body @{
#     email = "Khaylub.thompsoncalvin@pcc.edu"
#     password = "pass123"
# } -ContentType "application/json"
# Check: Login successful response

# --------------------------------------------------------
# Test Case 11: Hashed Passwords
# --------------------------------------------------------
# Confirm that passwords in MongoDB begin with $pbkdf2-sha256$
# Shows password hashing using Werkzeug is active and plaintext is avoided
