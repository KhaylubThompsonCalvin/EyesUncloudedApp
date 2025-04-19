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
#
#   Role Type logic connects to audio onboarding and future dashboard divergence.
#   Session variables (`user_id`, `username`, `role_type`) act as the symbolic keys
#   for unlocking perception-based features throughout the system.
# ==============================================================================

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps

from .database import get_user_profiles
from src.controllers.role_controller import ROLE_AUDIO  # Maps symbolic roles → audio onboarding

# ------------------------------------------------------------------------------
# Blueprint Setup
# ------------------------------------------------------------------------------
auth_bp = Blueprint('auth', __name__)

# ------------------------------------------------------------------------------
# Utility: Route Guard
# ------------------------------------------------------------------------------
def login_required(f):
    """
    Wraps any route that requires authentication.
    If user is not logged in, redirect to the login page with warning.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Login required.", "warning")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

# ------------------------------------------------------------------------------
# Route: /register – Create User Profile + Role Selection
# ------------------------------------------------------------------------------
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    GET: Display registration form with Role Type dropdown and overview audio.
    POST: Validate form input, hash password, create new user document,
          and redirect to login for onboarding.
    """
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
            "virtue_affinity":   {},  # Will evolve through usage
            "created_at":        datetime.utcnow()
        }

        try:
            get_user_profiles().insert_one(user)
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f"Registration failed: {e}", "danger")
            return redirect(url_for('auth.register'))

    # GET: inject symbolic role options and audio metadata
    roles = list(ROLE_AUDIO.keys())
    overview_audio = 'Role_Overview.mp3'
    return render_template('register.html',
                           roles=roles,
                           overview_audio=overview_audio)

# ------------------------------------------------------------------------------
# Route: /login – Authenticate User & Store Session
# ------------------------------------------------------------------------------
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    GET: Display login form.
    POST: Authenticate using email or username, store session data including:
          user_id, username, and role_type.
    """
    if request.method == 'POST':
        data = request.form
        user = get_user_profiles().find_one({
            "$or": [
                {"username": data['identifier']},
                {"email": data['identifier']}
            ]
        })
        if user and check_password_hash(user['password'], data['password']):
            session['user_id']    = str(user['_id'])
            session['username']   = user['username']
            session['role_type']  = user.get('role_type', 'Seeker')  # fallback
            flash("Login successful!", "success")
            return redirect(url_for('auth.dashboard'))

        flash("Invalid credentials.", "danger")

    return render_template('login.html')

# ------------------------------------------------------------------------------
# Route: /dashboard – Symbolic Core of the System
# ------------------------------------------------------------------------------
@auth_bp.route('/dashboard')
@login_required
def dashboard():
    """
    Render the user dashboard.
    This hub evolves as perception logs and Role/Class mechanics mature.
    """
    return render_template('dashboard.html', username=session.get('username'))

# ------------------------------------------------------------------------------
# Route: /logout – Exit the Behavioral Engine
# ------------------------------------------------------------------------------
@auth_bp.route('/logout')
@login_required
def logout():
    """
    Clear all session data and exit the Eyes Unclouded system.
    """
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('auth.login'))





