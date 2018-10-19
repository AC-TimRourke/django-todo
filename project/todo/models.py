from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Todo(models.Model):
    description = models.CharField(max_length=250)
    created_at  = models.DateTimeField()
    updated_at  = models.DateTimeField()
    finished_at = models.DateTimeField()
    user_id     = models.ForeignKey(User, on_delete=models.CASCADE)