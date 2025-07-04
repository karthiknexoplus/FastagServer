# FASTag Parking Flask App

A modern, lightweight, and scalable Flask application for FASTag Parking with animated split-screen login/signup/logout pages, SQLite3 database, and rotational logging.

## Features
- Modern split-screen login, signup, and logout pages with animations
- Time-based greeting messages
- SQLite3 database (auto-created if not present)
- Rotational logging for all actions
- Scalable project structure
- Lightweight for EC2 free tier

## Setup
1. Clone the repository and navigate to the project directory.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. (Optional) Set your own secret key in a `.env` file:
   ```env
   SECRET_KEY=your_secret_key_here
   ```
5. Add your images and logo:
   - Place your logo as `app/static/images/logo.png`
   - Place login, signup, and logout images as `login_image.jpg`, `signup_image.jpg`, `logout_image.jpg` in `app/static/images/`
   - Place your favicon as `favicon.ico` in `app/static/images/`

## Run
```bash
python -m app
```

## Project Structure
- `app/` - Main application package
  - `static/` - Static files (CSS, JS, images)
  - `templates/` - HTML templates
  - `logs/` - Rotational log files
- `requirements.txt` - Python dependencies
- `README.md` - This file

---
**Note:** For best experience, use your own high-quality images and logo in the specified folders. 