from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def dashboard(request):
    # Ensure profile exists
    profile, created = Profile.objects.get_or_create(user=request.user)

    if not profile.is_complete:
        return redirect('complete_profile')

    return render(request, 'users/dashboard.html', {'user': request.user})


@login_required
def complete_profile(request):
    profile = request.user.profile
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            # Save user fields
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            # Save profile fields
            profile = form.save(commit=False)
            profile.is_complete = True
            profile.save()

            return redirect('dashboard')
    else:
        form = ProfileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'company_name': profile.company_name,
            'abn_number': profile.abn_number,
            'address': profile.address,
            'phone_number': profile.phone_number,
        })

    return render(request, 'users/complete_profile.html', {'form': form})

@login_required
def edit_profile(request):
    profile = request.user.profile
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            profile = form.save(commit=False)
            profile.save()

            return redirect('dashboard')
    else:
        form = ProfileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'company_name': profile.company_name,
            'abn_number': profile.abn_number,
            'address': profile.address,
            'phone_number': profile.phone_number,
        })

    return render(request, 'users/edit_profile.html', {'form': form})

