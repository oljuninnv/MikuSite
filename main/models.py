from datetime import date
from unicodedata import name
from django.db import models

# Create your models here.

class BotFunctions (models.Model):
    name = models.TextField(db_column = 'name',null = False,verbose_name='Название функции')
    description = models.TextField(db_column = 'description',null = False,verbose_name='Описание функции')

    class Meta:
        verbose_name = "Описание функций"
    def __str__(self) -> str:
        return f"{self.name } - {self.description}"