from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('employee/create/',views.create_employee,name='create_employee'),
    path('leave/create/',views.create_leave,name='create_leave'),
    path('leave/list/',views.leave_list,name='leave_list'),
    path('leave/approve/<int:pk>/',views.approve_leave,name='approve_leave'),
    path('leave/reject/<int:pk>/',views.reject_leave,name='reject_leave'),
]