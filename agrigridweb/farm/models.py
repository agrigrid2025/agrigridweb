from django.db import models
from django.contrib.auth.models import User

class Farm(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_farms')
    sub_users = models.ManyToManyField(User, related_name='assigned_farms', blank=True)
    boundary_geojson = models.TextField(blank=True)  # stores polygon as GeoJSON

    def __str__(self):
        return self.name
