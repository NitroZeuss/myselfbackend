from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
