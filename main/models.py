from datetime import date
from unicodedata import name
from django.db import models
from numpy import positive

# Create your models here.

class BotFunctions (models.Model):
    name = models.TextField(db_column = 'name',null = False,verbose_name='Название функции')
    description = models.TextField(db_column = 'description',null = False,verbose_name='Описание функции')

    class Meta:
        verbose_name = "Описание функций"
    def __str__(self) -> str:
        return f"{self.name } - {self.description}"


class Dialogs(models.Model):
    user_msg = models.TextField(db_column = 'user_msg',null = False,verbose_name='Сообщение от пользователя')
    reply_msg = models.TextField(db_column = 'reply_msg',null = False,verbose_name='Ответ')
    positive = models.BooleanField(default = True,db_column = 'positive',null = False,verbose_name='Поизитивная или негативная фраза(True/False)')
    score = models.IntegerField(db_column = 'score',null = False,verbose_name='Очки')
    
    class Meta:
        verbose_name = "Фразы"
    def __str__(self) -> str:
        return f"{self.user_msg} - {self.reply_msg} - {self.positive} - {self.score}"

class Videos(models.Model):
    url = models.TextField(db_column = 'url',null = False,verbose_name='Ссылка на видео')
    tags = models.TextField(db_column = 'tags',null = False,verbose_name='тэг(для чила,животные,Смешные видео)')
    coment = models.TextField(db_column = 'coment',null = True ,blank = True,verbose_name='коментарий к видео(не обязателен)')
    
    class Meta:
        verbose_name = "Видео"
    def __str__(self) -> str:
        return f"{self.url} - {self.tags} - {self.coment}"

class Pictures(models.Model):
    url = models.TextField(db_column = 'url',null = False,verbose_name='Ссылка на картинку')
    tags = models.TextField(db_column = 'tags',null = False,verbose_name='тэг(животные,пейзажи,смешнявка,пикчи,мои фоточки)')
    coment = models.TextField(db_column = 'coment',null = True ,blank = True,verbose_name='коментарий к картинке(не обязателен)')
    
    class Meta:
        verbose_name = "Картинки"
    def __str__(self) -> str:
        return f"{self.url} - {self.tags} - {self.coment}"

class Anime(models.Model):
    urls = models.TextField(db_column = 'urls',null = False,verbose_name='Ссылка на сайт с аниме(Aniu)')
    tags = models.TextField(db_column = 'tag',null = False,verbose_name='Жанр аниме')

    class Meta:
        verbose_name = "Аниме"
    def __str__(self) -> str:
        return f"{self.urls } - {self.tags}"