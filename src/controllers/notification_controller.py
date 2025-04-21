# ==============================================================================
# File: src/controllers/notification_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Behavioral Legacy Engine
# Author: Khaylub Thompson‑Calvin
# Date: 04/17/2025
# ==============================================================================
#   Manages strategic broadcasts (“Perception Signals”) and their archive.
# ==============================================================================

import os
from datetime import datetime
from functools import wraps
from flask import (
    Blueprint, render_template, request,
    redirect, url_for, flash, session
)
from werkzeug.utils import secure_filename

from src.extensions import mongo  # ← pull in our shared PyMongo instance

# Blueprint setup
notification_bp = Blueprint("notification", __name__, url_prefix="/notify")

# Collection shortcut
notifications_collection = mongo.db.notifications

# Upload config
BASE_DIR     = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            "..", "views", "static"))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads", "videos")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_VIDEO_EXT = {"mp4", "webm", "ogg"}

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_VIDEO_EXT

@notification_bp.route("", methods=["GET", "POST"])
@login_required
def notifications():
    if request.method == "POST":
        title       = request.form.get("title")
        message     = request.form.get("message")
        virtue_tag  = request.form.get("virtue_tag")
        emotion_tag = request.form.get("emotion_tag")

        video      = request.files.get("video")
        video_name = None
        if video and allowed_file(video.filename):
            safe = secure_filename(video.filename)
            video_name = f"{session['user_id']}_{safe}"
            video.save(os.path.join(UPLOAD_FOLDER, video_name))

        note = {
            "title":     title,
            "message":   message,
            "virtue_tag": virtue_tag,
            "emotion_tag": emotion_tag,
            "createdBy": session.get("username"),
            "sent_at":   datetime.utcnow(),
            "video":     video_name
        }

        try:
            notifications_collection.insert_one(note)
            flash("Signal broadcasted successfully.", "success")
        except Exception as e:
            flash(f"Failed to send signal: {e}", "danger")

        return redirect(url_for("notification.notifications"))

    all_notes = list(notifications_collection.find()
                     .sort("sent_at", -1))
    return render_template("notifications.html",
                           notifications=all_notes)

@notification_bp.route("/log")
@login_required
def notification_log():
    from datetime import datetime
    start = request.args.get("start_date")
    end   = request.args.get("end_date")
    query = {}
    if start and end:
        try:
            s = datetime.strptime(start, "%Y-%m-%d")
            e = datetime.strptime(end,   "%Y-%m-%d")
            query["sent_at"] = {"$gte": s, "$lte": e}
        except ValueError:
            flash("Invalid date format.", "danger")
            return redirect(url_for("notification.notifications"))

    notes = list(notifications_collection.find(query)
                 .sort("sent_at", -1))
    return render_template("notification_log.html",
                           notifications=notes)

