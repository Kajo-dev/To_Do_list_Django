from curses import def_prog_mode
from pyexpat import model
from django.db import models

class Taski(models.Model):
    nazwa=models.CharField(
        max_length=50,
    )
    godzina_rozpoczencia=models.CharField(
        max_length=5
    )
    czas_przeznaczony=models.CharField(
        max_length=5
    )
    OSOBISTE='Osobiste'
    PRACA='Praca'
    SZKOLA='Szkoła'
    kat=[(OSOBISTE,'Osobiste'),(PRACA,'Praca'),(SZKOLA,'Szkoła')]
    kategorie=models.CharField(
        max_length=10,
        choices=kat,
        default=OSOBISTE
    )

