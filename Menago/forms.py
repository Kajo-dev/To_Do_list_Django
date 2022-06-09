from dataclasses import fields
from django import forms
from .models import Taski

class TaskiWyswietlanie(forms.ModelForm):
    class Meta:
        model=Taski
        fields=[
            'nazwa',
            'godzina_rozpoczencia',
            'czas_przeznaczony',
            'kategorie',
        ]