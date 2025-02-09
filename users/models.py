from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import render  

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    
    def __str__(self):
        return self.username

# ✅ User role check
from django.contrib.auth.decorators import user_passes_test

def is_manager(user):
    return user.role == 'manager'

@user_passes_test(is_manager)
def restricted_view(request):
    return render(request, 'restricted.html')
