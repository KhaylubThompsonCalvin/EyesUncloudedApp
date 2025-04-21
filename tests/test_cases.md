# CIS 234A: Real World Programming

# Project: Eyes Unclouded App – Sprint 3

# Name: Khaylub Thompson-Calvin

# Date: 04/19/2025

# Description:

# This test document provides terminal-based and web-based functional test cases

# for the Eyes Unclouded App. It includes Role-based onboarding, Class reveal logic,

# emotion log tracking, Oracle Archive input, and secure user session handling.

# Inspired by the teachings of Dr. Paul Ekman, Sherlock Holmes deduction,

# and strategic legacy systems.

# **********************************\*\*\***********************************

## Terminal-Based Test Suite

### Test Case 1: Project Folder & Virtual Environment

1. Open PowerShell.
2. Navigate to your project directory:
   ```
   cd .\Assignment1
   ```
3. Create and activate a virtual environment:
   ```
   python -m venv venv
   .\venv\Scripts\Activate
   ```

### Test Case 2: Install Dependencies

1. Run:
   ```
   pip install -r requirements.txt
   ```
2. Confirm installed packages with:
   ```
   pip list
   ```

### Test Case 3: Start Flask Application

1. Run the app:
   ```
   python app.py
   ```
2. Check output:
   - Should show `Running on http://127.0.0.1:7777/`

### Test Case 4: Role Registration Functionality

1. Visit: `http://127.0.0.1:7777/register`
2. Fill in user details and select a Role Type.
3. Click Register and check:
   - Success flash message
   - MongoDB stores role_type field

### Test Case 5: Login Verification

1. Send a POST request using curl:
   ```
   curl -X POST http://127.0.0.1:7777/login -H "Content-Type: application/json" -d "{\"email\":\"test@pcc.edu\",\"password\":\"pass123\"}"
   ```

### Test Case 6: Emotion Logging

1. In terminal, run:
   ```
   python src/utils/microexpression_decoder.py --log
   ```
2. Choose an emotion like `anger` and confirm it's logged to `logs/emotion_log.json`.

### Test Case 7: Emotion Summary Report

1. Run:
   ```
   python src/utils/microexpression_decoder.py --summary
   ```
2. Output should list:
   - Most common emotion
   - Total observations
   - First and last timestamps

### Test Case 8: Export Logs to CSV

1. Run:
   ```
   python src/utils/microexpression_decoder.py --export-csv
   ```
2. Check that `emotion_log_export.csv` is created in `logs/`.

## Web-Based Test Suite

### Test Case 9: Dashboard Access Post-Login

1. Visit: `/dashboard`
2. Verify:
   - Logged-in user name appears
   - Role Type and perception streak displayed

### Test Case 10: Notification System

1. Visit: `/notifications`
2. Submit a message
3. Check that it appears on `/notification-log`

### Test Case 11: Class Reveal Mechanism

1. Precondition: Log multiple emotions to simulate perception streak.
2. Visit: `/reveal`
3. Confirm:
   - Audio plays
   - Class is displayed on screen

### Test Case 12: Oracle Archive Upload

1. Visit: `/oracle`
2. Upload a `.txt` or `.pdf` file
3. Receive summary feedback

### Test Case 13: Mentor Insight for Role

1. Log in with a Role selected
2. Navigate to dashboard
3. Confirm:
   - Audio lesson plays
   - Message is specific to Role Type

### Test Case 14: Screenshot Documentation

1. Take screenshots of:
   - splash_screen.png
   - login_ui.png
   - dashboard_main.png
2. Store them in:
   ```
   docs/screenshots/
   ```

### Test Case 15: Static Audio File Check

1. Confirm the following files exist:
   ```
   static/audio/Role_Seeker.mp3
   static/audio/Role_Mentor.mp3
   ```
2. Ensure they play on the registration and dashboard pages.

### Test Case 16: MongoDB Index Check

1. In Mongo shell, run:
   ```
   db.subscribers.getIndexes()
   ```
2. Confirm email and username are indexed uniquely.

### Test Case 17: Session Protection

1. Try accessing `/dashboard` without logging in
2. System should redirect to `/login`

# End of Test Plan
