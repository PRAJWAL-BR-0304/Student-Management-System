# 🎓 Student Management System

A web-based student management system built using Django. This system supports role-based authentication and features distinct dashboards for Admin, HOD, Staff, and Student users.

---

## 🔗 GitHub Repository

[Student-Management-System](https://github.com/PRAJWAL-BR-0304/Student-Management-System)

---

## 🚀 Features

- 🔐 Role-based login system:
  - Admin Panel
  - HOD Panel
  - Staff Panel
  - Student Panel
- 📂 Profile Picture support (ImageField)
- 🧩 Modular Django App structure
- 📦 Static files and templates
- 🛠 Admin panel for management

---

## 📁 Project Setup Instructions

### 🔧 Requirements

- Python 3.12+
- Git
- Virtualenv (recommended)
- VS Code or any IDE

### ⚙️ Installation Steps

1. Clone the repository

git clone https://github.com/PRAJWAL-BR-0304/Student-Management-System.git

css
Copy
Edit

2. Navigate to the project directory

cd Student-Management-System/student_management_system

cpp
Copy
Edit

3. Create a virtual environment

python -m venv .venv

r
Copy
Edit

4. Activate the virtual environment

- PowerShell:
  ```
  .\.venv\Scripts\activate
  ```
- Command Prompt:
  ```
  .venv\Scripts\activate.bat
  ```

5. Install required packages

pip install django django-active-link Pillow

markdown
Copy
Edit

6. Apply database migrations

python manage.py migrate

markdown
Copy
Edit

7. Run the development server

python manage.py runserver

yaml
Copy
Edit

8. Open in browser

Navigate to http://127.0.0.1:8000

---

## 🔐 Default Login Credentials

| Role     | Email                         | Password  | Panel         |
|----------|-------------------------------|-----------|---------------|
| Admin    | admin                         | admin123  | Admin Panel   |
| HOD      | prajwalbr0304@gmail.com       | admin123  | HOD Panel     |
| Staff    | staff@gmail.com               | 12345     | Staff Panel   |
| Student  | prathamuk@gmail.com           | 12345     | Student Panel |

---

## 🐛 Troubleshooting

- **Missing `active_link` Module**

Install using:
pip install django-active-link

markdown
Copy
Edit

- **ImageField Pillow Error**

Install Pillow:
pip install Pillow

sql
Copy
Edit

- **Static File 404 Errors**

If needed, collect static files:
python manage.py collectstatic

yaml
Copy
Edit

---

## 🛠 Optional: MySQL Setup

If you're switching from SQLite to MySQL, update `settings.py` and run:
ALTER USER 'root'@'localhost' IDENTIFIED BY 'root123';

yaml
Copy
Edit

---

## 📦 Folder Structure

Student-Management-System/
├── student_management_system/
│ ├── app/
│ ├── templates/
│ ├── static/
│ ├── manage.py
│ └── ...
└── README.md

yaml
Copy
Edit

---

## 📧 Contact

Created by **Prajwal B R**  
📩 Email: prajwalbr0304@gmail.com

---

## 🪪 License

This project is licensed under the MIT License.
