# ==============================================================================
# File: oracle_controller.py
# Project: Eyes Unclouded App – Oracle Insight Module
# Author: Khaylub Thompson-Calvin
# Date: 2025-04-19
# ==============================================================================
# Description:
#   Reads the emotion_log.json, tallies entries, and renders
#   an AI‑style “oracle” insight at the /oracle route.
# ==============================================================================

import os
import json
from collections import Counter
from flask import Blueprint, render_template

oracle_bp = Blueprint("oracle", __name__)
LOG_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../logs/emotion_log.json")
)


@oracle_bp.route("/oracle")
def oracle_insight():
    """
    Count occurrences of each emotion, find the most common one,
    and render an “oracle” insight page.
    """
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH) as f:
            logs = json.load(f)
    else:
        logs = []

    counts = Counter(entry["emotion"] for entry in logs if "emotion" in entry)
    most_common = counts.most_common(1)[0] if counts else ("none", 0)

    return render_template(
        "oracle.html",
        logs=logs,
        summary=most_common
    )