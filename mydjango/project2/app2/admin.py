from django.contrib import admin
from app2.models import Bank
# Register your models here.
class BankAdmin(admin.ModelAdmin):
    admin.site.register(Bank)