# ======================================================================
# File: src/controllers/audio_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Audio Static Serving
# Author: Khaylub Thompson‑Calvin
# Date: 04/19/2025
# ======================================================================
# Description:
#   Blueprint to serve narration audio files from the static folder.
# ======================================================================

import os
from flask import Blueprint, send_from_directory, current_app

audio_bp = Blueprint('audio', __name__)

@audio_bp.route('/audio/<path:filename>')
def serve_audio(filename):
    """
    Serve the requested audio file from the static audio directory.
    """
    audio_dir = os.path.join(
        current_app.root_path,
        'src', 'views', 'static', 'audio'
    )
    return send_from_directory(audio_dir, filename)
