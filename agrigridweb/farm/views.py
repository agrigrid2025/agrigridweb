from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FarmForm
from users.models import Company
from .models import Farm
from django.http import JsonResponse
import json

@login_required
def create_farm(request):
    if request.user.profile.role != 'admin':
        return redirect('dashboard')

    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.manager = request.user
            farm.save()
            form.save_m2m()
            return redirect('farm_map', farm_id=farm.id)
    else:
        form = FarmForm()

    return render(request, 'farm/create_farm.html', {'form': form})

@login_required
def farm_map(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    return render(request, 'farm/farm_map.html', {'farm': farm})

@login_required
def save_farm_boundary(request, farm_id):
    if request.method == 'POST':
        farm = get_object_or_404(Farm, id=farm_id)
        data = json.loads(request.body)
        farm.boundary_geojson = json.dumps(data['geojson'])
        farm.save()
        return JsonResponse({'status': 'success'})

@login_required
def farm_map(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    company = Company.objects.filter(owner=request.user).first()
    api_key = company.google_maps_api_key if company else ''
    return render(request, 'farm/farm_map.html', {'farm': farm, 'api_key': api_key})
