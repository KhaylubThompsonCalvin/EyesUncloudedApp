# ==============================================================================
# File: src/utils/immersion_engine/reflection_logger.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Immersion Engine
# Author: Khaylub Thompson‑Calvin
# Date: 04/19/2025
# ==============================================================================
# Description:
#   Logs Maximus emotion insights to perception_log.json using Pacific Time.
#   Safely handles empty or invalid JSON by initializing an empty list.
# ==============================================================================

import os
import json
from datetime import datetime
from zoneinfo import ZoneInfo

LOG_PATH = os.path.join("src", "data", "perception_log.json")

def log_reflection(scene_id, expression, virtue, insight, user_role="Unknown"):
    """
    Append a symbolic insight log to perception_log.json, timestamped
    in America/Los_Angeles timezone. If the file is missing or malformed,
    starts with an empty list.
    """
    # Generate Pacific‑time timestamp
    timestamp = datetime.now(ZoneInfo("America/Los_Angeles")) \
                    .strftime("%Y-%m-%d %I:%M:%S %p %Z")

    log_entry = {
        "scene_id": scene_id,
        "expression": expression,
        "virtue_test": virtue,
        "insight": insight,
        "user_role": user_role,
        "timestamp": timestamp
    }

    # Safely load existing data or start with empty list
    try:
        with open(LOG_PATH, "r") as f:
            data = json.load(f)
            if data is None:
                data = []
    except (json.JSONDecodeError, FileNotFoundError):
        data = []

    # Append the new entry and write back
    data.append(log_entry)
    with open(LOG_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[LOGGED] Insight for {scene_id} at {timestamp}")

