# ==============================================================================
# File: src/controllers/chat_controller.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – AI Speaker Box
# Author: Khaylub Thompson‑Calvin
# Date: 04/17/2025
# ==============================================================================
import os
from flask import Blueprint, render_template, request, jsonify, session, flash, redirect, url_for
import openai
from dotenv import load_dotenv
from functools import wraps

# Load your OPENAI_API_KEY from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Blueprint setup
chat_bp = Blueprint("chat", __name__, url_prefix="/chat")

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to chat with the Oracle AI.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated

@chat_bp.route("", methods=["GET"])
@login_required
def chat_page():
    return render_template("chat.html")

@chat_bp.route("/api", methods=["POST"])
@login_required
def chat_api():
    """
    Receives a JSON payload: { "history": [ {role, content}, ... ] }
    Returns JSON: { "reply": "...", "error": optional error message }
    """
    data = request.get_json(force=True)
    history = data.get("history", [])

    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history
        )
        reply = resp.choices[0].message.content
        return jsonify({"reply": reply})

    except openai.error.RateLimitError as e:
        # 429 from too many requests/quota
        return jsonify({
            "reply": "[Oracle is resting—quota exceeded. Please try again later.]",
            "error": str(e)
        }), 429

    except openai.error.AuthenticationError as e:
        # key invalid
        return jsonify({
            "reply": "[Authentication error. Check your API key.]",
            "error": str(e)
        }), 401

    except Exception as e:
        # catch‑all
        return jsonify({
            "reply": "[Error contacting AI: please try again later.]",
            "error": str(e)
        }), 500


