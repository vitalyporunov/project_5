from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(
        User, 
        related_name='sent_messages',  
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User, 
        related_name='received_messages',  
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)  # ✅ Tracks if message was opened

    def __str__(self):
        return f"{self.subject} ({'Read' if self.is_read else 'Unread'})"

