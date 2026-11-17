from django.contrib import admin

from .models import Ability
from .models import Schedule

admin.site.register(Ability)
admin.site.register(Schedule)