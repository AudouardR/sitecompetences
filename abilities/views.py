from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST
from django.views.generic import CreateView

from .forms import AbilityForm, ScheduleForm, UserAbilitiesForm
from .models import Schedule, Ability, Profile

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "abilities/registration/signup.html"

@require_GET
def index(request):
    schedule_list = Schedule.objects.filter(date__gte=timezone.now()).order_by("date")
    ability_list = Ability.objects.all()
    context = {"schedule_list": schedule_list, "ability_list": ability_list}

    if request.user.is_authenticated:
        profile = Profile.objects.get(user__username=request.user.username)

        user_ability_list = profile.abilities.all()
        context["user_ability_list"] = user_ability_list

        proposed_schedule_list = (Schedule.objects.filter(accepted=False,
                                                         ability__in=user_ability_list,
                                                         date__gte=timezone.now())
                                  .exclude(client=profile.user).order_by("date"))
        context["proposed_schedule_list"] = proposed_schedule_list

        user_schedule_list = Schedule.objects.filter(client__username=request.user.username)
        context["user_schedule_list"] = user_schedule_list

        if request.user.is_superuser:
            outdated_schedule_list = Schedule.objects.filter(date__lte=timezone.now()).order_by("date")
            context["outdated_schedule_list"] = outdated_schedule_list

    return render(request, "abilities/index.html", context)

# Profils

@require_GET
def profile_view(request, username):
    profile = Profile.objects.get(user__username=username)
    return render(request, 'abilities/profile.html', {'profile': profile})

@require_GET
def select_abilities(request, username):
    profile = Profile.objects.get(user__username=username)

    if request.user.is_authenticated and (request.user.is_superuser or request.user.username == username):
        form = UserAbilitiesForm()
        return render(request, "abilities/user_abilities.html", {"form": form, 'profile': profile})
    else:
        return HttpResponseRedirect(reverse("index"))

@require_POST
def confirm_abilities(request, username):
    profile = Profile.objects.get(user__username=username)

    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == "POST":
            form = UserAbilitiesForm(request.POST)
            if form.is_valid():
                profile.abilities.set(form.cleaned_data["abilities"])
                profile.save()
                return HttpResponseRedirect(reverse("index"))
        else:
            form = ScheduleForm(initial={"abilities": profile.abilities})

        return render(request, "abilities/user_abilities.html", {"form": form, 'profile': profile})
    else:
        return HttpResponseRedirect(reverse("index"))

# Login



# Compétences

@require_GET
def show_ability(request, ability_id):
    ability = get_object_or_404(Ability, pk=ability_id)
    return render(request, "abilities/ability/show.html", {"ability": ability})

@require_GET
def create_ability(request):
    if request.user.is_authenticated and request.user.is_superuser:
        form = AbilityForm()
        return render(request, "abilities/ability/create.html", {"form": form})
    else:
        return HttpResponseRedirect(reverse("index"))

@require_POST
def save_ability(request):
    if request.user.is_authenticated and request.user.is_superuser:
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
    if request.user.is_authenticated and request.user.is_superuser:
        ability = get_object_or_404(Ability, pk=ability_id)
        form = AbilityForm(initial={"label": ability.label, "activity": ability.activity})
        return render(request, "abilities/ability/edit.html", {"form": form, "ability": ability})
    else:
        return HttpResponseRedirect(reverse("index"))

@require_POST
def update_ability(request, ability_id):
    ability = get_object_or_404(Ability, pk=ability_id)

    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == "POST":
            form = AbilityForm(request.POST)
            if form.is_valid():
                ability.label = form.cleaned_data["label"]
                ability.activity = form.cleaned_data["activity"]
                ability.save()
                return HttpResponseRedirect(reverse("index"))
        else:
            form = ScheduleForm(initial={"label": ability.label, "activity": ability.activity})

        return render(request, "abilities/ability/edit.html", {"form": form, "ability": ability})
    else:
        return HttpResponseRedirect(reverse("index"))

@require_POST
def delete_ability(request, ability_id):
    ability = get_object_or_404(Ability, pk=ability_id)
    if request.user.is_authenticated and request.user.is_superuser:

        if request.method == "POST":
            ability.delete()

    return HttpResponseRedirect(reverse("index"))

# Créneaux

@require_GET
def show_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    profile = Profile.objects.get(user__username=request.user.username)
    return render(request, "abilities/schedule/show.html", {"schedule": schedule, "profile": profile})

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
    if request.user.is_authenticated:
        schedule = get_object_or_404(Schedule, pk=schedule_id)
        form = ScheduleForm(initial={"ability": schedule.ability, "date": schedule.date})
        return render(request, "abilities/schedule/edit.html", {"form": form, "schedule": schedule})
    else:
        return HttpResponseRedirect(reverse("index"))

@require_POST
def update_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)

    if request.user.is_authenticated and (request.user.is_superuser or request.user == schedule.client):

        if request.method == "POST":
            form = ScheduleForm(request.POST)
            if form.is_valid():
                schedule.ability=form.cleaned_data["ability"]
                schedule.date=form.cleaned_data["date"]
                schedule.save()
                return HttpResponseRedirect(reverse("index"))
        else:
            form = ScheduleForm(initial={"ability": schedule.ability, "date": schedule.date})

        return render(request, "abilities/schedule/edit.html", {"form": form, "schedule": schedule})
    else:
        return HttpResponseRedirect(reverse("index"))

@require_POST
def delete_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    if request.user.is_authenticated and (request.user.is_superuser or request.user == schedule.client):

        if request.method == "POST":
            schedule.delete()

    return HttpResponseRedirect(reverse("index"))

@require_POST
def apply_for_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if request.method == "POST" and schedule.ability in profile.abilities:
            schedule.applicant = request.user
            schedule.save()

    return HttpResponseRedirect(reverse("index"))

@require_POST
def accept_application(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)

    if request.user.is_authenticated and (schedule.client == request.user) and schedule.applicant:
        if request.method == "POST":
            schedule.accepted = True
            schedule.save()

    return HttpResponseRedirect(reverse("index"))