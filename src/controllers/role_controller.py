# ==============================================================================
# File: src/controllers/role_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Role Selection & Audio Integration
# Author: Khaylub Thompson-Calvin
# Date: 04/17/2025
# ==============================================================================
# Description:
#   This controller governs the Role Type system—the symbolic archetypes through
#   which users engage the Eyes Unclouded App. It also links these roles to their
#   personalized onboarding audio stored under static/audio/.
#
#   Functionality:
#   • Route for selecting a Role Type with symbolic descriptions and preview audio
#   • Route for rendering the user dashboard with role-based audio context
#   • Includes session guard via custom login_required decorator
#
#   Symbolically, Role Types define perception lenses—"masks of awareness"
#   chosen by the user at initiation. These roles later shape the UI, responses,
#   audio logic, and eventual Class evolution.
# ==============================================================================

from flask import Blueprint, render_template, session, redirect, url_for
from functools import wraps

# ------------------------------------------------------------------------------
# Role Audio Mapping: Role Type → MP3 Filename
# All files are located in: src/views/static/audio/
# ------------------------------------------------------------------------------
ROLE_AUDIO = {
    'Seeker':     'Role_Seeker.mp3',
    'Strategist': 'Role_Strategist.mp3',
    'Mentor':     'Role_Mentor.mp3',
    'Cipher':     'Role_Cipher.mp3',
    'Observer':   'Role_Observer.mp3',
    'Warden':     'Role_Warden.mp3'
}

# ------------------------------------------------------------------------------
# Blueprint Setup
# ------------------------------------------------------------------------------
role_bp = Blueprint('roles', __name__, url_prefix='/roles')

# ------------------------------------------------------------------------------
# Session Guard – Protect Role-based Endpoints
# ------------------------------------------------------------------------------
def login_required(f):
    """
    Decorator: Restrict access to authenticated users.
    Redirects to login if 'user_id' not found in session.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated

# ------------------------------------------------------------------------------
# Route: /roles/select → Role Selection Interface
# ------------------------------------------------------------------------------
@role_bp.route('/select')
def select_role():
    """
    Render the role-selection page with symbolic archetypes.
    Each role contains:
      - name: role label
      - symbol: iconography
      - description: behavior profile
      - audio_filename: ElevenLabs narration file
    """
    base_roles = [
        {"name": "Seeker",      "symbol": "🔍", "description": "Questions everything."},
        {"name": "Strategist",  "symbol": "♟", "description": "Plans ahead."},
        {"name": "Mentor",      "symbol": "🕊", "description": "Guides through virtue."},
        {"name": "Cipher",      "symbol": "🧬", "description": "Speaks in symbols."},
        {"name": "Observer",    "symbol": "👁", "description": "Watches silently."},
        {"name": "Warden",      "symbol": "⚖", "description": "Balances justice."}
    ]

    # Attach audio filename to each role
    roles = []
    for r in base_roles:
        audio_file = ROLE_AUDIO.get(r['name'], 'Role_Overview.mp3')
        roles.append({**r, 'audio_filename': audio_file})

    # Narration overview of all roles
    overview_audio = 'Role_Overview.mp3'

    return render_template(
        'role_select.html',
        roles=roles,
        overview_audio=overview_audio
    )

# ------------------------------------------------------------------------------
# Route: /roles/dashboard → User Dashboard (Role-Aware)
# ------------------------------------------------------------------------------
@role_bp.route('/dashboard')
@login_required
def dashboard():
    """
    Render the central dashboard with a role-specific audio cue.
    Assumes session['role_type'] has been set at registration/login.
    """
    role = session.get('role_type', 'Seeker')
    audio_file = ROLE_AUDIO.get(role, 'Role_Overview.mp3')

    return render_template(
        'dashboard.html',
        user=session,
        role_audio=audio_file
    )



