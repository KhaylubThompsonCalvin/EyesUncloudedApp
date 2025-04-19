# CIS234A: Real World Programming

# Project: Food Pantry Notification System – Sprint 1

# Name: Khaylub Thompson-Calvin

# Date: 4/14/2025

# Description: Implementation details of the backend structure and MVC design of the system.

# Source: Assignment A1 Specification, PCC CIS234A Course Materials

# ********************************************\*\*\*\*********************************************

## Components

- Flask handles routing and web server
- MongoDB Atlas stores users and notifications
- Jinja Templates render dynamic views
- Flask-Session manages login sessions
- Werkzeug hashes passwords securely

## Folder Structure

- controllers/ – Python route logic
- models/ – MongoDB schemas (optional)
- static/ – CSS and JavaScript
- src/views/templates/ – HTML templates
- project-backlog/ – Agile planning docs
- tests/ – Functional testing scripts
- documentation/ – Notes, screenshots, flow diagrams

## Security Measures

- Passwords are hashed with Werkzeug before database storage
- User sessions only store non-sensitive identifiers (user_id)
- Login and register routes sanitize inputs and validate uniqueness
