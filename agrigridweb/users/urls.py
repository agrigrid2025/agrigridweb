from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('register-sub-user/', views.register_sub_user, name='register_sub_user'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('company-settings/', views.company_settings, name='company_settings'),

]