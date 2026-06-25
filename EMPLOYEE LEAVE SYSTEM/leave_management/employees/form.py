from django import forms
from .models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model=LeaveRequest
        fields=[
            'employee',
            'leave_type',
            'start_date',
            'end_date',
            'reason',
        ]