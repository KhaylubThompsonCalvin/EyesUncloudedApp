# ==============================================================================
# File: microexpression_decoder_simple.py
# Project: Eyes Unclouded App – Emotion Training CLI Module
# Author: Khaylub Thompson-Calvin
# Date: 2025-04-19
# ==============================================================================
# Description:
#   Terminal-based CLI tool for analyzing facial expression image counts.
#   Extracts symbolic emotion frequency and neuroscience-backed interpretation
#   for each core emotion, as part of the Eyes Unclouded training engine.
#
#   This module supports data validation and logic for emotion decoding.
#   Used during symbolic gameplay, training, or preprocessing.
# ==============================================================================

import os
from collections import defaultdict

# -------------------------------------------------------------------------------
# Directory Configuration
# -------------------------------------------------------------------------------
EXPRESSIONS_PATH = "../../views/static/images/expressions"

# -------------------------------------------------------------------------------
# Universal Emotions (Based on Ekman's 7 + neutral)
# -------------------------------------------------------------------------------
UNIVERSAL_EMOTIONS = [
    "anger", "contempt", "disgust", "fear",
    "happiness", "neutral", "sadness", "surprise"
]

# -------------------------------------------------------------------------------
# Emotion Descriptions (Neuroscience-Based)
# -------------------------------------------------------------------------------
def describe_emotion(emotion):
    """
    Return a neuroscience-based interpretation of the emotion.
    """
    descriptions = {
        "anger": "Triggered by perceived injustice or threat. Observable in lowered brows and glaring eyes.",
        "contempt": "A unilateral expression of superiority—one corner of the mouth raised.",
        "disgust": "An aversion response—nose wrinkle and upper lip raise signal repulsion.",
        "fear": "Evolutionarily tied to survival; wide eyes and raised eyelids signal potential danger.",
        "happiness": "Marked by Duchenne smile—eye crinkles and lip raise linked to reward pathways.",
        "neutral": "Baseline state—used for comparison or when emotion is suppressed.",
        "sadness": "Signals loss or empathy; inner brow raise and downward mouth angle.",
        "surprise": "Heightened alertness—raised brows and dropped jaw reflect sudden stimulus."
    }
    return descriptions.get(emotion, "Unknown emotion.")

# -------------------------------------------------------------------------------
# Count Expression Images by Emotion
# -------------------------------------------------------------------------------
def get_expression_counts():
    """
    Scan the expressions directory and return a dictionary of emotion to file count.
    """
    counts = defaultdict(int)

    if not os.path.exists(EXPRESSIONS_PATH):
        print(f"[ERROR] Directory not found: {EXPRESSIONS_PATH}")
        return counts

    for filename in os.listdir(EXPRESSIONS_PATH):
        emotion = filename.split('_')[0]
        if emotion in UNIVERSAL_EMOTIONS:
            counts[emotion] += 1

    return dict(counts)

# -------------------------------------------------------------------------------
# Terminal Entry Point – Run Symbolic Emotion Summary
# -------------------------------------------------------------------------------
if __name__ == "__main__":
    print("\nMicroexpression Decoder Summary\n")

    counts = get_expression_counts()

    if not counts:
        print("No expression images found or path is invalid.")
    else:
        for emotion, count in counts.items():
            print(f"{emotion.title():<10}: {count} images")
            print("Interpretation:", describe_emotion(emotion))
            print("-" * 60)


