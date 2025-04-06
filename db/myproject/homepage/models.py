from django.db import models

class UserInfo(models.Model):
    # Personal Information
    name = models.CharField(max_length=100)
    dob = models.DateField(default='2000-01-01')  # Add a default date
    email = models.EmailField()
    phone = models.CharField(max_length=15, default='000-000-0000')  # Add a default phone number
    address = models.TextField(default='Not provided')  # Add a default address

    # Academic Information
    roll = models.CharField(max_length=20, blank=True, null=True)  # Optional
    class_name = models.CharField(max_length=50)  # Applying for Grade
    year = models.IntegerField(default=2023)  # Add a default year
    previous_school = models.CharField(max_length=100, blank=True, null=True)  # Optional

    # Documents (File Upload)
    documents = models.FileField(upload_to='documents/', blank=True, null=True)  # Optional

    # Parent/Guardian Information
    parent_name = models.CharField(max_length=100, default='Not provided')  # Add a default
    parent_phone = models.CharField(max_length=15, default='000-000-0000')  # Add a default
    parent_email = models.EmailField(default='example@example.com')  # Add a default

    # Agreements
    terms = models.BooleanField(default=False)  # Terms and Conditions

    class Meta:
        verbose_name = "RK_FUTURE_SCHOOL_INFO"
        verbose_name_plural = "RK_FUTURE_SCHOOL_INFO"

    def __str__(self):
        return self.name