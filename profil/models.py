from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to='profile_images/', blank=True, null=True, default='media/default-profile.png')
    t_me = models.CharField(max_length=50)

    def __str__(self):
        return self.t_me


User = get_user_model()


class Chat(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_view = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author.username} → {self.qabul.username}: {self.desc[:20]}"
