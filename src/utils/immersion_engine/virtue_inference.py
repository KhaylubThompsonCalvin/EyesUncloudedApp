# ==============================================================================
# File: src/utils/immersion_engine/virtue_inference.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Immersion Engine
# Author: Khaylub Thompson-Calvin
# Date: 04/19/2025
# ==============================================================================
# Description:
#   Maps raw emotion input (microexpression) to its associated
#   symbolic virtue test, which will guide the narrative analysis.
# ==============================================================================

def map_emotion_to_virtue(emotion):
    """Map emotion to symbolic virtue being tested in the story context."""
    emotion = emotion.lower()
    mapping = {
        "anger": "patience",
        "fear": "courage",
        "sadness": "hope",
        "contempt": "humility",
        "disgust": "tolerance",
        "surprise": "mindfulness",
        "happiness": "gratitude",
        "neutral": "wisdom"
    }
    return mapping.get(emotion, "reflection")
