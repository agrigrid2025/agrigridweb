from django import forms
from .models import Farm
from django.contrib.auth.models import User

class FarmForm(forms.ModelForm):
    sub_users = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(profile__role='member'),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Farm
        fields = ['name', 'address', 'sub_users']