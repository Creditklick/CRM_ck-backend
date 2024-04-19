from django.contrib import admin
from .models import Customer , CustomUser
# from . models import UserProfile
# Register your models here.

# admin.site.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]
admin.site.register(Customer, CustomerAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display=('username', 'email' , 'name' ,'password', 'employee_code', 'registration_date')
admin.site.register(CustomUser, CustomUserAdmin)