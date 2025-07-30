🎓 Student Management System
A Django-based web application to manage academic roles such as HOD, Staff, and Students. Built for ease of use in educational institutions to track and manage user roles, academic data, and permissions through different panels.

🔗 GitHub Repository
GitHub - PRAJWAL-BR-0304/Student-Management-System

✅ Features
🔐 Role-based authentication (Admin, HOD, Staff, Student)

📋 Dashboard panels:

Admin Panel

HOD Panel

Staff Panel

Student Panel

🖼 User profile management (with image upload)

📦 Static files and templates integration

📊 Admin interface for data control

🧰 Tech Stack
Backend: Django 5.1.4

Frontend: HTML, CSS, Bootstrap

Database: Default SQLite (or MySQL configurable)

Environment: Python 3.12, Virtualenv

💻 Installation Guide
Clone the repo

bash
Copy
Edit
git clone https://github.com/PRAJWAL-BR-0304/Student-Management-System.git
Navigate to project

bash
Copy
Edit
cd Student-Management-System/student_management_system
Create a virtual environment

bash
Copy
Edit
python -m venv .venv
Activate the virtual environment

PowerShell:

bash
Copy
Edit
.\.venv\Scripts\activate
Command Prompt:

bash
Copy
Edit
.venv\Scripts\activate.bat
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Or manually install:

bash
Copy
Edit
pip install django django-active-link Pillow
Apply migrations

bash
Copy
Edit
python manage.py migrate
Run the server

bash
Copy
Edit
python manage.py runserver
Access
Open your browser and go to: http://127.0.0.1:8000

🔐 Default Logins
Role	Email	Password	Panel
Admin	admin	admin123	Admin Panel
HOD	prajwalbr0304@gmail.com	admin123	HOD Panel
Staff	staff@gmail.com	12345	Staff Panel
Student	prathamuk@gmail.com	12345	Student Panel

⚠️ Troubleshooting
ModuleNotFoundError: No module named 'active_link'

bash
Copy
Edit
pip install django-active-link
ImageField Error / Pillow Missing

bash
Copy
Edit
pip install Pillow
Static Files Missing (e.g. bootstrap.bundle.min.js 404)

Check if static files are correctly linked and collected

Run: python manage.py collectstatic (if DEBUG=False in production)

🛠 MySQL Setup (Optional)
If switching to MySQL:

sql
Copy
Edit
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root123';
Update DATABASES in settings.py accordingly.

📂 Folder Structure
sql
Copy
Edit
Student-Management-System/
├── student_management_system/
│   ├── manage.py
│   ├── student_management_system/
│   ├── app/
│   ├── templates/
│   ├── static/
│   └── ...
└── README.md
📧 Contact
Created by Prajwal B R

📄 License
This project is licensed under the MIT License - feel free to modify and use.


