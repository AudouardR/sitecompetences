from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from .models import Schedule, Ability


@require_GET
def index(request):
    schedule_list = Schedule.objects.all()
    context = {"schedule_list": schedule_list}
    return render(request, "abilities/index.html", context)

# Compétences

@require_GET
def show_ability(request, ability_id):
    ability = get_object_or_404(Ability, pk=ability_id)
    return render(request, "abilities/ability/show.html", {"ability": ability})

@require_GET
def create_ability(request):
    return HttpResponse("You're creating a new ability.")

@require_POST
def save_ability(request):
    return HttpResponse("You're saving a new ability.")

@require_GET
def edit_ability(request, ability_id):
    return HttpResponse("You're editing ability %s." % ability_id)

@require_POST
def update_ability(request, ability_id):
    return HttpResponse("You're updating ability %s." % ability_id)

@require_POST
def delete_ability(request, ability_id):
    return HttpResponse("You're deleting ability %s." % ability_id)

# Créneaux

@require_GET
def show_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    return render(request, "abilities/schedule/show.html", {"schedule": schedule})

@require_GET
def create_schedule(request):
    return HttpResponse("You're creating a new schedule.")

@require_POST
def save_schedule(request):
    return HttpResponse("You're saving a new schedule.")

@require_GET
def edit_schedule(request, schedule_id):
    return HttpResponse("You're editing schedule %s." % schedule_id)

@require_POST
def update_schedule(request, schedule_id):
    return HttpResponse("You're updating schedule %s." % schedule_id)

@require_POST
def delete_schedule(request, schedule_id):
    return HttpResponse("You're deleting schedule %s." % schedule_id)