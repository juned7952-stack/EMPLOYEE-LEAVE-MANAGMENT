from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    department=models.TextField()
    joining_date=models.DateField()


    def __str__(self):
        return self.name
    

class LeaveRequest(models.Model):
    STATUS_CHOICE=(
        ('Pending',"Pending"),
        ('Approved','Approved'),
        ('Rejected','Rejected'),
    )

    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='leave_request')
    leave_type=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    reason=models.TextField()
    status=models.CharField(max_length=100,choices=STATUS_CHOICE,default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.employee.name}-{self.status}"