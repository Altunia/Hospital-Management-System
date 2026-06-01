from django.contrib import admin
from .models import (
    Department, Doctor, Patient, Staff, Nurse, Room,
    Appointment, MedicalRecord, Prescription, Medicine,
    PrescriptionDetail, Admission, Billing, LabTest
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_id', 'department_name', 'location', 'phone']
    search_fields = ['department_name', 'location']
    list_filter = ['location']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor_id', 'first_name', 'last_name', 'specialization', 'department', 'phone', 'email']
    search_fields = ['first_name', 'last_name', 'specialization', 'license_number']
    list_filter = ['department', 'specialization']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'first_name', 'last_name', 'gender', 'blood_type', 'phone', 'registration_date']
    search_fields = ['first_name', 'last_name', 'phone']
    list_filter = ['gender', 'blood_type']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'first_name', 'last_name', 'role', 'department', 'phone', 'hire_date']
    search_fields = ['first_name', 'last_name', 'role']
    list_filter = ['department', 'role']


@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ['nurse_id', 'staff', 'shift', 'department', 'certification']
    search_fields = ['staff__first_name', 'staff__last_name']
    list_filter = ['shift', 'department']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_id', 'room_number', 'room_type', 'department', 'status', 'price_per_day']
    search_fields = ['room_number']
    list_filter = ['room_type', 'status', 'department']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['appointment_id', 'patient', 'doctor', 'appointment_date', 'status']
    search_fields = ['patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name']
    list_filter = ['status', 'appointment_date']
    date_hierarchy = 'appointment_date'


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['record_id', 'patient', 'doctor', 'visit_date', 'diagnosis']
    search_fields = ['patient__first_name', 'patient__last_name', 'diagnosis']
    list_filter = ['visit_date']
    date_hierarchy = 'visit_date'


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['prescription_id', 'patient', 'prescribed_date', 'expiry_date', 'status']
    search_fields = ['patient__first_name', 'patient__last_name']
    list_filter = ['status', 'prescribed_date']
    date_hierarchy = 'prescribed_date'


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['medicine_id', 'medicine_name', 'generic_name', 'category', 'stock_quantity', 'unit_price']
    search_fields = ['medicine_name', 'generic_name', 'category']
    list_filter = ['category']


@admin.register(PrescriptionDetail)
class PrescriptionDetailAdmin(admin.ModelAdmin):
    list_display = ['detail_id', 'prescription', 'medicine', 'dosage', 'frequency', 'duration_days']
    search_fields = ['medicine__medicine_name', 'prescription__patient__first_name']
    list_filter = ['dosage', 'frequency']


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['admission_id', 'patient', 'room', 'doctor', 'admission_date', 'discharge_date', 'status']
    search_fields = ['patient__first_name', 'patient__last_name']
    list_filter = ['status', 'admission_date']
    date_hierarchy = 'admission_date'


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ['bill_id', 'patient', 'total_amount', 'paid_amount', 'payment_status', 'bill_date', 'payment_method']
    search_fields = ['patient__first_name', 'patient__last_name']
    list_filter = ['payment_status', 'payment_method', 'bill_date']
    date_hierarchy = 'bill_date'


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ['test_id', 'patient', 'doctor', 'test_name', 'test_date', 'status']
    search_fields = ['patient__first_name', 'patient__last_name', 'test_name']
    list_filter = ['status', 'test_date']
    date_hierarchy = 'test_date'
