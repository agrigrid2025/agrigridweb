from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    abn_number = models.CharField(max_length=20)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Profile"
