from django.test import TestCase
from .forms import Step1Form, Step2Form

class FormTests(TestCase):
    def test_invalid_aadhaar(self):
        form = Step1Form(data={'aadhaar': 'abc'})
        self.assertFalse(form.is_valid())

    def test_valid_aadhaar(self):
        form = Step1Form(data={'aadhaar': '123456789012'})
        self.assertTrue(form.is_valid())

    def test_invalid_pan(self):
        form = Step2Form(data={'name': 'Test', 'pan': '1234'})
        self.assertFalse(form.is_valid())

    def test_valid_pan(self):
        form = Step2Form(data={'name': 'Test', 'pan': 'ABCDE1234F'})
        self.assertTrue(form.is_valid())
