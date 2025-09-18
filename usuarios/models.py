from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    AVATAR_CHOICES = [
        ('avatar1.png', 'Avatar 1'),
        ('avatar2.png', 'Avatar 2'),
        ('avatar3.png', 'Avatar 3'),
        ('avatar4.png', 'Avatar 4'),
        ('avatar5.png', 'Avatar 5'),
        ('avatar6.png', 'Avatar 6'),
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=50, choices=AVATAR_CHOICES, default='avatar1.png')


    def __str__(self):
        return self.user.username
