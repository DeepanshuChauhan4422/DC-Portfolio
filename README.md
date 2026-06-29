# Premium AI Portfolio Website for Deepanshu Chauhan

This repository contains a **production-ready, fully responsive, and visually stunning** developer portfolio website for **Deepanshu Chauhan**. It features a modern dark-theme glassmorphism user interface with moving background aurora glows, orbiting tech items, real-time GitHub integration, and a floating interactive **AI Portfolio Assistant** chatbot powered by Django and the **Gemini API**.

Strictly following the project constraints, this application is built using **Python and Django** for the backend, and **Vanilla HTML5, CSS3, and JavaScript** for the frontend—without the use of React, Next.js, Tailwind CSS, or Bootstrap templates.

---

## Key Features

- **Dark Aurora Glassmorphism UI**: Premium visual aesthetics incorporating deep radial gradients, blurred background structures, custom cursors, typing headers, and smooth micro-animations.
- **AI Portfolio Assistant**: A floating chat widget in the bottom right corner allowing visitors to talk directly to an AI representing Deepanshu. It uses the Gemini API (fallback to OpenAI or keyword-matching offline classifier if API keys are not supplied).
- **Dynamic GitHub Widget**: Real-time integration displaying Deepanshu's profile details, pinned repositories, language tags, and an embedded contribution chart.
- **Featured Projects & Screenshots**: Interactive detail cards displaying comprehensive descriptions, screenshot galleries, challenges faced, future improvements, architecture diagrams, and links.
- **Django Admin Console**: A structured management dashboard to easily add, modify, or delete skills, projects, certifications, achievements, and review incoming contact messages.
- **Robust AJAX Contact Form**: Submits messages in the background, validates emails, and shows beautiful animated floating toast notifications.
- **SEO & Production Optimized**: Includes dynamic `sitemap.xml`, proper `robots.txt`, custom favicons, semantic HTML elements, Open Graph (OG) meta tags, and WhiteNoise static compression.

---

## Tech Stack

- **Backend**: Python 3.11+, Django 5.x/6.x, python-dotenv
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6)
- **Database**: SQLite (default for development; easily swappable to PostgreSQL/MySQL via `.env`)
- **Third-Party Integrations**: Google Gemini API (`google-generativeai`), OpenAI API, FontAwesome 6, Devicon, ghchart.rshah.org
- **DevOps/Deployment**: Docker, Docker Compose, Gunicorn, WhiteNoise

---

## Local Setup & Installation

### Prerequisites
Make sure you have Python 3.11+ installed.

### 1. Set Up Virtual Environment & Dependencies
Open your shell inside the project root and run:
```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment (Windows Powershell)
.\venv\Scripts\Activate.ps1

# Activate virtual environment (macOS/Linux)
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 2. Configure Environment Variables (`.env`)
Create a `.env` file in the root directory (a default template is provided):
```env
DEBUG=True
SECRET_KEY=django-insecure-development-key-deepanshu-portfolio
ALLOWED_HOSTS=localhost,127.0.0.1
GITHUB_USERNAME=DeepanshuChauhan4422

# AI Configuration (Optional: chat widget falls back to keyword classifier if empty)
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Run Migrations & Seed Database
Build the database tables and automatically populate them with Deepanshu's skills, experience, projects, certifications, and achievements:
```bash
# Create database files
python manage.py makemigrations
python manage.py migrate

# Seed data automatically
python manage.py seed_portfolio
```

### 4. Admin Credentials
The seeding phase automatically creates a default superuser account for the Django Admin Panel:
- **URL**: `http://127.0.0.1:8000/admin/`
- **Username**: `admin`
- **Password**: `adminpassword`
*(Note: Please modify this password immediately upon deployment).*

### 5. Launch the Server
Start the local development server:
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## Run Unit Tests
To run the automated test suite checking models, views, API responses, and fallbacks:
```bash
python manage.py test
```

---

## Running with Docker

You can launch the entire application, including automatic database migrations and static file compilation, with Docker:

```bash
# Build and start the containers
docker-compose up --build
```
Access the website at `http://localhost:8000/`. To run in the background, append the `-d` flag.
