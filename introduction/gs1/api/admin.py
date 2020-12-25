from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # localhost:8000/admin/student
    # student table view with below fields in admin
    # list_display is a builtin property, used to display required fields of student table in admin view
    list_display = ['id', 'name', 'roll', 'city']
