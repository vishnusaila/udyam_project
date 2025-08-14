from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UdyamRegistration

@admin.register(UdyamRegistration)
class UdyamRegistrationAdmin(admin.ModelAdmin):
    list_display = ("name", "aadhaar", "pan", "submitted_at")

from django.contrib import admin
from .models import AadhaarVerification

admin.site.register(AadhaarVerification)
