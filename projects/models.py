from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Project Model
class Project(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='owned_projects'  # ✅ Unique related_name for owner
    )
    stakeholders = models.ManyToManyField(
        User, 
        related_name='stakeholder_projects',  # ✅ Unique related_name for stakeholders
        blank=True
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Not Started')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


# Message Model
class Message(models.Model):
    sender = models.ForeignKey(
        User,
        related_name='projects_sent_messages',  # ✅ Unique related_name for sender
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User,
        related_name='projects_received_messages',  # ✅ Unique related_name for recipient
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
