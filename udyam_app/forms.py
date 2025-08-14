from django import forms
import re

class Step1Form(forms.Form):
    aadhaar = forms.CharField(max_length=12, min_length=12, required=True)

    def clean_aadhaar(self):
        aadhaar = self.cleaned_data['aadhaar']
        if not aadhaar.isdigit():
            raise forms.ValidationError("Aadhaar must be 12 digits.")
        return aadhaar


class Step2Form(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    pan = forms.CharField(max_length=10, required=True)

    def clean_pan(self):
        pan = self.cleaned_data['pan']
        if not re.match(r'^[A-Za-z]{5}[0-9]{4}[A-Za-z]$', pan):
            raise forms.ValidationError("Invalid PAN format.")
        return pan
# udyam_app/forms.py
from django import forms
from .models import AadhaarVerification

class AadhaarVerificationForm(forms.ModelForm):
    class Meta:
        model = AadhaarVerification
        fields = ['name', 'aadhaar', 'pan']  # match model field names exactly
