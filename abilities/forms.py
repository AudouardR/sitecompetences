from django import forms

from abilities.models import Ability


class AbilityForm(forms.Form):
    label = forms.CharField(label="Compétence", max_length=100)
    activity = forms.CharField(label="Activité", max_length=100)

class ScheduleForm(forms.Form):
    ability = forms.ModelChoiceField(label="Compétence", queryset=Ability.objects.all())
    date = forms.DateField(label="Date")

class UserAbilitiesForm(forms.Form):
    abilities = forms.ModelMultipleChoiceField(
        label="Compétences maîtrisées",
        queryset=Ability.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )