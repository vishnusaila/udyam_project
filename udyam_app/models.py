from django.db import models


from django.db import models

class UdyamRegistration(models.Model):
    aadhaar = models.CharField(max_length=12)
    otp = models.CharField(max_length=6)
    pan = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.pan})"
from django.db import models

# udyam_app/models.py
from django.db import models

class AadhaarVerification(models.Model):
    entrepreneur_name = models.CharField(max_length=100)
    aadhaar = models.CharField(max_length=12)
    consent_given = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.entrepreneur_name} - {self.aadhaar}"
