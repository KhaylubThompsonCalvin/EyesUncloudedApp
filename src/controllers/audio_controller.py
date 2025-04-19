# ==============================================================================
# File: src/controllers/audio_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Audio Serving Blueprint
# Author: Khaylub Thompson-Calvin
# Date: 04/18/2025
# ==============================================================================
# Description:
#   This blueprint serves audio assets (e.g., role narrations, legacy messages)
#   stored in `src/views/static/audio/`. These files are used for:
#     • Onboarding users into Role Types and Classes
#     • Narrating symbolic templates and perception logs
#     • Creating immersive audio-guided experiences
#
#   The route ensures secure and accurate path resolution before playback.
#   Example usage:
#     GET /audio/Role_Seeker.mp3 → serves the Seeker narration file
# ==============================================================================

import os
from flask import Blueprint, current_app, send_from_directory, abort, jsonify

# ------------------------------------------------------------------------------
# Blueprint Configuration
# ------------------------------------------------------------------------------
audio_bp = Blueprint('audio', __name__, url_prefix='/audio')

# ------------------------------------------------------------------------------
# Route: /audio/<filename> – Serve Audio from Static Folder
# ------------------------------------------------------------------------------
@audio_bp.route('/<path:filename>')
def serve_audio(filename):
    """
    Serve an audio file from the static/audio folder.
    Automatically resolves full path using current_app root.
    
    Parameters:
        filename (str): The name of the audio file to serve (e.g. Role_Seeker.mp3)
    
    Returns:
        Response: Audio file or JSON error response (404 if not found)
    """
    # Compute absolute path to the static audio directory
    audio_dir = os.path.join(
        current_app.root_path,
        'src', 'views', 'static', 'audio'
    )

    full_path = os.path.join(audio_dir, filename)

    # --------------------------------------------------------------------------
    # Security: Only serve if the file actually exists
    # --------------------------------------------------------------------------
    if not os.path.isfile(full_path):
        return abort(404, description=jsonify({"error": "Audio file not found."}))

    # --------------------------------------------------------------------------
    # Send file from the audio directory
    # --------------------------------------------------------------------------
    return send_from_directory(audio_dir, filename)

