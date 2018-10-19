from datetime import datetime
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Todo(models.Model):
    description = models.CharField(max_length=250)
    created_at  = models.DateTimeField()
    updated_at  = models.DateTimeField()
    finished_at = models.DateTimeField(null=True)

    @classmethod
    def create(cls, description):
        todo = cls(description=description, created_at=datetime.now(), updated_at=datetime.now())
        todo.save()

    @classmethod
    def update_description(cls, description):
        cls.description = description
        cls.updated_at = datetime.now()