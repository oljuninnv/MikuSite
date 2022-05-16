from django.contrib import admin
from .models import BotFunctions,Dialogs,Videos,Pictures
# Register your models here.
@admin.register(BotFunctions)
class BFAdmin(admin.ModelAdmin):
    search_fields = ['name__startswitch','description__startswitch']

@admin.register(Dialogs)
class DialogsAdmin(admin.ModelAdmin):
    search_fields = ['user_msg__startswitch','reply_msg__startswitch','score__startswitch']

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    search_fields = ['url__startswitch','tags__startswitch','coment__startswitch']

@admin.register(Pictures)
class PicturesAdmin(admin.ModelAdmin):
    search_fields = ['url__startswitch','tags__startswitch','coment__startswitch']
    