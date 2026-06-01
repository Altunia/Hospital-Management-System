import csv
import os
from django.core.management.base import BaseCommand
from django.db import transaction
from datetime import datetime
from hospital.models import (
    Department, Doctor, Patient, Staff, Nurse, Room,
    Appointment, MedicalRecord, Prescription, Medicine,
    PrescriptionDetail, Admission, Billing, LabTest
)


class Command(BaseCommand):
    help = 'Load seed data from CSV files'

    def handle(self, *args, **kwargs):
        base_path = '/home/abid-ullah/DB'
        
        with transaction.atomic():
            self.load_departments(base_path)
            self.load_doctors(base_path)
            self.update_department_heads(base_path)
            self.load_patients(base_path)
            self.load_staff(base_path)
            self.load_nurses(base_path)
            self.load_rooms(base_path)
            self.load_appointments(base_path)
            self.load_medical_records(base_path)
            self.load_medicines(base_path)
            self.load_prescriptions(base_path)
            self.load_prescription_details(base_path)
            self.load_admissions(base_path)
            self.load_billing(base_path)
            self.load_lab_tests(base_path)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded all CSV data'))

    def load_departments(self, base_path):
        with open(os.path.join(base_path, 'department.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Department.objects.create(
                    department_id=int(row['department_id']),
                    department_name=row['department_name'],
                    location=row['location'],
                    phone=row['phone'] if row['phone'] else None
                )
        self.stdout.write('Loaded Departments')

    def update_department_heads(self, base_path):
        with open(os.path.join(base_path, 'department.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['head_doctor_id']:
                    dept = Department.objects.get(department_id=int(row['department_id']))
                    dept.head_doctor_id = Doctor.objects.get(doctor_id=int(row['head_doctor_id']))
                    dept.save()
        self.stdout.write('Updated Department Heads')

    def load_doctors(self, base_path):
        with open(os.path.join(base_path, 'doctor.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Doctor.objects.create(
                    doctor_id=int(row['doctor_id']),
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    specialization=row['specialization'],
                    phone=row['phone'],
                    email=row['email'] if row['email'] else None,
                    department_id=int(row['department_id']),
                    hire_date=datetime.strptime(row['hire_date'], '%Y-%m-%d').date(),
                    license_number=row['license_number']
                )
        self.stdout.write('Loaded Doctors')

    def load_patients(self, base_path):
        with open(os.path.join(base_path, 'patient.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Patient.objects.create(
                    patient_id=int(row['patient_id']),
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    date_of_birth=datetime.strptime(row['date_of_birth'], '%Y-%m-%d').date(),
                    gender=row['gender'],
                    blood_type=row['blood_type'] if row['blood_type'] else None,
                    phone=row['phone'],
                    email=row['email'] if row['email'] else None,
                    address=row['address'] if row['address'] else None,
                    registration_date=datetime.strptime(row['registration_date'], '%Y-%m-%d').date()
                )
        self.stdout.write('Loaded Patients')

    def load_staff(self, base_path):
        with open(os.path.join(base_path, 'staff.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Staff.objects.create(
                    staff_id=int(row['staff_id']),
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    role=row['role'],
                    department_id=int(row['department_id']),
                    phone=row['phone'],
                    email=row['email'] if row['email'] else None,
                    hire_date=datetime.strptime(row['hire_date'], '%Y-%m-%d').date()
                )
        self.stdout.write('Loaded Staff')

    def load_nurses(self, base_path):
        with open(os.path.join(base_path, 'nurse.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Nurse.objects.create(
                    nurse_id=int(row['nurse_id']),
                    staff_id=int(row['staff_id']),
                    shift=row['shift'],
                    department_id=int(row['department_id']),
                    certification=row['certification'] if row['certification'] else None
                )
        self.stdout.write('Loaded Nurses')

    def load_rooms(self, base_path):
        with open(os.path.join(base_path, 'room.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Room.objects.create(
                    room_id=int(row['room_id']),
                    room_number=row['room_number'],
                    room_type=row['room_type'],
                    department_id=int(row['department_id']),
                    status=row['status'],
                    price_per_day=float(row['price_per_day'])
                )
        self.stdout.write('Loaded Rooms')

    def load_appointments(self, base_path):
        with open(os.path.join(base_path, 'appointment.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Appointment.objects.create(
                    appointment_id=int(row['appointment_id']),
                    patient_id=int(row['patient_id']),
                    doctor_id=int(row['doctor_id']),
                    appointment_date=datetime.strptime(row['appointment_date'], '%Y-%m-%d %H:%M:%S'),
                    status=row['status'],
                    reason=row['reason'] if row['reason'] else None,
                    notes=row['notes'] if row['notes'] else None
                )
        self.stdout.write('Loaded Appointments')

    def load_medical_records(self, base_path):
        with open(os.path.join(base_path, 'medical_record.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                MedicalRecord.objects.create(
                    record_id=int(row['record_id']),
                    patient_id=int(row['patient_id']),
                    doctor_id=int(row['doctor_id']),
                    visit_date=datetime.strptime(row['visit_date'], '%Y-%m-%d').date(),
                    diagnosis=row['diagnosis'],
                    treatment=row['treatment'] if row['treatment'] else None,
                    notes=row['notes'] if row['notes'] else None,
                    appointment_id=int(row['appointment_id']) if row['appointment_id'] else None
                )
        self.stdout.write('Loaded Medical Records')

    def load_medicines(self, base_path):
        with open(os.path.join(base_path, 'medicine.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Medicine.objects.create(
                    medicine_id=int(row['medicine_id']),
                    medicine_name=row['medicine_name'],
                    generic_name=row['generic_name'],
                    category=row['category'],
                    manufacturer=row['manufacturer'] if row['manufacturer'] else None,
                    stock_quantity=int(row['stock_quantity']),
                    unit_price=float(row['unit_price'])
                )
        self.stdout.write('Loaded Medicines')

    def load_prescriptions(self, base_path):
        with open(os.path.join(base_path, 'prescription.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Prescription.objects.create(
                    prescription_id=int(row['prescription_id']),
                    record_id=int(row['record_id']),
                    patient_id=int(row['patient_id']),
                    prescribed_date=datetime.strptime(row['prescribed_date'], '%Y-%m-%d').date(),
                    expiry_date=datetime.strptime(row['expiry_date'], '%Y-%m-%d').date() if row['expiry_date'] else None,
                    status=row['status']
                )
        self.stdout.write('Loaded Prescriptions')

    def load_prescription_details(self, base_path):
        with open(os.path.join(base_path, 'prescription_detail.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                PrescriptionDetail.objects.create(
                    detail_id=int(row['detail_id']),
                    prescription_id=int(row['prescription_id']),
                    medicine_id=int(row['medicine_id']),
                    dosage=row['dosage'],
                    frequency=row['frequency'],
                    duration_days=int(row['duration_days']),
                    instructions=row['instructions'] if row['instructions'] else None
                )
        self.stdout.write('Loaded Prescription Details')

    def load_admissions(self, base_path):
        with open(os.path.join(base_path, 'admission.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Admission.objects.create(
                    admission_id=int(row['admission_id']),
                    patient_id=int(row['patient_id']),
                    room_id=int(row['room_id']),
                    doctor_id=int(row['doctor_id']),
                    admission_date=datetime.strptime(row['admission_date'], '%Y-%m-%d %H:%M:%S'),
                    discharge_date=datetime.strptime(row['discharge_date'], '%Y-%m-%d %H:%M:%S') if row['discharge_date'] else None,
                    diagnosis=row['diagnosis'],
                    status=row['status']
                )
        self.stdout.write('Loaded Admissions')

    def load_billing(self, base_path):
        with open(os.path.join(base_path, 'billing.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Billing.objects.create(
                    bill_id=int(row['bill_id']),
                    patient_id=int(row['patient_id']),
                    admission_id=int(row['admission_id']) if row['admission_id'] else None,
                    total_amount=float(row['total_amount']),
                    paid_amount=float(row['paid_amount']),
                    payment_status=row['payment_status'],
                    bill_date=datetime.strptime(row['bill_date'], '%Y-%m-%d').date(),
                    payment_method=row['payment_method'] if row['payment_method'] else None
                )
        self.stdout.write('Loaded Billing')

    def load_lab_tests(self, base_path):
        with open(os.path.join(base_path, 'lab_test.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                LabTest.objects.create(
                    test_id=int(row['test_id']),
                    patient_id=int(row['patient_id']),
                    doctor_id=int(row['doctor_id']),
                    test_name=row['test_name'],
                    test_date=datetime.strptime(row['test_date'], '%Y-%m-%d').date(),
                    results=row['results'] if row['results'] else None,
                    status=row['status'],
                    record_id=int(row['record_id']) if row['record_id'] else None
                )
        self.stdout.write('Loaded Lab Tests')
