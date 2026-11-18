from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST

from .forms import AbilityForm, ScheduleForm
from .models import Schedule, Ability


@require_GET
def index(request):
    schedule_list = Schedule.objects.all()
    ability_list = Ability.objects.all()
    context = {"schedule_list": schedule_list, "ability_list": ability_list}
    return render(request, "abilities/index.html", context)

# Compétences

@require_GET
def show_ability(request, ability_id):
    ability = get_object_or_404(Ability, pk=ability_id)
    return render(request, "abilities/ability/show.html", {"ability": ability})

@require_GET
def create_ability(request):
    if request.user.is_authenticated:
        form = AbilityForm()
        return render(request, "abilities/ability/create.html", {"form": form})
    else:
        return HttpResponseRedirect(reverse("index"))

@require_POST
def save_ability(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AbilityForm(request.POST)
            if form.is_valid():
                Ability.objects.create(label=form.cleaned_data["label"],
                                        activity=form.cleaned_data["activity"])
                return HttpResponseRedirect(reverse("index"))
        else:
            form = AbilityForm()

        return render(request, "abilities/ability/create.html", {"form": form})
    else:
        return HttpResponseRedirect(reverse("index"))

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
    if request.user.is_authenticated:
        form = ScheduleForm()
        return render(request, "abilities/schedule/create.html", {"form": form})
    else:
        return HttpResponseRedirect(reverse("index"))

@require_POST
def save_schedule(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ScheduleForm(request.POST)
            if form.is_valid():
                Schedule.objects.create(ability=form.cleaned_data["ability"],
                                       client=request.user, # Demandeur = utilisateur connecté
                                       accepted=0,
                                       date=form.cleaned_data["date"])
                return HttpResponseRedirect(reverse("index"))
        else:
            form = ScheduleForm()

        return render(request, "abilities/schedule/create.html", {"form": form})
    else:
        return HttpResponseRedirect(reverse("index"))

@require_GET
def edit_schedule(request, schedule_id):
    return HttpResponse("You're editing schedule %s." % schedule_id)

@require_POST
def update_schedule(request, schedule_id):
    return HttpResponse("You're updating schedule %s." % schedule_id)

@require_POST
def delete_schedule(request, schedule_id):
    return HttpResponse("You're deleting schedule %s." % schedule_id)