@"

# Eyes Unclouded App – Project Summary

**Author**: Khaylub Thompson-Calvin  
**Date**: April 17, 2025  
**Course**: CIS 234A – Real World Programming  
**Project**: Eyes Unclouded App – Sprint 1

---

## 🧠 Overview

_Eyes Unclouded App_ is an interactive Flask + MongoDB system designed for:

- Behavioral perception training
- Emotional awareness logging
- Strategic symbolic messaging
- Role-based onboarding (Seeker, Strategist, Mentor, etc.)

Inspired by legacy-based teaching, the system merges cognitive mastery with a visually immersive UI, preparing the foundation for a deeper reincarnation modeling engine.

---

## 🔐 Key Features

- 🧬 Role Type Registration & Dynamic Audio Onboarding
- 🛡️ Secure Login w/ Hashed Passwords (Werkzeug)
- 🧠 Flash messaging & session tracking
- 📡 Strategic Signal Logging w/ Virtue & Emotion Tags
- 🕰️ Date-filtered Insight Archive
- 🎙️ Audio Engine w/ ElevenLabs Role Narration
- 🧩 Modular Blueprint Routing (MVC)

---

## 🔧 Technologies

- **Python 3.11+**
- **Flask** (Jinja2, Blueprints, Sessions)
- **MongoDB Atlas** + MongoDB Compass (local testing)
- **HTML5 / CSS3** (custom theme, dark UI)
- **JavaScript** (for audio & form logic)
- **dotenv** for secure environment variable management

---

## 📁 Project Folder Structure

\`\`\`
Assignment1/
├── app.py # Central app registrar
├── run.py # Dev server runner
├── .env # Local secrets (not committed)
├── .env.template # Safe environment structure for collaborators
├── src/
│ ├── controllers/ # Route Blueprints
│ └── views/
│ ├── templates/ # Jinja2 Pages (Splash, Register, Role, etc.)
│ └── static/
│ ├── css/
│ ├── js/
│ ├── images/
│ └── audio/
├── data/ # Mentor insights, seed data (JSON)
├── docs/ # Diagrams, flowcharts
└── tests/ # Functional test cases
\`\`\`

---

## 🔄 Setup Instructions

1. **Clone this repository**

\`\`\`bash
git clone https://github.com/YourUsername/EyesUncloudedApp.git
cd EyesUncloudedApp/Assignment1
\`\`\`

2. **Create the environment file**

\`\`\`bash
cp .env.template .env
\`\`\`

3. **Edit \`.env\` and add your secrets**

\`\`\`env
SECRET_KEY=your-secure-key
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.xsknu.mongodb.net/eyes_unclouded
\`\`\`

4. **Install dependencies**

\`\`\`bash
pip install -r requirements.txt
\`\`\`

5. **Run the app**

\`\`\`bash
python run.py
\`\`\`

---

## 🔭 What's Coming Next

- 🌐 Remote class-reveal system based on perception score
- 📊 Insight Chain visualizer with reincarnation modeling
- 🧠 SQL-based microexpression tracker
- 💠 Legacy Vault unlocking logic (wisdom engine + perception milestones)
- 🎧 Mentor Mode with strategic voice reflections

---

## 🛡️ Security Notes

- \`.env\` is ignored in \`.gitignore\`
- \`.env.template\` is safe to commit
- Mongo Atlas URI uses dedicated user w/ scoped permissions

---

## ✍️ Credits & Philosophy

This app is part of a greater symbolic narrative & legacy design — integrating myth, strategy, and emotional intelligence into a software artifact meant for future generations.

> “”  
> — _Eyes Unclouded_
> "@ | Set-Content "README.md"
