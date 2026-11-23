from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # ex: /abilities/
    path("", views.index, name="index"),

    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),

    path("signup/", views.SignUpView.as_view(), name="signup"),

    # ex: /abilities/accounts/audouardr/
    path('accounts/<str:username>/', views.profile_view, name='profile_view'),
    # ex: /abilities/accounts/audouardr/select-abilities
    path('accounts/<str:username>/select-abilities', views.select_abilities, name='select_abilities'),
    # ex: /abilities/accounts/audouardr/confirm-abilities
    path('accounts/<str:username>/confirm-abilities', views.confirm_abilities, name='confirm_abilities'),

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
    # ex: /abilities/schedule/2/apply/
    path("schedule/<int:schedule_id>/apply/", views.apply_for_schedule, name="apply_for_schedule"),
    # ex: /abilities/schedule/2/accept/
    path("schedule/<int:schedule_id>/accept/", views.accept_application, name="accept_application"),
    # ex: /abilities/schedule/2/refuse/
    path("schedule/<int:schedule_id>/refuse/", views.refuse_application, name="refuse_application"),
]