# Hospital Management System

A Django-based Hospital Management System that helps hospitals maintain and manipulate patient and doctor data efficiently.

## Project Overview

This application provides a comprehensive solution for managing hospital operations including patient information, doctor profiles, and user authentication. It features a REST API for data management and a web interface for easy access.

## Features

- **Patient Management**: Add, view, and manage patient records with details like name, age, contact information, and address
- **Doctor Management**: Manage doctor profiles including specialization, contact details, and credentials
- **User Authentication**: Secure login system for hospital staff
- **REST API**: RESTful API endpoints for programmatic access to patient data
- **Web Interface**: User-friendly templates for data visualization and entry

## Project Structure

```
hospital_management_system/
├── hms/                          # Main app directory
│   ├── models.py                 # Patient and Doctor models
│   ├── views.py                  # API views and page views
│   ├── serializers.py            # DRF serializers
│   ├── urls.py                   # URL routing
│   ├── migrations/               # Database migrations
│   └── admin.py                  # Django admin configuration
├── hospital_management_system/   # Project settings
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Project URL configuration
│   └── wsgi.py                   # WSGI configuration
├── templates/                    # HTML templates
│   ├── login.html                # Login page
│   ├── patient_info.html         # Patient information form
│   └── patient_details.html      # Patient details display
├── static/                       # CSS and static files
│   ├── style.css
│   ├── login.css
│   └── patient_details.css
├── db.sqlite3                    # SQLite database
└── manage.py                     # Django management script
```

## Technologies Used

- **Django 6.0.1**: Web framework
- **Django REST Framework 3.16.1**: REST API toolkit
- **Python 3**: Programming language
- **SQLite**: Database
- **HTML/CSS**: Frontend interface

## Models

### Patient
- `full_name`: Character field (max 200 chars)
- `age`: Integer field
- `phone_number`: Integer field
- `address`: Text field

### Doctor
- `name`: Character field (max 200 chars)
- `userid`: Integer field
- `password`: Character field (max 200 chars)
- `specialization`: Character field (max 200 chars)
- `phone_number`: Integer field
- `address`: Text field

## API Endpoints

- **POST /api/patientinfo/**: Create new patient record
- **GET /api/patientinfo/**: Get patient information form
- **GET /api/patientdetails/**: Retrieve all patients (JSON)
- **GET /patientdetails/**: View all patients (HTML page)
- **POST /login/**: User authentication

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Hospital_management_system.git
   cd Hospital_management_system
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv hms_env
   # On Windows
   hms_env\Scripts\activate
   # On macOS/Linux
   source hms_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Web Interface: `http://localhost:8000`
   - Admin Panel: `http://localhost:8000/admin`
   - API: `http://localhost:8000/api/patientdetails/`

## Usage

### Adding a Patient
1. Navigate to the patient information page
2. Fill in the required details (name, age, phone, address)
3. Submit the form to save the patient record

### Viewing Patients
1. Go to the patient details page to view all registered patients
2. Use the login system to access protected areas

### API Usage

**Get all patients:**
```bash
curl http://localhost:8000/api/patientdetails/
```

**Add new patient:**
```bash
curl -X POST http://localhost:8000/api/patientinfo/ \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "John Doe",
    "age": 30,
    "phone_number": 1234567890,
    "address": "123 Main St"
  }'
```

## Authentication

The system uses Django's built-in authentication system. Users must log in with valid credentials to access certain pages.

## Future Enhancements

- Appointment scheduling system
- Medical records management
- Prescription tracking
- Patient-Doctor assignment
- Email notifications
- Advanced reporting features

## License

This project is open source and available under the MIT License.

## Contact & Support

For issues, questions, or suggestions, please create an issue in the repository.
