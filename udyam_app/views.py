# udyam_app/views.py
import json
import os
import random
from django.shortcuts import render, redirect
from .models import AadhaarVerification


def load_schema():
    schema_path = os.path.join(os.path.dirname(__file__), "schema.json")
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


# Step 1: Aadhaar + OTP
def step1_view(request):
    schema = load_schema()
    step_data = next((s for s in schema["steps"] if s["step"] == 1), None)

    if request.method == "POST":
        aadhaar = request.POST.get("aadhaar", "").strip()
        if not aadhaar:
            return render(request, "step1.html", {
                "step": step_data,
                "error": "Aadhaar number is required"
            })

        # Save Aadhaar in DB
        record, created = AadhaarVerification.objects.get_or_create(aadhaar=aadhaar)

        # Generate OTP (Dev mode)
        otp = str(random.randint(100000, 999999))
        request.session["aadhaar"] = aadhaar
        request.session["otp"] = otp

        return render(request, "otp_display.html", {"otp": otp})

    return render(request, "step1.html", {"step": step_data})


# Step 2: Verify OTP + Save Name & PAN
def step2_view(request):
    schema = load_schema()
    step_data = next((s for s in schema["steps"] if s["step"] == 2), None)

    if request.method == "POST":
        entered_otp = request.POST.get("otp", "").strip()
        stored_otp = request.session.get("otp")
        pan = request.POST.get("pan", "").strip()
        name = request.POST.get("name", "").strip()

        if entered_otp != stored_otp:
            return render(request, "step2.html", {
                "step": step_data,
                "error": "Invalid OTP"
            })

        if not pan or not name:
            return render(request, "step2.html", {
                "step": step_data,
                "error": "PAN and Name are required"
            })

        # Update DB record
        aadhaar = request.session.get("aadhaar")
        record = AadhaarVerification.objects.filter(aadhaar=aadhaar).first()
        if record:
            record.name = name
            record.pan = pan
            record.save()

        return redirect("success")

    return render(request, "step2.html", {"step": step_data})


def success_view(request):
    return render(request, 'success.html')
