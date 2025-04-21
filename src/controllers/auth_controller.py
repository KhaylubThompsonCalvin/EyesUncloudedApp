# ==============================================================================
# File: src/controllers/auth_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Role-Driven Identity Engine
# Author: Khaylub Thompson-Calvin
# Date: 04/17/2025
# ==============================================================================
# Description:
#   Manages user lifecycle functions including:
#     • Registration: builds a legacy profile with symbolic Role Type.
#     • Login: authenticates and stores role-based session state.
#     • Logout: clears session and exits system.
#     • Dashboard: renders core hub of self-reflection and strategic tools.
# ==============================================================================

import os
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps

from .database import get_user_profiles
from src.controllers.role_controller import ROLE_AUDIO  # Maps symbolic roles → audio onboarding

auth_bp = Blueprint('auth', __name__)

# -------------------------------------------------------------------
# Route Guard for Protected Routes
# -------------------------------------------------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Login required.", "warning")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

# -------------------------------------------------------------------
# /register – Symbolic Identity Creation
# -------------------------------------------------------------------
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        if data['password'] != data['confirmPassword']:
            flash("Passwords do not match.", "danger")
            return redirect(url_for('auth.register'))

        user = {
            "fullName":          data['fullname'],
            "username":          data['username'],
            "email":             data['email'],
            "password":          generate_password_hash(data['password']),
            "role_type":         data.get('role_type', 'Seeker'),
            "learning_level":    int(data.get('learning_level', 1)),
            "perception_score":  0,
            "virtue_affinity":   {},
            "created_at":        datetime.utcnow()
        }

        try:
            get_user_profiles().insert_one(user)
            print("[✓] Registration successful:", user["username"])
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('auth.login'))
        except Exception as e:
            print("[×] Registration error:", str(e))
            flash(f"Registration failed: {e}", "danger")
            return redirect(url_for('auth.register'))

    roles = list(ROLE_AUDIO.keys())
    overview_audio = 'Role_Overview.mp3'
    return render_template('register.html', roles=roles, overview_audio=overview_audio)

# -------------------------------------------------------------------
# /login – Identity Verification
# -------------------------------------------------------------------
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        identifier = data['identifier']
        password = data['password']

        print(f"[DEBUG] Login attempt for: {identifier}")

        user = get_user_profiles().find_one({
            "$or": [
                {"username": identifier},
                {"email": identifier}
            ]
        })

        if user:
            print("[DEBUG] User found in DB:", user["username"])
        else:
            print("[DEBUG] No user matched the identifier.")

        if user and check_password_hash(user['password'], password):
            print("[✓] Password verified for:", user["username"])
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            session['role_type'] = user.get('role_type', 'Seeker')
            flash("Login successful!", "success")
            return redirect(url_for('auth.dashboard'))

        flash("Invalid credentials.", "danger")
        print("[×] Login failed: Invalid credentials")

    return render_template('login.html')

# -------------------------------------------------------------------
# /dashboard – Strategic Hub
# -------------------------------------------------------------------
@auth_bp.route('/dashboard')
@login_required
def dashboard():
    chart_path = os.path.join("src", "views", "static", "images", "chart.png")
    chart_exists = os.path.exists(chart_path)
    return render_template(
        'dashboard.html',
        username=session.get('username'),
        chart_exists=chart_exists
    )

# -------------------------------------------------------------------
# /logout – Session Reset
# -------------------------------------------------------------------
@auth_bp.route('/logout')
@login_required
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('auth.login'))

# -------------------------------------------------------------------
# /debug-user – Diagnostic Route to Verify DB Access
# -------------------------------------------------------------------
@auth_bp.route('/debug-user')
def debug_user():
    user = get_user_profiles().find_one({"username": "HEWHOATETHESUN"})
    if user:
        return f"[✓] Found user: {user['username']}<br>Password: {user['password']}"
    return "[×] User not found in current database."
