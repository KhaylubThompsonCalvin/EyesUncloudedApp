# ==============================================================================
# File: src/controllers/immersion_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Flask Immersion Route
# Author: Khaylub Thompson-Calvin
# Date: 04/19/2025
# ==============================================================================
# Description:
#   Web controller for analyzing story scenes through Maximus logic.
#   Uses emotion + virtue to trigger symbolic insight and narrated audio.
# ==============================================================================

from flask import Blueprint, render_template
from src.utils.immersion_engine.scene_parser import get_scene_data
from src.utils.immersion_engine.virtue_inference import map_emotion_to_virtue
from src.utils.immersion_engine.maximus_engine import analyze_scene
from src.utils.immersion_engine.audio_controller import get_audio_path

# ----------------------------------------------------------------------
# Blueprint Initialization
# ----------------------------------------------------------------------
immersion_bp = Blueprint('immersion', __name__)

# ----------------------------------------------------------------------
# Route: Maximus Analysis – Scene Insight + Audio Narration
# ----------------------------------------------------------------------
@immersion_bp.route('/maximus-analysis/<scene_id>')
def maximus_analysis(scene_id):
    """
    Render Maximus symbolic deduction for a given scene.
    Uses emotion tags and virtue logic to determine insight and narration.
    """
    scene = get_scene_data(scene_id)
    if not scene:
        return "Scene not found", 404

    expression = scene['expression']
    virtue = map_emotion_to_virtue(expression)
    result = analyze_scene(expression, virtue)

    return render_template("maximus_analysis.html",
                           scene=scene,
                           insight=result['insight'],
                           audio_path=get_audio_path(result['audio_file']))

# ----------------------------------------------------------------------
# Export Blueprint (required for app.py registration)
# ----------------------------------------------------------------------
# This ensures immersion_bp is visible to app.py on import.

