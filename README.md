# project_5
# Project Management System

## 📌 Overview 
This is a **Django-based Project Management System** that allows users to **create, update, delete, and manage projects**, send **messages**, and **recover passwords via email**. Can be accessed via: https://project-5-2bz7.onrender.com

## 🚀 Features
- **User Authentication** (Login, Signup, Password Reset)
- **Project Management** (CRUD operations)
- **Messaging System** (Send, Read, Archive Messages)
- **Role-Based Access Control** (Manager/Admin restrictions)
- **Forgot Password Email Recovery**

## 🛠️ Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/project_management.git
   cd project_management
   ```

2. **Create a Virtual Environment and Activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the App:**
   Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

## 🔑 Environment Variables
Create a `.env` file in the root directory and add:
```ini
SECRET_KEY='your_secret_key_here'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='your_email@gmail.com'
EMAIL_HOST_PASSWORD='your_password'
```

## 📜 Usage
### ✅ **Project Management**
- Create a project
- Edit project details
- Assign stakeholders
- Mark project status
- Delete projects

### ✅ **Messaging System**
- Send messages
- View inbox
- Archive messages

### ✅ **Authentication**
- Register/Login
- Password recovery via email
