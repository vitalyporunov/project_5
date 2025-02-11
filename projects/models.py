from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# ✅ Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')  # Added related_name for clarity

    def __str__(self):
        return self.name


# ✅ Project Model
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

    # ✅ Owner - Unique related_name to prevent conflicts
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='owned_projects'
    )

    # ✅ Stakeholders - Fixed ManyToManyField for user association
    stakeholders = models.ManyToManyField(
        User,
        related_name='stakeholder_projects',
        blank=True
    )

    # ✅ Status Field with default value
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Not Started')

    # ✅ Category - Ensure clarity with related_name
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='projects'  # Added related_name for reverse querying
    )

    def __str__(self):
        return self.name


# ✅ Message Model
class Message(models.Model):
    sender = models.ForeignKey(
        User,
        related_name='sent_messages',  # Simplified related_name
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User,
        related_name='received_messages',  # Simplified related_name
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.subject} (From: {self.sender.username})'
