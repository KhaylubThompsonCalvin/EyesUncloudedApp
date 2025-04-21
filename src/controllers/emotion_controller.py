# ==============================================================================
# File: emotion_controller.py
# Route: /emotion-log
# Description: Visual browser log of all emotion observations (from JSON)
# Author: Khaylub Thompson-Calvin
# ==============================================================================

import json
import os
from flask import Blueprint, render_template

emotion_bp = Blueprint("emotion", __name__)

LOG_PATH = os.path.join(os.path.dirname(__file__), "../../logs/emotion_log.json")
DESCRIPTIONS = {
    "anger": "Triggered by perceived injustice or threat.",
    "contempt": "A unilateral expression of superiority.",
    "disgust": "Signals repulsion; nose wrinkle, upper lip raised.",
    "fear": "Raised eyelids and wide eyes show alarm.",
    "happiness": "Marked by Duchenne smile (eye crinkle + mouth lift).",
    "neutral": "Baseline comparison or suppression of feeling.",
    "sadness": "Loss or empathy; brows drawn up and together.",
    "surprise": "Sudden alertness, brows raised and jaw dropped."
}


@emotion_bp.route("/emotion-log")
def emotion_log():
    """Render all observed emotion logs to the browser UI."""
    try:
        with open(LOG_PATH, "r") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    return render_template("emotion_log.html", logs=logs, descriptions=DESCRIPTIONS)
