from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_farm, name='create_farm'),
    path('map/<int:farm_id>/', views.farm_map, name='farm_map'),
    path('save-boundary/<int:farm_id>/', views.save_farm_boundary, name='save_farm_boundary'),
]