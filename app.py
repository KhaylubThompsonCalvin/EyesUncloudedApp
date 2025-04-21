# ==============================================================================
# File: app.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Sprint 1
# Author: Khaylub Thompson‑Calvin
# Date: 04/20/2025
# ==============================================================================
# Description:
#   Core Flask app launcher with modular MVC routing and secure config loading.
# ==============================================================================

import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(
    __name__,
    template_folder="src/views/templates",
    static_folder="src/views/static"
)

# Secret key from .env
app.secret_key = os.getenv("SECRET_KEY")
if not app.secret_key:
    raise ValueError("[ERROR] SECRET_KEY missing from .env")

# MongoDB configuration
from src.extensions import mongo
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo.init_app(app)

# ==============================
# Register Blueprints (Routes)
# ==============================

from src.controllers.main_controller import main_bp
app.register_blueprint(main_bp)

from src.controllers.auth_controller import auth_bp
app.register_blueprint(auth_bp)

from src.controllers.notification_controller import notification_bp
app.register_blueprint(notification_bp)

from src.controllers.role_controller import role_bp
app.register_blueprint(role_bp, url_prefix="/role")

from src.controllers.template_controller import template_bp
app.register_blueprint(template_bp, url_prefix="/template")

from src.controllers.audio_controller import audio_bp
app.register_blueprint(audio_bp)

from src.controllers.emotion_log_controller import emotion_log_bp
app.register_blueprint(emotion_log_bp)

from src.controllers.oracle_controller import oracle_bp
app.register_blueprint(oracle_bp)

from src.controllers.chat_controller import chat_bp
app.register_blueprint(chat_bp)

from src.controllers.immersion_controller import immersion_bp
app.register_blueprint(immersion_bp)

# ✅ New: Maximus Controller for Perception Symbolism
from src.controllers.maximus_controller import maximus_bp
app.register_blueprint(maximus_bp)

# ==============================
# Launch App
# ==============================

if __name__ == "__main__":
    print("[INFO] Starting Eyes Unclouded App at http://127.0.0.1:7777")
    app.run(port=7777, debug=False)


