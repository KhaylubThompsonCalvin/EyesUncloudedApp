# ==============================================================================
# File: run.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Application Launcher
# Author: Khaylub Thompson-Calvin
# Date: 04/17/2025
# ==============================================================================
# Description:
#   This is the official entry point script to initiate the Eyes Unclouded system.
#
#   It launches the Flask development server locally, allowing all integrated
#   Blueprints, routes, and logic to become accessible for testing and iteration.
#
#   Symbolically, this script acts as the "Ignition Ritual"—triggering the system
#   that will one day serve as a behavioral archive, perceptual training engine,
#   and legacy vault.
#
#   Technical Specs:
#   • Port: 7777
#   • Mode: Debug = True
# ==============================================================================

from app import app

def main():
    """Ritual Start – Boot the Eyes Unclouded Flask server."""
    print("[INFO] Starting Eyes Unclouded App at http://127.0.0.1:7777")
    app.run(port=7777, debug=True)

# Pythonic entry condition: only executes when run directly
if __name__ == "__main__":
    main()
