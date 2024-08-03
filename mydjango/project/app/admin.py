from django.contrib import admin
from app.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    admin.site.register(Student)