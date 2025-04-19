# ==============================================================================
# File: app.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Sprint 1
# Author: Khaylub Thompson-Calvin
# Date: 04/17/2025
# ==============================================================================
# Description:
#   This is the central launcher and blueprint registrar for the Eyes Unclouded App.
#
#   It performs the following:
#   • Loads .env environment variables (MONGO_URI, SECRET_KEY)
#   • Initializes Flask with Jinja templating and static pathing
#   • Configures MongoDB connection using Flask-PyMongo
#   • Registers modular Blueprints that represent symbolic routes:
#       - main (splash, home, class reveal)
#       - auth (register, login, logout)
#       - notify (strategic broadcasts)
#       - role (role-type onboarding and dashboard logic)
#       - template (message blueprints for future signals)
#       - audio (dynamic narration delivery from static/audio)
#   • Runs development server on http://127.0.0.1:7777
#
#   This file acts as the application’s "Core Invocation Scroll."
# ==============================================================================

import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv

# -------------------------------------------------------------------------------
# Load Environment Variables (from .env)
# -------------------------------------------------------------------------------
load_dotenv()

# -------------------------------------------------------------------------------
# Flask App Initialization (template and static directories declared)
# -------------------------------------------------------------------------------
app = Flask(
    __name__,
    template_folder="src/views/templates",
    static_folder="src/views/static"
)

# Session Key Initialization (used for secure user sessions)
app.secret_key = os.getenv("SECRET_KEY")
if not app.secret_key:
    raise ValueError("[ERROR] SECRET_KEY missing from environment variables!")

# -------------------------------------------------------------------------------
# MongoDB Configuration (via PyMongo)
# -------------------------------------------------------------------------------
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

# -------------------------------------------------------------------------------
# Blueprint Registration – Modular Routes (MVC Structure)
# -------------------------------------------------------------------------------

#  Root Interface: splash, home, class reveal
from src.controllers.main_controller import main_bp
app.register_blueprint(main_bp)  # /

#  Authentication: register, login, logout
from src.controllers.auth_controller import auth_bp
app.register_blueprint(auth_bp)  # /register, /login, /logout

#  Strategic Notification Engine: symbolic signal logging
from src.controllers.notification_controller import notification_bp
app.register_blueprint(notification_bp, url_prefix="/notify")

#  Role Type & Audio Guidance: role onboarding and identity evolution
from src.controllers.role_controller import role_bp
app.register_blueprint(role_bp, url_prefix="/role")

#  Insight Template System: reusable encoded messages
from src.controllers.template_controller import template_bp
app.register_blueprint(template_bp, url_prefix="/template")

#  Audio Narration Delivery: ElevenLabs MP3 streaming
from src.controllers.audio_controller import audio_bp
app.register_blueprint(audio_bp)  # /audio/<filename>

# -------------------------------------------------------------------------------
# Run the App (Development Server)
# -------------------------------------------------------------------------------
if __name__ == "__main__":
    print("[INFO] Starting Eyes Unclouded App at http://127.0.0.1:7777")
    app.run(port=7777, debug=True)
import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv

# -------------------------------------------------------------------------------
# Load environment variables from .env
# -------------------------------------------------------------------------------
load_dotenv()

# -------------------------------------------------------------------------------
# Flask App Initialization (template and static directories)
# -------------------------------------------------------------------------------
app = Flask(
    __name__,
    template_folder="src/views/templates",
    static_folder="src/views/static"
)

# -------------------------------------------------------------------------------
# Secure Session Key (used for signing cookies and sessions)
# -------------------------------------------------------------------------------
app.secret_key = os.getenv("SECRET_KEY")
if not app.secret_key:
    raise ValueError("[ERROR] SECRET_KEY missing from environment variables!")

# -------------------------------------------------------------------------------
# MongoDB Configuration via Flask-PyMongo
# -------------------------------------------------------------------------------
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

# -------------------------------------------------------------------------------
# Blueprint Registration – Modular Routes (MVC Structure)
# -------------------------------------------------------------------------------
# 1. Root Interface: splash, home, class reveal
from src.controllers.main_controller import main_bp
app.register_blueprint(main_bp)  # mounts at /

# 2. Authentication: register, login, logout
from src.controllers.auth_controller import auth_bp
app.register_blueprint(auth_bp)  # mounts at /register, /login, /logout

# 3. Strategic Notification Engine: send and view broadcasts
from src.controllers.notification_controller import notification_bp
# Use the blueprint's own prefix '/notifications'
app.register_blueprint(notification_bp)  # mounts at /notifications

# 4. Role Type & Audio Guidance: role selection and dashboard audio
from src.controllers.role_controller import role_bp
app.register_blueprint(role_bp, url_prefix="/role")

# 5. Insight Template System: reusable message templates
from src.controllers.template_controller import template_bp
app.register_blueprint(template_bp, url_prefix="/template")

# 6. Audio Narration Delivery: serve audio files
from src.controllers.audio_controller import audio_bp
app.register_blueprint(audio_bp)  # mounts at /audio/<filename>

# -------------------------------------------------------------------------------
# Run the application (development server)
# -------------------------------------------------------------------------------
if __name__ == "__main__":
    print("[INFO] Starting Eyes Unclouded App at http://127.0.0.1:7777")
    app.run(port=7777, debug=True)



