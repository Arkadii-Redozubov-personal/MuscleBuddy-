# Muscle Buddy

A web application for workout planning, exercise execution, and nutrition calculation built with Django.

## Features

- **Workout Generator**: Generates personalized training splits based on gender, experience level, and intensity.
- **Exercise Catalog**: Over 40 exercises with video demonstrations, form cues, and recommended sets/reps.
- **Nutrition Calculator**: Calculates daily calories and macronutrient targets based on fitness goals and activity level.
- **Useful Materials**: Curated training guides and educational video resources.

## Quick Start

### 1. Setup Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Initialize Database & Seed Data
```bash
python manage.py migrate
python manage.py loaddata fixtures/initial_data.json
```

### 3. Create Admin Account (Optional)
```bash
python manage.py createsuperuser
```

### 4. Run the Server
```bash
python manage.py runserver
```

Access the application at http://127.0.0.1:8000
Access the admin panel at http://127.0.0.1:8000/admin

## Tech Stack

- Python 3.11+, Django 5.1
- SQLite (Development) / PostgreSQL (Production)
- Bootstrap & Vanilla CSS
- WhiteNoise & Gunicorn