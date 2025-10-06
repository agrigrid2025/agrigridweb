from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    abn_number = models.CharField(max_length=20)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    is_complete = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_users')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Company(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    abn_number = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = CountryField(blank_label='(Select country)')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    unit_of_measure = models.CharField(max_length=10, choices=[('metric', 'Metric'), ('imperial', 'Imperial')])
    time_zone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

