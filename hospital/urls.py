from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Department URLs
    path('departments/', views.DepartmentListView.as_view(), name='department-list'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('departments/create/', views.DepartmentCreateView.as_view(), name='department-create'),
    path('departments/<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='department-update'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department-delete'),
    
    # Doctor URLs
    path('doctors/', views.DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctors/create/', views.DoctorCreateView.as_view(), name='doctor-create'),
    path('doctors/<int:pk>/update/', views.DoctorUpdateView.as_view(), name='doctor-update'),
    path('doctors/<int:pk>/delete/', views.DoctorDeleteView.as_view(), name='doctor-delete'),
    
    # Patient URLs
    path('patients/', views.PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('patients/create/', views.PatientCreateView.as_view(), name='patient-create'),
    path('patients/<int:pk>/update/', views.PatientUpdateView.as_view(), name='patient-update'),
    path('patients/<int:pk>/delete/', views.PatientDeleteView.as_view(), name='patient-delete'),
    
    # Staff URLs
    path('staff/', views.StaffListView.as_view(), name='staff-list'),
    path('staff/<int:pk>/', views.StaffDetailView.as_view(), name='staff-detail'),
    path('staff/create/', views.StaffCreateView.as_view(), name='staff-create'),
    path('staff/<int:pk>/update/', views.StaffUpdateView.as_view(), name='staff-update'),
    path('staff/<int:pk>/delete/', views.StaffDeleteView.as_view(), name='staff-delete'),
    
    # Nurse URLs
    path('nurses/', views.NurseListView.as_view(), name='nurse-list'),
    path('nurses/<int:pk>/', views.NurseDetailView.as_view(), name='nurse-detail'),
    path('nurses/create/', views.NurseCreateView.as_view(), name='nurse-create'),
    path('nurses/<int:pk>/update/', views.NurseUpdateView.as_view(), name='nurse-update'),
    path('nurses/<int:pk>/delete/', views.NurseDeleteView.as_view(), name='nurse-delete'),
    
    # Room URLs
    path('rooms/', views.RoomListView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='room-detail'),
    path('rooms/create/', views.RoomCreateView.as_view(), name='room-create'),
    path('rooms/<int:pk>/update/', views.RoomUpdateView.as_view(), name='room-update'),
    path('rooms/<int:pk>/delete/', views.RoomDeleteView.as_view(), name='room-delete'),
    
    # Appointment URLs
    path('appointments/', views.AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('appointments/create/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('appointments/<int:pk>/update/', views.AppointmentUpdateView.as_view(), name='appointment-update'),
    path('appointments/<int:pk>/delete/', views.AppointmentDeleteView.as_view(), name='appointment-delete'),
    
    # Medical Record URLs
    path('medical-records/', views.MedicalRecordListView.as_view(), name='medical-record-list'),
    path('medical-records/<int:pk>/', views.MedicalRecordDetailView.as_view(), name='medical-record-detail'),
    path('medical-records/create/', views.MedicalRecordCreateView.as_view(), name='medical-record-create'),
    path('medical-records/<int:pk>/update/', views.MedicalRecordUpdateView.as_view(), name='medical-record-update'),
    path('medical-records/<int:pk>/delete/', views.MedicalRecordDeleteView.as_view(), name='medical-record-delete'),
    
    # Prescription URLs
    path('prescriptions/', views.PrescriptionListView.as_view(), name='prescription-list'),
    path('prescriptions/<int:pk>/', views.PrescriptionDetailView.as_view(), name='prescription-detail'),
    path('prescriptions/create/', views.PrescriptionCreateView.as_view(), name='prescription-create'),
    path('prescriptions/<int:pk>/update/', views.PrescriptionUpdateView.as_view(), name='prescription-update'),
    path('prescriptions/<int:pk>/delete/', views.PrescriptionDeleteView.as_view(), name='prescription-delete'),
    
    # Medicine URLs
    path('medicines/', views.MedicineListView.as_view(), name='medicine-list'),
    path('medicines/<int:pk>/', views.MedicineDetailView.as_view(), name='medicine-detail'),
    path('medicines/create/', views.MedicineCreateView.as_view(), name='medicine-create'),
    path('medicines/<int:pk>/update/', views.MedicineUpdateView.as_view(), name='medicine-update'),
    path('medicines/<int:pk>/delete/', views.MedicineDeleteView.as_view(), name='medicine-delete'),
    
    # Prescription Detail URLs
    path('prescription-details/', views.PrescriptionDetailListView.as_view(), name='prescription-detail-list'),
    path('prescription-details/<int:pk>/', views.PrescriptionDetailDetailView.as_view(), name='prescription-detail-detail'),
    path('prescription-details/create/', views.PrescriptionDetailCreateView.as_view(), name='prescription-detail-create'),
    path('prescription-details/<int:pk>/update/', views.PrescriptionDetailUpdateView.as_view(), name='prescription-detail-update'),
    path('prescription-details/<int:pk>/delete/', views.PrescriptionDetailDeleteView.as_view(), name='prescription-detail-delete'),
    
    # Admission URLs
    path('admissions/', views.AdmissionListView.as_view(), name='admission-list'),
    path('admissions/<int:pk>/', views.AdmissionDetailView.as_view(), name='admission-detail'),
    path('admissions/create/', views.AdmissionCreateView.as_view(), name='admission-create'),
    path('admissions/<int:pk>/update/', views.AdmissionUpdateView.as_view(), name='admission-update'),
    path('admissions/<int:pk>/delete/', views.AdmissionDeleteView.as_view(), name='admission-delete'),
    
    # Billing URLs
    path('billing/', views.BillingListView.as_view(), name='billing-list'),
    path('billing/<int:pk>/', views.BillingDetailView.as_view(), name='billing-detail'),
    path('billing/create/', views.BillingCreateView.as_view(), name='billing-create'),
    path('billing/<int:pk>/update/', views.BillingUpdateView.as_view(), name='billing-update'),
    path('billing/<int:pk>/delete/', views.BillingDeleteView.as_view(), name='billing-delete'),
    
    # Lab Test URLs
    path('lab-tests/', views.LabTestListView.as_view(), name='lab-test-list'),
    path('lab-tests/<int:pk>/', views.LabTestDetailView.as_view(), name='lab-test-detail'),
    path('lab-tests/create/', views.LabTestCreateView.as_view(), name='lab-test-create'),
    path('lab-tests/<int:pk>/update/', views.LabTestUpdateView.as_view(), name='lab-test-update'),
    path('lab-tests/<int:pk>/delete/', views.LabTestDeleteView.as_view(), name='lab-test-delete'),
]
