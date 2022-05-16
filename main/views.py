from django.shortcuts import render
from django.http import HttpResponse
from .models import BotFunctions
# Create your views here.

def index(request):
    functions = BotFunctions.objects.values()
    return render(request,'main/index.html',{'functions':functions})

def about(request):
    return render(request,'main/about_us.html')