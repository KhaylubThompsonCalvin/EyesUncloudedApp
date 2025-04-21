# ==============================================================================
# File: src/controllers/main_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Main & Splash Routes
# Author: Khaylub Thompson-Calvin
# Date: 04/17/2025
# ==============================================================================
# Description:
#   This controller defines the foundational gateway routes for the Eyes Unclouded App.
#   It manages:
#     • Root redirection (/) → symbolic entrypoint (/splash)
#     • Splash animation and onboarding prompt
#     • Temporary Class Reveal testing interface for development
#     • Real‑time micro‑expression trial launcher
# ==============================================================================

from flask import Blueprint, render_template, redirect, url_for

# ------------------------------------------------------------------------------
# Blueprint Setup
# ------------------------------------------------------------------------------
main_bp = Blueprint("main", __name__)


# ------------------------------------------------------------------------------
# Route: / → Redirect to Splash Gateway
# ------------------------------------------------------------------------------
@main_bp.route("/")
def index():
    """
    Redirect root access to the splash screen.
    This keeps the "/" route clean and symbolically sends the user
    through the Eyes Unclouded gateway experience.
    """
    return redirect(url_for("main.splash"))


# ------------------------------------------------------------------------------
# Route: /splash → Welcome & Audio Prompt Screen
# ------------------------------------------------------------------------------
@main_bp.route("/splash")
def splash():
    """
    Render the splash.html template, which contains:
      - Eyes Unclouded sigil
      - Audio onboarding via ElevenLabs narration
      - Fade-out transition on click
    """
    return render_template("splash.html")


# ------------------------------------------------------------------------------
# Route: /reveal → Class Archetype Reveal (Testing Only)
# ------------------------------------------------------------------------------
@main_bp.route("/reveal")
def class_reveal_test():
    """
    TEMPORARY route used for testing the Class Reveal interface.
    Eventually, this will be gated by perception scores and virtue logs.
    """
    return render_template(
        "class_reveal.html",
        user={
            "class_name": "The Architect",
            "class_title": "Queen of the Eagle Order",
            "animal_order": "Eagle",
            "class_description": (
                "You see patterns where others see chaos. "
                "You are tasked with vision, precision, and legacy. "
                "This title was not given — it was earned."
            ),
        },
    )


# ------------------------------------------------------------------------------
# Route: /observe_trial → Real‑Time Observation Trial
# ------------------------------------------------------------------------------
@main_bp.route("/observe_trial")
def observe_trial():
    """
    Launches the real‑time observation mode where the user can
    log micro‑expressions in a live trial.
    """
    return render_template("observe_trial.html")

