# ==============================================================================
# File: src/utils/immersion_engine/maximus_engine.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Immersion Engine
# Author: Khaylub Thompson-Calvin
# Date: 04/19/2025
# ==============================================================================
# Description:
#   Contains logic for symbolic deduction by Maximus. Based on emotion and
#   virtue pairs, it returns a strategic insight quote and the audio narration.
# ==============================================================================

def analyze_scene(expression, virtue):
    """Return audio + insight based on symbolic emotion/virtue pairing."""
    expression = expression.lower()
    virtue = virtue.lower()

    match = f"{expression}_{virtue}"

    insight_map = {
        "anger_patience": (
            "Maximus_Anger_Patience.mp3",
            "In fury, restraint reveals the truer strength."
        ),
        "fear_courage": (
            "Maximus_Fear_Courage.mp3",
            "Bravery is not the absence of fear—it is acting while afraid."
        ),
        "sadness_hope": (
            "Maximus_Sadness_Hope.mp3",
            "Even in grief, the light of hope endures beneath the ashes."
        ),
        "contempt_humility": (
            "Maximus_Contempt_Humility.mp3",
            "True power is not in scorn but in silence that listens."
        ),
    }

    # Return match or default fallback
    audio_file, insight = insight_map.get(match, (
        "Maximus_Generic_Reflection.mp3",
        "Every gesture tells a story—few know how to listen."
    ))

    return {
        "audio_file": audio_file,
        "insight": insight
    }
