from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


class Task(models.Model):
    IMPORTANCE_CHOICES  = [
        ('low', 'Низкая'),
        ('medium', 'Средняя'),
        ('high', 'Высокая'),
    ]
    importance = models.CharField(max_length=10, choices=IMPORTANCE_CHOICES, default='medium')
    text = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    priority = models.CharField(max_length=10,choices=IMPORTANCE_CHOICES ,default='medium',verbose_name='Важность')

    def __str__(self):
        return self.text

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    notify_email = models.BooleanField(default=True)
    theme_dark = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name or self.user.username


