# ======================================================================
# File: src/utils/immersion_engine/audio_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Immersion Engine
# Author: Khaylub Thompson‑Calvin
# Date: 04/19/2025
# ======================================================================
# Description:
#   Formats a filename into the public URL path for audio playback.
# ======================================================================

def get_audio_path(file_name):
    """
    Given an audio filename, return the URL path for Flask to serve.
    """
    return f"/static/audio/maximus_narrations/{file_name}"
