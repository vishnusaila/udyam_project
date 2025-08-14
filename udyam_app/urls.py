from django.contrib import admin
from django.urls import path
from udyam_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.step1_view, name="step1"),
    path("step2/", views.step2_view, name="step2"),
    path("success/", views.success_view, name="success"),
]
