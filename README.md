# Hospital Management System (HMS)

A comprehensive Hospital Management System web application built with Django and SQLite (development) / MySQL (production).

## Features

- **14 Database Tables**: Department, Doctor, Patient, Staff, Nurse, Room, Appointment, Medical Record, Prescription, Medicine, Prescription Detail, Admission, Billing, Lab Test
- **Full CRUD Operations**: Create, Read, Update, Delete for all entities
- **Dashboard**: Real-time statistics and quick actions
- **Admin Panel**: Django admin interface for advanced management
- **Responsive Design**: Bootstrap 5 based responsive UI
- **Data Validation**: Field-level validation with regex patterns
- **Relationship Management**: Proper foreign key relationships with CASCADE, RESTRICT, and SET NULL

## Technology Stack

- **Backend**: Django 6.0.5
- **Database**: SQLite (development), MySQL (production)
- **Frontend**: Bootstrap 5.3.0, Bootstrap Icons
- **Python**: 3.12.3

## Project Structure

```
/home/abid-ullah/DB/
├── hms_project/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── hospital/             # Main application
│   ├── models.py         # 14 Django models
│   ├── views.py          # CRUD views
│   ├── forms.py          # Model forms
│   ├── urls.py           # URL patterns
│   ├── admin.py          # Admin configuration
│   ├── templates/        # HTML templates
│   └── management/       # Custom management commands
├── venv/                 # Virtual environment
├── manage.py
└── README.md
```

## Installation

### Prerequisites

- Python 3.12+
- pip

### Setup

1. **Clone/Download the project**
   ```bash
   cd /home/abid-ullah/DB
   ```

2. **Activate virtual environment**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django mysqlclient
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Load seed data** (optional)
   ```bash
   python manage.py load_csv_data
   ```

6. **Create superuser** (if not already created)
   ```bash
   python manage.py createsuperuser
   ```
   - Username: admin
   - Password: admin123

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main Application: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Database Configuration

### For Development (SQLite)

The project is configured to use SQLite by default. No additional configuration needed.

### For Production (MySQL)

To switch to MySQL:

1. Update `hms_project/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'hospital_db',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
           'OPTIONS': {
               'charset': 'utf8mb4',
               'init_command': "SET sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'",
           },
       }
   }
   ```

2. Create MySQL database:
   ```sql
   CREATE DATABASE hospital_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

## Models and Relationships

### Core Entities

1. **Department** - Hospital departments with head doctor assignment
2. **Doctor** - Medical staff with specialization and department
3. **Patient** - Patient records with medical history
4. **Staff** - Non-medical hospital staff
5. **Nurse** - Nursing staff (extends Staff)
6. **Room** - Hospital rooms with status and pricing
7. **Appointment** - Patient-doctor appointments
8. **MedicalRecord** - Clinical visit records
9. **Prescription** - Prescription headers
10. **Medicine** - Pharmacy inventory
11. **PrescriptionDetail** - Prescription-medicine mapping
12. **Admission** - Inpatient admission records
13. **Billing** - Patient invoices and payments
14. **LabTest** - Laboratory test orders and results

### Relationship Rules

- **CASCADE**: Patient records cascade to appointments, medical records, prescriptions, admissions, lab tests
- **RESTRICT**: Doctors, departments, rooms cannot be deleted if referenced
- **SET NULL**: Department head doctor, appointment references in medical records

## Dashboard Features

- **Statistics Cards**: Total patients, doctors, appointments, admissions, available rooms, pending bills, pending lab tests, total revenue
- **Quick Actions**: Add patient, schedule appointment, new admission, create bill
- **System Overview**: Database status, total records, server time
- **Quick Links**: Navigation to key modules

## Available Views

Each model has full CRUD operations:

- List View: Display all records with search and filters
- Detail View: View individual record details
- Create View: Add new records
- Update View: Edit existing records
- Delete View: Remove records with confirmation

## URL Patterns

- `/` - Dashboard
- `/departments/` - Department management
- `/doctors/` - Doctor management
- `/patients/` - Patient management
- `/staff/` - Staff management
- `/nurses/` - Nurse management
- `/rooms/` - Room management
- `/appointments/` - Appointment management
- `/medical-records/` - Medical record management
- `/prescriptions/` - Prescription management
- `/medicines/` - Medicine inventory
- `/prescription-details/` - Prescription detail management
- `/admissions/` - Admission management
- `/billing/` - Billing management
- `/lab-tests/` - Lab test management
- `/admin/` - Django admin panel

## Seed Data

The project includes CSV files with sample data for all tables:
- department.csv
- doctor.csv
- patient.csv
- staff.csv
- nurse.csv
- room.csv
- appointment.csv
- medical_record.csv
- medicine.csv
- prescription.csv
- prescription_detail.csv
- admission.csv
- billing.csv
- lab_test.csv

Load seed data using:
```bash
python manage.py load_csv_data
```

## Validation Rules

### Phone Numbers
- Must contain only digits
- Length: 7-15 characters

### Email
- Must contain @ symbol

### Dates
- Hire date must be on or after 2000-01-01
- Date of birth cannot be in the future
- Registration date cannot be before date of birth
- Visit date must be on or after 2000-01-01
- Expiry date cannot be before prescribed date
- Discharge date cannot be before admission date

### Numeric Values
- Stock quantity must be >= 0
- Unit price must be > 0
- Price per day must be > 0
- Duration days must be > 0
- Paid amount must be >= 0 and <= total amount

### Choice Fields
- Gender: Male, Female, Other
- Blood Type: A+, A-, B+, B-, O+, O-, AB+, AB-
- Room Type: General, Private, ICU, Semi-Private, Emergency
- Room Status: Available, Occupied, Maintenance
- Appointment Status: Scheduled, Completed, Cancelled, No-Show
- Prescription Status: Active, Dispensed, Expired
- Admission Status: Admitted, Discharged, Transferred
- Payment Status: Unpaid, Partial, Paid
- Payment Method: Cash, Card, Insurance, Online Transfer
- Lab Test Status: Pending, In Progress, Completed, Cancelled
- Nurse Shift: Morning, Evening, Night

## Development Notes

### Current Status

- ✅ All 14 models created with proper relationships
- ✅ Database migrations completed
- ✅ Admin panel configured
- ✅ Seed data loaded (100 patients, 40 doctors, 15 departments, etc.)
- ✅ CRUD views and forms created
- ✅ URL patterns configured
- ✅ Base template with Bootstrap 5
- ✅ Dashboard with statistics
- ✅ Patient templates (list, detail, form)
- ✅ Generic templates for reuse

### TODO

- Create specific templates for remaining models (doctor, department, etc.)
- Add search functionality to list views
- Implement pagination for large datasets
- Add export functionality (CSV, PDF)
- Implement user authentication and authorization
- Add audit logging
- Create reports and analytics
- Add email notifications
- Implement file upload for documents
- Add calendar view for appointments
- Create mobile-responsive improvements

## Troubleshooting

### MySQL Connection Issues

If you encounter MySQL connection errors:
1. Verify MySQL server is running: `sudo systemctl status mysql`
2. Check credentials in settings.py
3. Ensure database exists: `CREATE DATABASE hospital_db;`
4. For development, use SQLite (default configuration)

### Template Not Found Errors

If you encounter template not found errors:
1. Ensure templates directory exists: `hospital/templates/hospital/`
2. Check template names match view template_name attributes
3. Verify TEMPLATES setting in settings.py includes app directories

### Migration Errors

If migrations fail:
1. Delete database file (SQLite) or drop database (MySQL)
2. Run: `python manage.py migrate`
3. If issues persist: `python manage.py makemigrations --empty hospital`

## License

This project is for educational purposes.

## Contact

For issues or questions, please contact the development team.
