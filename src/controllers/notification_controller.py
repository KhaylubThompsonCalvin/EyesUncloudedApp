# ==============================================================================
# File: src/controllers/notification_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Behavioral Legacy Engine
# Author: Khaylub Thompson‑Calvin
# Date: 04/17/2025
# ==============================================================================
# Description:
#   This controller manages the broadcast and archival of symbolic notifications,
#   also called “Perception Signals.” These logs include virtue tags, emotion tones,
#   and may optionally include uploaded video evidence.
#
#   Functional Highlights:
#   • Authenticated users can submit strategic messages (insights or warnings)
#   • Optional video evidence uploads (.mp4, .webm, .ogg)
#   • MongoDB stores metadata and filenames for later review
#   • All broadcasts are viewable from the same endpoint (/notifications)
#
#   Symbolically, each notification is a ripple in the perception engine—
#   a recorded echo of insight, designed to train, reflect, or awaken.
# ==============================================================================

import os
from datetime import datetime
from flask import (
    Blueprint, render_template, request,
    redirect, url_for, flash, session
)
from werkzeug.utils import secure_filename

# Import the PyMongo instance from app.py
from app import mongo

# Blueprint configuration
notification_bp = Blueprint("notification", __name__, url_prefix="/notify")

# MongoDB collection
notifications_collection = mongo.db.notifications

# Compute upload folder relative to this file
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "views", "static"))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads", "videos")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Whitelist of allowed video extensions
ALLOWED_VIDEO_EXT = {"mp4", "webm", "ogg"}


def login_required(f):
    """Decorator to ensure the user is logged in before accessing the route."""
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated


def allowed_file(filename):
    """Return True if the filename has an allowed video extension."""
    return "." in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_VIDEO_EXT


@notification_bp.route("", methods=["GET", "POST"])
@login_required
def notifications():
    """
    GET: Render the submission form plus list of past notifications.
    POST: Save a new notification, optionally handling a video upload.
    """
    if request.method == "POST":
        title       = request.form.get("title")
        message     = request.form.get("message")
        virtue_tag  = request.form.get("virtue_tag")
        emotion_tag = request.form.get("emotion_tag")

        # Handle optional video upload
        video_file    = request.files.get("video")
        video_filename = None

        if video_file and video_file.filename and allowed_file(video_file.filename):
            secure_name    = secure_filename(video_file.filename)
            # prefix with user_id to avoid collisions
            video_filename = f"{session['user_id']}_{secure_name}"
            save_path      = os.path.join(UPLOAD_FOLDER, video_filename)
            video_file.save(save_path)

        # Construct our notification document
        note = {
            "title":       title,
            "message":     message,
            "virtue_tag":  virtue_tag,
            "emotion_tag": emotion_tag,
            "createdBy":   session.get("username"),
            "sent_at":     datetime.utcnow(),
            "video":       video_filename  # None if no upload
        }

        try:
            notifications_collection.insert_one(note)
            flash("Signal broadcasted successfully.", "success")
        except Exception as e:
            flash(f"Failed to send signal: {e}", "danger")

        return redirect(url_for("notification.notifications"))

    # GET: fetch and display all past notifications
    all_notes = list(notifications_collection.find().sort("sent_at", -1))
    return render_template("notifications.html", notifications=all_notes)


@notification_bp.route("/log", methods=["GET"])
@login_required
def notification_log():
    """
    GET: Render the filtered archive of past notifications.
    Accepts 'start_date' and 'end_date' as GET parameters.
    """
    start_date = request.args.get('start_date')
    end_date   = request.args.get('end_date')
    query = {}
    if start_date and end_date:
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end   = datetime.strptime(end_date, '%Y-%m-%d')
            # MongoDB stores UTC timestamps; adjust if needed
            query['sent_at'] = { '$gte': start, '$lte': end }
        except ValueError:
            flash("Invalid date format.", "danger")
            return redirect(url_for('notification.notifications'))

    filtered = list(notifications_collection.find(query).sort("sent_at", -1))
    return render_template("notification_log.html", notifications=filtered)
