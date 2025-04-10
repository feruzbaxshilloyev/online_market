from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True, default='media/default-profile.png')
    t_me = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Xabar(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='yuborilgan_xabarlar')
    qabul = models.PositiveIntegerField()
    desc = models.TextField()
    is_view = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} → {self.recipient.username} | {self.created_at}"
