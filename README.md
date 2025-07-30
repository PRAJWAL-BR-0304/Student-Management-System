# 🎓 Student Management System - Role-Based Academic Portal

A robust Django-based web application for managing users and operations within an educational institution. It includes role-based access for Admin, HOD, Staff, and Students — each with a dedicated dashboard and set of functionalities.

---

## ✨ Features

### 🔐 Role-Based Authentication
- Separate login panels for Admin, HOD, Staff, and Students  
- Custom user model with profile pictures  
- Session-based authentication  

### 🏫 Academic Management
- HOD and Staff dashboards with student details  
- Add/update/delete student and staff records  
- Department and subject management  
- Attendance and leave tracking system  

### 📊 Admin Dashboard
- Full access to all data  
- Create HOD, Staff, and Student accounts  
- Approve leaves and monitor activities  

### 🎓 Student Panel
- View personal profile  
- Attendance tracking  
- View academic reports and notices  

### 📁 File Management
- Image upload (via Pillow) for profile pictures  
- Static and media file configuration  

---

## 🛠️ Tech Stack

### Backend
- Django 5.1.4  
- Python 3.12  
- SQLite (default) or MySQL (optional)  

### Frontend
- HTML5, CSS3  
- Bootstrap  
- JavaScript  

### Other Packages
- Pillow  
- django-active-link  

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.12+  
- Git  
- Virtualenv (optional but recommended)  
- VS Code or any IDE  

---

### 🧑‍💻 Installation

#### Clone the Repository

**Using HTTPS:**
```bash
git clone https://github.com/PRAJWAL-BR-0304/Student-Management-System.git
cd Student-Management-System/student_management_system

Using GitHub CLI:

bash
Copy
Edit
gh repo clone PRAJWAL-BR-0304/Student-Management-System
cd Student-Management-System/student_management_system
Set up the Virtual Environment
bash
Copy
Edit
python -m venv .venv
Activate the virtual environment:

PowerShell:

bash
Copy
Edit
.\.venv\Scripts\activate
CMD:

bash
Copy
Edit
.venv\Scripts\activate.bat
Install Dependencies
bash
Copy
Edit
pip install django django-active-link Pillow
Run Migrations
bash
Copy
Edit
python manage.py migrate
Start the Server
bash
Copy
Edit
python manage.py runserver
Now open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:8000
🔐 Default Login Credentials
Role	Email	Password	Panel
Admin	admin	admin123	Admin Panel
HOD	prajwalbr0304@gmail.com	admin123	HOD Panel
Staff	staff@gmail.com	12345	Staff Panel
Student	prathamuk@gmail.com	12345	Student Panel

📁 Project Structure
arduino
Copy
Edit
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
🛠 Optional: MySQL Setup
If you're using MySQL instead of SQLite:

sql
Copy
Edit
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root123';
Then update DATABASES in settings.py accordingly.

🐛 Troubleshooting
ModuleNotFoundError: No module named 'active_link'

bash
Copy
Edit
pip install django-active-link
ImageField Error (Pillow not installed)

bash
Copy
Edit
pip install Pillow
Static Files Not Loading (e.g. Bootstrap 404)

bash
Copy
Edit
python manage.py collectstatic
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

Log in using test credentials

Navigate through dashboards and test features like student creation, leave approval, etc.

🌐 Deployment
To deploy:

Configure ALLOWED_HOSTS in settings.py

Collect static files:

bash
Copy
Edit
python manage.py collectstatic
Use Gunicorn + Nginx (Linux) or deploy on Heroku, Render, Railway, etc.

🤝 Contributing
Fork the repository

Create your feature branch

Commit your changes

Push to your branch

Open a Pull Request

🔒 Security
Custom user model with permission-based routing

CSRF protection enabled by default

Static and media file protection in production

User passwords hashed securely

🙏 Acknowledgments
Django

Pillow

MetaMask (for reference in other projects)

Bootstrap

Supabase (optional future integration)

🗺️ Roadmap
Add notification system

Integrate email alerts

Enhance dashboard analytics

Add REST API endpoints

Optional mobile app interface (React Native)

yaml
Copy
Edit

---

Let me know if you'd like me to also generate a `requirements.txt` or `.env.example`, or even help publish this directly to
