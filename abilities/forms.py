from django import forms


class AbilityForm(forms.Form):
    label = forms.CharField(label="Compétence", max_length=100)
    activity = forms.CharField(label="Activité", max_length=100)