# Mohd Rayyan — Portfolio Website

A creative, dev-style personal portfolio built with **Flask + Python**.

## Project Structure

```
portfolio/
├── app.py                  # Flask app + all portfolio data
├── requirements.txt
├── templates/
│   └── index.html          # Main Jinja2 template
└── static/
    ├── css/
    │   └── style.css       # Dark theme, animations, responsive
    └── js/
        └── main.js         # Cursor, typing effect, scroll reveal, filters
```

## Features

- Dark dev-style theme with dot-grid background
- Custom animated cursor with trailing effect
- Terminal-style hero section with typing animation
- Filterable project cards (ML, NLP, Cloud, Web)
- Scroll-reveal animations
- Responsive mobile layout
- REST API endpoints: `/api/projects`, `/api/profile`

## Run Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the Flask dev server
python app.py

# 3. Open in browser
# http://localhost:5000
```

## Deploy to Production

### Option A — Gunicorn (Linux/Mac)
```bash
pip install gunicorn
gunicorn -w 4 app:app
```

### Option B — Render / Railway (free hosting)
- Push to GitHub
- Connect repo to Render.com → New Web Service
- Start command: `gunicorn app:app`

### Option C — AWS EC2
```bash
sudo apt install python3-pip nginx
pip3 install flask gunicorn
gunicorn --bind 0.0.0.0:8000 app:app &
# Configure nginx as reverse proxy on port 80
```

## Customisation

All portfolio data (projects, skills, experience, certifications) lives
at the top of `app.py` in plain Python dicts — easy to update without
touching HTML.
