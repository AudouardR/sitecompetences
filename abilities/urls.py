from django.urls import path

from . import views

urlpatterns = [
    # ex: /abilities/
    path("", views.index, name="index"),

    # ex: /abilities/ability/2/
    path("ability/<int:ability_id>/", views.show_ability, name="show_ability"),
    # ex: /abilities/ability/create/
    path("ability/create/", views.create_ability, name="create_ability"),
    # ex: /abilities/ability/save/
    path("ability/save/", views.save_ability, name="save_ability"),
    # ex: /abilities/ability/2/edit/
    path("ability/<int:ability_id>/edit/", views.edit_ability, name="edit_ability"),
    # ex: /abilities/ability/2/update/
    path("ability/<int:ability_id>/update/", views.update_ability, name="update_ability"),
    # ex: /abilities/ability/2/delete/
    path("ability/<int:ability_id>/delete/", views.delete_ability, name="delete_ability"),

    # ex: /abilities/schedule/1/
    path("schedule/<int:schedule_id>/", views.show_schedule, name="show_schedule"),
    # ex: /abilities/schedule/create/
    path("schedule/create/", views.create_schedule, name="create_schedule"),
    # ex: /abilities/schedule/save/
    path("schedule/save/", views.save_schedule, name="save_schedule"),
    # ex: /abilities/schedule/2/edit/
    path("schedule/<int:schedule_id>/edit/", views.edit_schedule, name="edit_schedule"),
    # ex: /abilities/schedule/2/update/
    path("schedule/<int:schedule_id>/update/", views.update_schedule, name="update_schedule"),
    # ex: /abilities/schedule/2/delete/
    path("schedule/<int:schedule_id>/delete/", views.delete_schedule, name="delete_schedule"),
]