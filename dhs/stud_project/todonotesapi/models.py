from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoNote(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.title