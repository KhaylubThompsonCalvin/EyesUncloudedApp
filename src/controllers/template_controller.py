# ==============================================================================
# File: src/controllers/template_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Behavioral Legacy Engine
# Author: Khaylub Thompson‑Calvin
# Date: 04/17/2025
# ==============================================================================
# Description:
#   This controller defines the Blueprint for managing reusable “Perceptual Templates.”
#   Templates allow users to encode symbolic narratives, strategies, or virtue-based
#   teachings—preserved for future recall during broadcasts.
#
#   Key Features:
#   • Authenticated users can create templates with name, subject, and body
#   • Optional upload support (images, videos, documents)
#   • File uploads are stored in /static/uploads/templates
#   • Metadata stored in MongoDB (collection: templates)
#
#   Symbolically, these templates act as behavioral blueprints—scrolls of wisdom
#   or deception, accessible to future selves or AI companions.
# ==============================================================================

import os
from datetime import datetime
from flask import (
    Blueprint, render_template, request,
    redirect, url_for, flash, session
)
from werkzeug.utils import secure_filename

# Import PyMongo instance (MongoDB client from app context)
from app import mongo

# ------------------------------------------------------------------------------
# Blueprint Registration
# ------------------------------------------------------------------------------
template_bp = Blueprint("template", __name__)

# MongoDB collection
templates_collection = mongo.db.templates

# ------------------------------------------------------------------------------
# File Upload Configuration
# ------------------------------------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "views", "static"))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads", "templates")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Allowed file extensions for uploads (symbolic evidence or narrative context)
ALLOWED_EXT = {
    "png", "jpg", "jpeg", "gif",         # images
    "mp4", "webm", "ogg",                # videos
    "pdf", "txt",                        # documents
    "doc", "docx"                        # Word files
}

def allowed_file(filename):
    """
    Return True if the file’s extension is in our allowed types.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT

# ------------------------------------------------------------------------------
# Session-Based Access Control
# ------------------------------------------------------------------------------
def login_required(f):
    """
    Decorator to restrict access to authenticated users only.
    Redirects to login if session lacks a user_id.
    """
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated

# ------------------------------------------------------------------------------
# Template Creation Route (GET / POST)
# ------------------------------------------------------------------------------
@template_bp.route("/create_template", methods=["GET", "POST"])
@login_required
def create_template():
    """
    GET: Render the template creation form.
    POST: Process form data, handle file upload, and archive new template in DB.
    """
    if request.method == "POST":
        name    = request.form.get("template_name")
        subject = request.form.get("template_subject")
        body    = request.form.get("template_body")

        # Optional symbolic artifact (image, video, etc.)
        file = request.files.get("attachment")
        filename = None

        if file and file.filename:
            if allowed_file(file.filename):
                safe_name = secure_filename(file.filename)
                filename  = f"{session['user_id']}_{safe_name}"  # Tie file to creator
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                flash("Unsupported file type.", "danger")
                return redirect(url_for("template.create_template"))

        # Construct template document
        tpl = {
            "name": name,
            "subject": subject,
            "body": body,
            "attachment": filename,                         # Null if no upload
            "createdBy": session.get("username"),
            "created_at": datetime.utcnow()
        }

        # Insert into MongoDB
        try:
            templates_collection.insert_one(tpl)
            flash("Template archived successfully.", "success")
        except Exception as e:
            flash(f"Error saving template: {e}", "danger")

        return redirect(url_for("template.create_template"))

    # GET: Render template creation form
    return render_template("create_template.html")



