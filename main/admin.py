from django.contrib import admin
from .models import BotFunctions
# Register your models here.
@admin.register(BotFunctions)
class BFAdmin(admin.ModelAdmin):
    search_fields = ['name__startswitch','description__startswitch']

    