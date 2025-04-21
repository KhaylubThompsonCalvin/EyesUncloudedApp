# ==============================================================================
# File: src/controllers/maximus_controller.py
# ==============================================================================
from flask import Blueprint, render_template, abort
import os

maximus_bp = Blueprint("maximus_bp", __name__)

@maximus_bp.route("/maximus-analysis/<trial_name>")
def maximus_trial(trial_name):
    print(f"[DEBUG] Trial route hit: {trial_name}")
    template_path = f"src/views/templates/maximus/{trial_name}.html"
    abs_path = os.path.abspath(template_path)
    print(f"[DEBUG] Looking for template at: {abs_path}")

    if os.path.exists(abs_path):
        print(f"[DEBUG] Template found. Rendering: {trial_name}")
        return render_template(f"maximus/{trial_name}.html")
    else:
        print(f"[ERROR] Template not found for trial: {trial_name}")
        abort(404, description=f"Trial page not found: {trial_name}")


