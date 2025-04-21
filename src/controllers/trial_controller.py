# ==============================================================================
# File: trial_controller.py
# Description: Handles the emotion trial gallery and observation interface
# ==============================================================================

import os
import random
from flask import Blueprint, render_template

trial_bp = Blueprint('trial', __name__)
EXPRESSIONS_DIR = os.path.join('src', 'views', 'static', 'images', 'expressions')

@trial_bp.route('/observe-trial')
def show_trial_gallery():
    all_images = os.listdir(EXPRESSIONS_DIR)
    image_files = random.sample(all_images, min(6, len(all_images)))  # show 6 random images
    return render_template('observe_trial.html', images=image_files)
