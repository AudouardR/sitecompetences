import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Ability(models.Model):
    label = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class Schedule(models.Model):
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applicant', null=True, blank=True)
    accepted = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return (str(self.date) + " : " +
                str(self.ability.activity) +
                ", proposé par " +
                ((self.client.first_name + " " + self.client.last_name) if (self.client.first_name and self.client.last_name) else self.client.username))

    def is_in_the_past(self):
        return self.date < timezone.localdate()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    abilities = models.ManyToManyField(Ability, related_name='abilities_set', blank=True)
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return (self.user.first_name + " " + self.user.last_name) \
            if (self.user.first_name and self.user.last_name) \
            else self.user.username
