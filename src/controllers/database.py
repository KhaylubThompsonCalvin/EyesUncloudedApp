# ==============================================================================
# File: database.py
# Course: CIS 234A – Real World Programming
# Project: Eyes Unclouded App – Behavioral Engine
# Author: Khaylub Thompson-Calvin
# Date: 04/17/2025
# ==============================================================================
# Description:
#   This module establishes a secure connection to the Eyes Unclouded MongoDB
#   database using credentials from the environment. It exposes named accessors
#   for core behavioral collections:
#
#   • user_profiles: Identity and legacy state
#   • notifications: Perception broadcasts and emotion-tagged insights
#   • templates: Symbolic narrative structures and reusable signal formats
#
#   This script acts as the entry point for the Oracle Layer of the app.
# ==============================================================================

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# ------------------------------------------------------------------------------
# Load Credentials from .env File
# ------------------------------------------------------------------------------
load_dotenv()

# ------------------------------------------------------------------------------
# Connect to the Eyes Unclouded MongoDB Cluster
# ------------------------------------------------------------------------------
client = MongoClient(os.getenv("MONGO_URI"))
db = client.get_default_database()  # Uses the default DB from connection string

# ------------------------------------------------------------------------------
# Collection Accessors – Modular, Readable, Extendable
# ------------------------------------------------------------------------------
def get_user_profiles():
    """
    Return the MongoDB collection storing user profiles.
    Contains fields like:
      - username, email, role_type
      - perception_score, virtue_affinity
      - class_name, learning_level, etc.
    """
    return db["user_profiles"]

def get_notifications():
    """
    Return the collection of submitted perception signals.
    Used for behavioral journaling, insight logging, and emotion tracking.
    """
    return db["notifications"]

def get_templates():
    """
    Return the collection of user-created templates.
    Templates define reusable message formats with attachments.
    """
    return db["templates"]

# ------------------------------------------------------------------------------
# Optional Future Hook:
# Add get_collection(name: str) for generic dynamic access
# ------------------------------------------------------------------------------
# def get_collection(name: str):
#     """Generic collection getter for future dynamic utilities."""
#     return db[name]


