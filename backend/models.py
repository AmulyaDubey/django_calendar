from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from datetime import datetime

class Profile(models.Model):
    
    username=models.CharField(max_length=100, db_column='username', null=True)
    email = models.EmailField(max_length=150, db_column='email', null=True, unique=True)
    password=models.CharField(max_length=100, db_column='password', null=True)
    user_id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, db_column='user_id')

    def __str__(self):
        return self.username

class Event(models.Model):
    title=models.CharField(max_length=100, db_column='title', null=True, unique=True)
    date = models.DateField(max_length=100, db_column='date', null=True, unique=False)
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.title