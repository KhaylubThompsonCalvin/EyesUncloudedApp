# ==============================================================================
# File: src/controllers/immersion_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Flask Immersion Route
# Author: Khaylub Thompson-Calvin
# Date: 04/19/2025
# ==============================================================================
# Description:
#   Web controller for analyzing story scenes through Maximus logic.
#   Supports both pre-tagged insights or dynamic emotion-based generation.
#   Logs each reflection to perception_log.json (Pacific Time).
# ==============================================================================

from flask import Blueprint, render_template, session
from src.utils.immersion_engine.scene_parser import get_scene_data
from src.utils.immersion_engine.virtue_inference import map_emotion_to_virtue
from src.utils.immersion_engine.maximus_engine import analyze_scene
from src.utils.immersion_engine.audio_controller import get_audio_path
from src.utils.immersion_engine.reflection_logger import log_reflection

# ----------------------------------------------------------------------
# Blueprint Initialization
# ----------------------------------------------------------------------
immersion_bp = Blueprint("immersion", __name__)

# ----------------------------------------------------------------------
# Route: Maximus Analysis – Scene Insight + Audio Narration
# ----------------------------------------------------------------------
@immersion_bp.route("/maximus-analysis/<scene_id>")
def maximus_analysis(scene_id):
    """
    Render Maximus symbolic deduction for a given scene.
    Uses emotion tags and virtue logic to determine insight and narration,
    then logs the result with Pacific Time.
    """
    # 1. Fetch the tagged scene
    scene = get_scene_data(scene_id)
    if not scene:
        return "Scene not found", 404

    # 2. Determine expression and virtue
    expression = scene.get("expression")
    virtue = scene.get("virtue_test") or map_emotion_to_virtue(expression)

    # 3. Get insight and audio file
    insight = scene.get("insight")
    audio_file = scene.get("audio_file")

    if not insight or not audio_file:
        result = analyze_scene(expression, virtue)
        insight = insight or result["insight"]
        audio_file = audio_file or result["audio_file"]

    # 4. Log this symbolic reflection
    user_role = session.get("role_type", "Unknown")
    log_reflection(scene_id, expression, virtue, insight, user_role)

    # 5. Render the analysis page
    return render_template(
        "maximus_analysis.html",
        scene=scene,
        insight=insight,
        audio_path=get_audio_path(audio_file)
    )
