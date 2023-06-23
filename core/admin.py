from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'result_status']
    #list_display = ['id', 'name', 'roll', 'department', 'result_status']
