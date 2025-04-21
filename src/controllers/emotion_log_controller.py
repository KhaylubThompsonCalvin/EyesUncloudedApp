"""
Emotion Log Controller – Eyes Unclouded App
Purpose: Reads logged emotions and renders them in a browser dashboard.
Author: Khaylub Thompson-Calvin
Date: 2025-04-19
"""

import os
import json
from flask import Blueprint, render_template

emotion_log_bp = Blueprint("emotion_log", __name__)
LOG_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../logs/emotion_log.json")
)

DESCRIPTIONS = {
    "anger": "Triggered by perceived injustice or threat. "
             "Observable in lowered brows and glaring eyes.",
    "contempt": "A unilateral expression of superiority—"
                "one corner of the mouth raised.",
    "disgust": "An aversion response—nose wrinkle and upper lip "
               "raise signal repulsion.",
    "fear": "Evolutionarily tied to survival; wide eyes and raised eyelids "
            "signal potential danger.",
    "happiness": "Marked by Duchenne smile—eye crinkles and lip raise "
                 "linked to reward pathways.",
    "neutral": "Baseline state—used for comparison or when emotion is suppressed.",
    "sadness": "Signals loss or empathy; inner brow raise and downward mouth angle.",
    "surprise": "Heightened alertness—raised brows and dropped jaw "
                "reflect sudden stimulus."
}


@emotion_log_bp.route("/emotion-log")
def show_emotion_log():
    """Render a card for each logged emotion observation."""
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH) as f:
            logs = json.load(f)
    else:
        logs = []

    return render_template(
        "emotion_log.html",
        logs=logs,
        descriptions=DESCRIPTIONS
    )


