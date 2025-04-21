# ==============================================================================
# File: src/utils/immersion_engine/scene_parser.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Immersion Engine
# Author: Khaylub Thompson‑Calvin
# Date: 04/19/2025
# ==============================================================================
# Description:
#   Parses the symbolic scene annotation file and retrieves scene data.
# ==============================================================================

import json
import os
import logging

log = logging.getLogger(__name__)

def get_scene_data(scene_id):
    """
    Retrieve the dictionary for a given scene ID from the JSON annotation file.
    Uses an absolute path so it works no matter the current working directory.
    """
    # Compute project root by going up three levels from this file
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )
    data_path = os.path.join(project_root, "src", "data", "story_annotations.json")

    try:
        with open(data_path, 'r', encoding='utf-8-sig') as file:
            scenes = json.load(file) or []
    except FileNotFoundError:
        log.error(f"Scene file not found at {data_path}")
        scenes = []
    except json.JSONDecodeError as e:
        log.error(f"Failed to parse JSON at {data_path}: {e}")
        scenes = []

    return next((s for s in scenes if s.get('scene_id') == scene_id), None)
    data_path = os.path.join(project_root, "src", "data", "story_annotations.json")

    try:
        with open(data_path, 'r', encoding='utf-8-sig') as file:
            scenes = json.load(file) or []
    except FileNotFoundError:
        log.error(f"Scene file not found at {data_path}")
        scenes = []
    except json.JSONDecodeError as e:
        log.error(f"Failed to parse JSON at {data_path}: {e}")
        scenes = []

    return next((s for s in scenes if s.get('scene_id') == scene_id), None)




