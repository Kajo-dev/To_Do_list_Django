from curses import def_prog_mode
from pyexpat import model
from django.db import models

class Taski(models.Model):
    nazwa=models.CharField(
        max_length=30,
    )
    godzina_rozpoczencia=models.CharField(
        max_length=5
    )
    czas_przeznaczony=models.CharField(
        max_length=5
    )
    

