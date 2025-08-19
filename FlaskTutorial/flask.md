# Self-study with Python flask Web Apps
Here are my web projects I did with Flask and SQLAlchemy.
- food_webapp
- member_api

# Use python Virtual Environment
Ensure you have Python 3
```
python3 --version
```
## Create and activate a virtual env
From your project folder:
```
python3 -m venv .venv
source .venv/bin/activate
```
Your prompt should now show (.venv)
## Upgrade tooling and install Flask
```
python -m pip install --upgrade pip setuptools wheel
pip install Flask
```
## Run the App

Option 1 — run directly:
```
python app.py
```
Option 2 — using Flask CLI:
```
flask run
```
Visit: http://127.0.0.1:5000

---
# Install Miniforge

If you don’t have Miniforge yet:

## via Homebrew
```
brew install miniforge
```
Restart your terminal and confirm:
```
conda --version
```
## Create & Activate a Virtual Environment

Pick a Python version (e.g., 3.9):
```
conda create -n flask-env python=3.9 -y
conda activate flask-env

```
Check:
```
which python
python --version
```
# Install Flask

Inside the environment:
```
pip install Flask
```
Optional (for .env files or DB tools):
```
pip install python-dotenv Flask-SQLAlchemy
```
## Run the App

Option 1 — run directly:
```
python app.py
```
Option 2 — using Flask CLI:
```
flask run
```
Visit: http://127.0.0.1:5000

# Troubleshooting
## Port already in use
```
lsof -i :5000
kill -9 <PID>
```
Or switch to another port.
## Wrong Python
Ensure which python points inside flask-env.
- No module named Flask:
```
pip install Flask
```