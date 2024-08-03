from django.contrib import admin
from app3.models import Hostel
# Register your models here.
class HostelAdmin(admin.ModelAdmin):
    admin.site.register(Hostel)
