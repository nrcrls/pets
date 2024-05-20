from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    PREFERRED_CONTACT_CHOICES = [
    ('facebook', 'Facebook Messenger'),
    ('line', 'Line'),
    ('email', 'Email'),
]
    
    preferred_contact = models.CharField(max_length=10, choices=PREFERRED_CONTACT_CHOICES, default='email')
