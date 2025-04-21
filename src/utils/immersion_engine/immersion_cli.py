# ==============================================================================
# File: src/utils/immersion_engine/immersion_cli.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – CLI Immersion Tester
# Author: Khaylub Thompson-Calvin
# Date: 04/19/2025
# ==============================================================================
# Description:
#   Command-line interface for testing Maximus scene logic,
#   emotion → virtue mapping, and narration insight results.
# ==============================================================================

import argparse
from scene_parser import get_scene_data
from virtue_inference import map_emotion_to_virtue
from maximus_engine import analyze_scene
from audio_controller import get_audio_path

def main():
    """Run CLI test for Maximus AI immersion analysis."""
    parser = argparse.ArgumentParser(description="Immersion Engine CLI – Maximus Analysis")
    parser.add_argument('--scene', required=True, help='Scene ID to analyze')
    args = parser.parse_args()

    scene = get_scene_data(args.scene)
    if not scene:
        print(f"[X] Scene '{args.scene}' not found.")
        return

    print(f"[✓] Scene Loaded: {scene['chapter']}")
    expression = scene['expression']
    virtue = map_emotion_to_virtue(expression)

    print(f"[→] Emotion: {expression}")
    print(f"[→] Virtue Test: {virtue}")

    result = analyze_scene(expression, virtue)
    print(f"[►] Maximus Says: {result['insight']}")
    print(f"[►] Audio Path: {get_audio_path(result['audio_file'])}")

if __name__ == '__main__':
    main()
