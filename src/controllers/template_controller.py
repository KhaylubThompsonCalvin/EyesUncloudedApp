# ==============================================================================
# File: src/controllers/template_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Template Builder
# Author: Khaylub Thompson‑Calvin
# Date: 04/17/2025
# ==============================================================================
# Manages CRUD on reusable “narrative blueprint” templates.
# ==============================================================================

import os
from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)
from src.extensions import mongo  # <- no circular import here

# Blueprint setup
template_bp = Blueprint("template", __name__, url_prefix="/template")

# MongoDB collection
templates_col = mongo.db.templates

def login_required(f):
    """Ensure the user is logged in before accessing the route."""
    from functools import wraps

    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated

@template_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_template():
    """
    GET:  Show form to author a new template and list all existing ones.
    POST: Persist a new narrative blueprint into MongoDB.
    """
    if request.method == "POST":
        # Gather form data
        name = request.form.get("name", "").strip()
        body = request.form.get("body", "").strip()

        # Build the document
        new_template = {
            "name":       name,
            "body":       body,
            "author":     session.get("username"),
            "created_at": datetime.utcnow()
        }

        # Save to MongoDB
        try:
            templates_col.insert_one(new_template)
            flash("Template saved.", "success")
        except Exception as e:
            flash(f"Error saving template: {e}", "danger")

        # Redirect back to clear the POST
        return redirect(url_for("template.create_template"))

    # GET: fetch all templates, newest first
    all_templates = list(
        templates_col.find()
                       .sort("created_at", -1)
    )

    return render_template(
        "template_create.html",
        templates=all_templates
    )





