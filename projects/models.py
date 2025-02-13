from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# ✅ Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='categories'  # Unique related_name for clarity
    )

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

    # ✅ Stakeholders - ManyToManyField for user association
    stakeholders = models.ManyToManyField(
        User,
        related_name='stakeholder_projects',
        blank=True
    )

    # ✅ Status Field with default value
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Not Started')

    # ✅ Category - Ensuring clarity with related_name
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='projects'  # Added related_name for reverse querying
    )

    def __str__(self):
        return self.name


# ✅ Messaging Model for General Communication
class Message(models.Model):
    sender = models.ForeignKey(
        User,
        related_name='messaging_sent_messages',  # ✅ Unique related_name for messaging
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User,
        related_name='messaging_received_messages',  # ✅ Unique related_name for messaging
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.subject} (From: {self.sender.username})'


# ✅ Messaging Model for Project-Specific Communication
class ProjectMessage(models.Model):
    sender = models.ForeignKey(
        User,
        related_name='projects_sent_messages',  # ✅ Unique related_name for project messaging
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User,
        related_name='projects_received_messages',  # ✅ Unique related_name for project messaging
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        related_name='messages'  # ✅ Connect messages to specific projects
    )
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.subject} (Project: {self.project.name})'
