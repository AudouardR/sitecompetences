from django.urls import path

from . import views

urlpatterns = [
    # ex: /abilities/
    path("", views.index, name="index"),
    # ex: /abilities/ability/2/
    path("/ability/<int:ability_id>/", views.detail_ability, name="detail_ability"),
    # ex: /abilities/schedule/1/
    path("/schedule/<int:schedule_id>/", views.detail_schedule, name="detail_schedule"),
]