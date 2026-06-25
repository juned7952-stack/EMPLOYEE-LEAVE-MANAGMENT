from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'email',
        'department',
    )

    search_fields=(
        "name",
        "email",
    )


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'employee',
        'leave_type',
        'status',
    )

    list_filter=(
        'status',
    )
