# ==============================================================================
# File: src/controllers/maximus_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Maximus Analysis Engine
# Author: Khaylub Thompson-Calvin
# Date: 04/20/2025
# ==============================================================================
# Description:
#   Handles symbolic routes like Maximus’ perception trials.
#   Route: /maximus-analysis/<trial>
# ==============================================================================

from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

maximus_bp = Blueprint("maximus", __name__)

@maximus_bp.route("/maximus-analysis/<trial_name>")
def maximus_trial(trial_name):
    template_path = f"maximus/{trial_name}.html"
    print(f"[DEBUG] Attempting to render: {template_path}")
    try:
        return render_template(template_path)
    except TemplateNotFound:
        return f"[ERROR] Template not found: {template_path}", 404

