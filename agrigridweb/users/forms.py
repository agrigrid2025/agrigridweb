import pytz


from django.contrib.auth.forms import UserCreationForm
from .models import Company
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ['company_name', 'abn_number', 'address', 'phone_number']

class SubUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CompanyForm(forms.ModelForm):
    time_zone = forms.ChoiceField(
        choices=[(tz, tz) for tz in pytz.common_timezones],
        required=True
        
    )

    google_maps_api_key = forms.CharField(required=False)

    class Meta:
        model = Company
        fields = [
            'name', 'abn_number', 'address_line_1', 'address_line_2',
            'city', 'postal_code', 'country', 'email', 'phone_number',
            'unit_of_measure', 'time_zone', 'google_maps_api_key'
        ]
        