from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .form import *
from .models import *

# Create your views here.

def is_admin(user):
    return user.is_staff


@login_required
def home(request):
    employees=Employee.objects.all()
    leaves=LeaveRequest.objects.all()
    context={
        'employees':employees,
        'leaves':leaves,
    }
    return render(request,'home.html',context)



def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})



def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            auth_login(request,user)
            return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})



def logout(request):
    auth_logout(request)
    return redirect('home')



@login_required
@user_passes_test(is_admin,login_url='home')
def create_employee(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=EmployeeForm()
    return render(request,'employee_form.html',{'form':form})


@login_required
def create_leave(request):
    if request.method=='POST':
        form=LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
        
    else:
        form=LeaveRequestForm()
    return render(request,'leave_form.html',{'form':form})


@login_required
def leave_list(request):
    leaves=LeaveRequest.objects.all()
    return render(request,'leave_list.html',{'leaves':leaves})


@login_required
@user_passes_test(is_admin,login_url='home')
def approve_leave(request,pk):
    leave=get_object_or_404(LeaveRequest,pk=pk)
    leave.status='Approved'
    leave.save()
    return redirect('leave_list')


@login_required
@user_passes_test(is_admin,login_url='home')
def reject_leave(request,pk):
    leave=get_object_or_404(LeaveRequest,pk=pk)
    leave.status='Rejected'
    leave.save()
    return redirect('leave_list')






