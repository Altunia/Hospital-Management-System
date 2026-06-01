from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db import models
from .models import (
    Department, Doctor, Patient, Staff, Nurse, Room,
    Appointment, MedicalRecord, Prescription, Medicine,
    PrescriptionDetail, Admission, Billing, LabTest
)
from .forms import (
    DepartmentForm, DoctorForm, PatientForm, StaffForm, NurseForm, RoomForm,
    AppointmentForm, MedicalRecordForm, PrescriptionForm, MedicineForm,
    PrescriptionDetailForm, AdmissionForm, BillingForm, LabTestForm
)


# Dashboard View
def dashboard(request):
    context = {
        'total_patients': Patient.objects.count(),
        'total_doctors': Doctor.objects.count(),
        'total_appointments': Appointment.objects.count(),
        'total_admissions': Admission.objects.filter(status='Admitted').count(),
        'available_rooms': Room.objects.filter(status='Available').count(),
        'pending_bills': Billing.objects.filter(payment_status='Unpaid').count(),
        'pending_lab_tests': LabTest.objects.filter(status='Pending').count(),
        'total_revenue': Billing.objects.aggregate(total=models.Sum('total_amount'))['total'] or 0,
    }
    return render(request, 'hospital/dashboard.html', context)


# Department Views
class DepartmentListView(ListView):
    model = Department
    template_name = 'hospital/department_list.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'hospital/department_detail.html'
    context_object_name = 'department'


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'hospital/department_form.html'
    success_url = reverse_lazy('department-list')


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('department-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Department'
        context['list_url'] = 'department-list'
        return context


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('department-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Department'
        context['list_url'] = 'department-list'
        return context


# Doctor Views
class DoctorListView(ListView):
    model = Doctor
    template_name = 'hospital/doctor_list.html'
    context_object_name = 'doctors'


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'hospital/doctor_detail.html'
    context_object_name = 'doctor'


class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('doctor-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Doctor'
        context['list_url'] = 'doctor-list'
        return context


class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('doctor-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Doctor'
        context['list_url'] = 'doctor-list'
        return context


class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('doctor-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Doctor'
        context['list_url'] = 'doctor-list'
        return context


# Patient Views
class PatientListView(ListView):
    model = Patient
    template_name = 'hospital/patient_list.html'
    context_object_name = 'patients'


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'hospital/patient_detail.html'
    context_object_name = 'patient'


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'hospital/patient_form.html'
    success_url = reverse_lazy('patient-list')


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'hospital/patient_form.html'
    success_url = reverse_lazy('patient-list')


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'hospital/patient_confirm_delete.html'
    success_url = reverse_lazy('patient-list')


# Staff Views
class StaffListView(ListView):
    model = Staff
    template_name = 'hospital/staff_list.html'
    context_object_name = 'staff_list'


class StaffDetailView(DetailView):
    model = Staff
    template_name = 'hospital/staff_detail.html'
    context_object_name = 'staff'


class StaffCreateView(CreateView):
    model = Staff
    form_class = StaffForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('staff-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Staff'
        context['list_url'] = 'staff-list'
        return context


class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('staff-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Staff'
        context['list_url'] = 'staff-list'
        return context


class StaffDeleteView(DeleteView):
    model = Staff
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('staff-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Staff'
        context['list_url'] = 'staff-list'
        return context


# Nurse Views
class NurseListView(ListView):
    model = Nurse
    template_name = 'hospital/nurse_list.html'
    context_object_name = 'nurses'


class NurseDetailView(DetailView):
    model = Nurse
    template_name = 'hospital/nurse_detail.html'
    context_object_name = 'nurse'


class NurseCreateView(CreateView):
    model = Nurse
    form_class = NurseForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('nurse-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Nurse'
        context['list_url'] = 'nurse-list'
        return context


class NurseUpdateView(UpdateView):
    model = Nurse
    form_class = NurseForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('nurse-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Nurse'
        context['list_url'] = 'nurse-list'
        return context


class NurseDeleteView(DeleteView):
    model = Nurse
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('nurse-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Nurse'
        context['list_url'] = 'nurse-list'
        return context


# Room Views
class RoomListView(ListView):
    model = Room
    template_name = 'hospital/room_list.html'
    context_object_name = 'rooms'


class RoomDetailView(DetailView):
    model = Room
    template_name = 'hospital/room_detail.html'
    context_object_name = 'room'


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('room-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Room'
        context['list_url'] = 'room-list'
        return context


class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('room-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Room'
        context['list_url'] = 'room-list'
        return context


class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('room-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Room'
        context['list_url'] = 'room-list'
        return context


# Appointment Views
class AppointmentListView(ListView):
    model = Appointment
    template_name = 'hospital/appointment_list.html'
    context_object_name = 'appointments'


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'hospital/appointment_detail.html'
    context_object_name = 'appointment'


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('appointment-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Appointment'
        context['list_url'] = 'appointment-list'
        return context


class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('appointment-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Appointment'
        context['list_url'] = 'appointment-list'
        return context


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('appointment-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Appointment'
        context['list_url'] = 'appointment-list'
        return context


# Medical Record Views
class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = 'hospital/medical_record_list.html'
    context_object_name = 'medical_records'


class MedicalRecordDetailView(DetailView):
    model = MedicalRecord
    template_name = 'hospital/medical_record_detail.html'
    context_object_name = 'medical_record'


class MedicalRecordCreateView(CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('medical-record-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Medical Record'
        context['list_url'] = 'medical-record-list'
        return context


class MedicalRecordUpdateView(UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('medical-record-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Medical Record'
        context['list_url'] = 'medical-record-list'
        return context


class MedicalRecordDeleteView(DeleteView):
    model = MedicalRecord
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('medical-record-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Medical Record'
        context['list_url'] = 'medical-record-list'
        return context


# Prescription Views
class PrescriptionListView(ListView):
    model = Prescription
    template_name = 'hospital/prescription_list.html'
    context_object_name = 'prescriptions'


class PrescriptionDetailView(DetailView):
    model = Prescription
    template_name = 'hospital/prescription_detail.html'
    context_object_name = 'prescription'


class PrescriptionCreateView(CreateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('prescription-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Prescription'
        context['list_url'] = 'prescription-list'
        return context


class PrescriptionUpdateView(UpdateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('prescription-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Prescription'
        context['list_url'] = 'prescription-list'
        return context


class PrescriptionDeleteView(DeleteView):
    model = Prescription
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('prescription-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Prescription'
        context['list_url'] = 'prescription-list'
        return context


# Medicine Views
class MedicineListView(ListView):
    model = Medicine
    template_name = 'hospital/medicine_list.html'
    context_object_name = 'medicines'


class MedicineDetailView(DetailView):
    model = Medicine
    template_name = 'hospital/medicine_detail.html'
    context_object_name = 'medicine'


class MedicineCreateView(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('medicine-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Medicine'
        context['list_url'] = 'medicine-list'
        return context


class MedicineUpdateView(UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('medicine-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Medicine'
        context['list_url'] = 'medicine-list'
        return context


class MedicineDeleteView(DeleteView):
    model = Medicine
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('medicine-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Medicine'
        context['list_url'] = 'medicine-list'
        return context


# Prescription Detail Views
class PrescriptionDetailListView(ListView):
    model = PrescriptionDetail
    template_name = 'hospital/prescription_detail_list.html'
    context_object_name = 'prescription_details'


class PrescriptionDetailDetailView(DetailView):
    model = PrescriptionDetail
    template_name = 'hospital/prescription_detail_detail.html'
    context_object_name = 'prescription_detail'


class PrescriptionDetailCreateView(CreateView):
    model = PrescriptionDetail
    form_class = PrescriptionDetailForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('prescription-detail-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Prescription Detail'
        context['list_url'] = 'prescription-detail-list'
        return context


class PrescriptionDetailUpdateView(UpdateView):
    model = PrescriptionDetail
    form_class = PrescriptionDetailForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('prescription-detail-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Prescription Detail'
        context['list_url'] = 'prescription-detail-list'
        return context


class PrescriptionDetailDeleteView(DeleteView):
    model = PrescriptionDetail
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('prescription-detail-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Prescription Detail'
        context['list_url'] = 'prescription-detail-list'
        return context


# Admission Views
class AdmissionListView(ListView):
    model = Admission
    template_name = 'hospital/admission_list.html'
    context_object_name = 'admissions'


class AdmissionDetailView(DetailView):
    model = Admission
    template_name = 'hospital/admission_detail.html'
    context_object_name = 'admission'


class AdmissionCreateView(CreateView):
    model = Admission
    form_class = AdmissionForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('admission-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Admission'
        context['list_url'] = 'admission-list'
        return context


class AdmissionUpdateView(UpdateView):
    model = Admission
    form_class = AdmissionForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('admission-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Admission'
        context['list_url'] = 'admission-list'
        return context


class AdmissionDeleteView(DeleteView):
    model = Admission
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('admission-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Admission'
        context['list_url'] = 'admission-list'
        return context


# Billing Views
class BillingListView(ListView):
    model = Billing
    template_name = 'hospital/billing_list.html'
    context_object_name = 'billings'


class BillingDetailView(DetailView):
    model = Billing
    template_name = 'hospital/billing_detail.html'
    context_object_name = 'billing'


class BillingCreateView(CreateView):
    model = Billing
    form_class = BillingForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('billing-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Billing'
        context['list_url'] = 'billing-list'
        return context


class BillingUpdateView(UpdateView):
    model = Billing
    form_class = BillingForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('billing-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Billing'
        context['list_url'] = 'billing-list'
        return context


class BillingDeleteView(DeleteView):
    model = Billing
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('billing-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Billing'
        context['list_url'] = 'billing-list'
        return context


# Lab Test Views
class LabTestListView(ListView):
    model = LabTest
    template_name = 'hospital/lab_test_list.html'
    context_object_name = 'lab_tests'


class LabTestDetailView(DetailView):
    model = LabTest
    template_name = 'hospital/lab_test_detail.html'
    context_object_name = 'lab_test'


class LabTestCreateView(CreateView):
    model = LabTest
    form_class = LabTestForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('lab-test-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Lab Test'
        context['list_url'] = 'lab-test-list'
        return context


class LabTestUpdateView(UpdateView):
    model = LabTest
    form_class = LabTestForm
    template_name = 'hospital/generic_form.html'
    success_url = reverse_lazy('lab-test-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Lab Test'
        context['list_url'] = 'lab-test-list'
        return context


class LabTestDeleteView(DeleteView):
    model = LabTest
    template_name = 'hospital/generic_confirm_delete.html'
    success_url = reverse_lazy('lab-test-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Lab Test'
        context['list_url'] = 'lab-test-list'
        return context
