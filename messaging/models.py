from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(
        User, 
        related_name='messaging_sent_messages',  
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User, 
        related_name='messaging_received_messages',  
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.subject