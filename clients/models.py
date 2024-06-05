from django.conf import settings
from django.db import models
from django.urls import reverse

class Client(models.Model):
    CLIENT_CONTACT_METHOD_CHOICES = [
        ('line', 'Line'),
        ('facebook', 'Facebook Messenger'),
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='clients'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_method = models.CharField(max_length=20, choices=CLIENT_CONTACT_METHOD_CHOICES)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    bonus_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk': self.pk})