from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import date


def validate_phone(value):
    if value and not value.isdigit():
        raise ValidationError('Phone number must contain only digits.')


def validate_email(value):
    if value and '@' not in value:
        raise ValidationError('Email must contain @.')


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    head_doctor_id = models.ForeignKey(
        'Doctor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headed_departments'
    )
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        validators=[RegexValidator(regex=r'^[0-9+\-() ]{7,15}$', message='Phone format invalid')]
    )

    class Meta:
        db_table = 'department'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.department_name


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True, validators=[validate_phone])
    email = models.CharField(max_length=100, unique=True, null=True, blank=True, validators=[validate_email])
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    hire_date = models.DateField()
    license_number = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'doctor'
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def clean(self):
        if self.hire_date < date(2000, 1, 1):
            raise ValidationError({'hire_date': 'Hire date must be on or after 2000-01-01'})

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


class Patient(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ]

    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_type = models.CharField(max_length=5, choices=BLOOD_TYPE_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, validators=[validate_phone])
    email = models.CharField(max_length=100, null=True, blank=True, validators=[validate_email])
    address = models.TextField(null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'patient'
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def clean(self):
        if self.date_of_birth > date.today():
            raise ValidationError({'date_of_birth': 'Date of birth cannot be in the future'})
        if self.registration_date < self.date_of_birth:
            raise ValidationError({'registration_date': 'Registration date cannot be before date of birth'})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    phone = models.CharField(max_length=15, unique=True, validators=[validate_phone])
    email = models.CharField(max_length=100, null=True, blank=True, validators=[validate_email])
    hire_date = models.DateField()

    class Meta:
        db_table = 'staff'
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def clean(self):
        if self.hire_date < date(2000, 1, 1):
            raise ValidationError({'hire_date': 'Hire date must be on or after 2000-01-01'})

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"


class Nurse(models.Model):
    SHIFT_CHOICES = [('Morning', 'Morning'), ('Evening', 'Evening'), ('Night', 'Night')]

    nurse_id = models.AutoField(primary_key=True)
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE, related_name='nurse_profile')
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    certification = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'nurse'
        verbose_name = 'Nurse'
        verbose_name_plural = 'Nurses'

    def __str__(self):
        return f"{self.staff.first_name} {self.staff.last_name} - Nurse"


class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('General', 'General'), ('Private', 'Private'), ('ICU', 'ICU'),
        ('Semi-Private', 'Semi-Private'), ('Emergency', 'Emergency')
    ]
    STATUS_CHOICES = [('Available', 'Available'), ('Occupied', 'Occupied'), ('Maintenance', 'Maintenance')]

    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=20, unique=True)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPE_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])

    class Meta:
        db_table = 'room'
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"


class Appointment(models.Model):
    STATUS_CHOICES = [('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('No-Show', 'No-Show')]

    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    reason = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'appointment'
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f"Appointment {self.appointment_id} - {self.patient}"


class MedicalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    visit_date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'medical_record'
        verbose_name = 'Medical Record'
        verbose_name_plural = 'Medical Records'

    def clean(self):
        if self.visit_date < date(2000, 1, 1):
            raise ValidationError({'visit_date': 'Visit date must be on or after 2000-01-01'})

    def __str__(self):
        return f"Record {self.record_id} - {self.patient}"


class Prescription(models.Model):
    STATUS_CHOICES = [('Active', 'Active'), ('Dispensed', 'Dispensed'), ('Expired', 'Expired')]

    prescription_id = models.AutoField(primary_key=True)
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescribed_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    class Meta:
        db_table = 'prescription'
        verbose_name = 'Prescription'
        verbose_name_plural = 'Prescriptions'

    def clean(self):
        if self.expiry_date and self.expiry_date < self.prescribed_date:
            raise ValidationError({'expiry_date': 'Expiry date cannot be before prescribed date'})

    def __str__(self):
        return f"Prescription {self.prescription_id} - {self.patient}"


class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=150)
    generic_name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    stock_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])

    class Meta:
        db_table = 'medicine'
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'

    def __str__(self):
        return self.medicine_name


class PrescriptionDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='details')
    medicine = models.ForeignKey(Medicine, on_delete=models.RESTRICT)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration_days = models.IntegerField(validators=[MinValueValidator(1)])
    instructions = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'prescription_detail'
        verbose_name = 'Prescription Detail'
        verbose_name_plural = 'Prescription Details'

    def __str__(self):
        return f"Detail {self.detail_id} - {self.medicine.medicine_name}"


class Admission(models.Model):
    STATUS_CHOICES = [('Admitted', 'Admitted'), ('Discharged', 'Discharged'), ('Transferred', 'Transferred')]

    admission_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.RESTRICT)
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    admission_date = models.DateTimeField()
    discharge_date = models.DateTimeField(null=True, blank=True)
    diagnosis = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Admitted')

    class Meta:
        db_table = 'admission'
        verbose_name = 'Admission'
        verbose_name_plural = 'Admissions'

    def clean(self):
        if self.discharge_date and self.discharge_date < self.admission_date:
            raise ValidationError({'discharge_date': 'Discharge date cannot be before admission date'})

    def __str__(self):
        return f"Admission {self.admission_id} - {self.patient}"


class Billing(models.Model):
    PAYMENT_STATUS_CHOICES = [('Unpaid', 'Unpaid'), ('Partial', 'Partial'), ('Paid', 'Paid')]
    PAYMENT_METHOD_CHOICES = [('Cash', 'Cash'), ('Card', 'Card'), ('Insurance', 'Insurance'), ('Online Transfer', 'Online Transfer')]

    bill_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT)
    admission = models.ForeignKey(Admission, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Unpaid')
    bill_date = models.DateField()
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, null=True, blank=True)

    class Meta:
        db_table = 'billing'
        verbose_name = 'Billing'
        verbose_name_plural = 'Billings'

    def clean(self):
        if self.paid_amount > self.total_amount:
            raise ValidationError({'paid_amount': 'Paid amount cannot exceed total amount'})

    def __str__(self):
        return f"Bill {self.bill_id} - {self.patient}"


class LabTest(models.Model):
    STATUS_CHOICES = [('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')]

    test_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    test_name = models.CharField(max_length=150)
    test_date = models.DateField()
    results = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    record = models.ForeignKey(MedicalRecord, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'lab_test'
        verbose_name = 'Lab Test'
        verbose_name_plural = 'Lab Tests'

    def __str__(self):
        return f"Test {self.test_id} - {self.test_name}"
