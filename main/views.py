from django.shortcuts import render
from django.http import HttpResponse
from .models import BotFunctions
from django.core.mail import send_mail
# Create your views here.

def index(request):
    functions = BotFunctions.objects.values()
    return render(request,'main/index.html',{'functions':functions})

def about(request):
    return render(request,'main/about_us.html')

def send_email(request):
    message = request.POST.get('message')
    user = request.POST.get('username')
    email = request.POST.get("email")
    send_mail(
    'Новое сообщение!',
    f'Обратная связь с пользователями сайта\n от кого: {user}, email : {email}\n сообщение: {message}',
    'e5608nn9@miku-bot.ru',
    ['kupryashin014@gmail.com','5608nik@mail.ru']
)
    return HttpResponse("<h1>Сообщение отправлено!</h1>")