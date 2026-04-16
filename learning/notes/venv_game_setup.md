# 🎮 Python Game Setup Notes (venv + Pygame + Git)

## 🧪 Virtual Environment (venv)

### Why we use it:
- Keeps project dependencies separate
- Prevents system Python issues
- Required for installing pygame safely

### Setup:
1. Create venv:
   python3 -m venv venv

2. Activate venv:
   source venv/bin/activate

3. Deactivate venv:
   deactivate

---

## 📦 Installing Pygame

Inside venv ONLY:
pip install pygame

If not using venv, system may block installs.

---

## 🚫 IMPORTANT: NEVER push venv to GitHub

Add this to .gitignore:
venv/
__pycache__/
*.pyc

---

## 🎮 Running a Pygame Game

python3 learning/python/space_game.py

---

## 🚀 Git Workflow

1. git add .
2. git commit -m "message"
3. git push origin main

---

## 🧠 Common Issues

### pip not found
→ Install python3-pip

### externally-managed-environment
→ Use venv

### pygame not found
→ Install inside venv

---

## 🎯 Summary
- venv = environment setup
- pygame = game engine
- git = version control + submission
