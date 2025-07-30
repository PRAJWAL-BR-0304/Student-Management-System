# 🎓 Student Management System

A web-based role-based student management system built using Django. This system supports different panels for Admin, HOD, Staff, and Student users with complete authentication and dashboard features.

---

## ✨ Features

- 🔐 Role-based login (Admin, HOD, Staff, Student)
- 🖼️ Profile Picture support (ImageField)
- 📁 Modular Django app structure
- 📊 Dashboard and user actions
- 📦 Static and media file support
- 🛠️ Built-in admin panel

---

## 🛠️ Tech Stack

- Python 3.12+
- Django
- SQLite (Default)
- MySQL (Optional)
- Pillow for ImageField
- Supabase (optional for future expansion)

---

## 🧑‍💻 Installation

### Clone the Repository

**Using HTTPS:**
```bash
git clone https://github.com/PRAJWAL-BR-0304/Student-Management-System.git
cd Student-Management-System/student_management_system
```
Using GitHub CLI:
```
gh repo clone PRAJWAL-BR-0304/Student-Management-System
cd Student-Management-System/student_management_system
```
Set up the Virtual Environment:
```
python -m venv .venv
```
Activate the Virtual Environment
PowerShell (Windows):
```
.\.venv\Scripts\activate
```
CMD (Windows):
```
.venv\Scripts\activate.bat
```
Install Dependencies
```
pip install django django-active-link Pillow
```
Run Migrations
```
python manage.py migrate
```
Start the Server
```
python manage.py runserver
```
📁 Project Structure
```
Student-Management-System/
├── student_management_system/
│   ├── app/
│   ├── templates/
│   ├── static/
│   ├── media/
│   ├── manage.py
│   └── ...
├── README.md
└── requirements.txt
```
🐛 Troubleshooting
ModuleNotFoundError: No module named 'active_link'
```
pip install django-active-link
```
ImageField Error (Pillow not installed)
```
pip install Pillow
```
Static Files Not Loading (e.g., Bootstrap 404)
```
python manage.py collectstatic
```
📝 Development Guidelines
Code Style
Follow PEP8

Use Django’s best practices for views, models, and templates

Keep apps modular and reusable

Use environment variables for secrets (in .env)

Commit Messages (Conventional Commits)
feat: for new features

fix: for bug fixes

docs: for documentation

style: for styling only

refactor: for code refactoring

test: for test-related changes

chore: for maintenance tasks

🧪 Testing
To test the application manually:

Run the dev server

Log in using the default credentials

Navigate through all dashboards

Test features like student creation, leave approval, etc.

🌐 Deployment
To deploy the application:

Set ALLOWED_HOSTS in settings.py

Collect static files:
```
python manage.py collectstatic
```
Deploy using:

Gunicorn + Nginx (Linux)

Heroku

Render

Railway

PythonAnywhere

🤝 Contributing
Fork the repository

Create your feature branch

Commit your changes

Push to your branch

Open a Pull Request

🔒 Security
Custom user model with permission-based routing

CSRF protection enabled

Static/media file protection in production

Passwords are hashed securely using Django’s authentication system

🙏 Acknowledgments
Django

Pillow

Bootstrap

Supabase (for future optional integrations)

MetaMask (for reference in Web3-related modules)

🗺️ Roadmap
Add notification system

Integrate email alerts

Enhance dashboard analytics

Add REST API endpoints

Optional mobile app (React Native)

📧 Contact
Created by Prajwal B R
📬 Email: prajwalbr0304@gmail.com


