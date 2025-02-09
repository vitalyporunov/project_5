from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Each category belongs to a user

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ])
    stakeholders = models.ManyToManyField(User, related_name='projects')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # ✅ New Field

    def __str__(self):
        return self.name
