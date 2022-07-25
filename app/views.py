from django.http import HttpResponse
from django.shortcuts import reverse, render
from datetime import datetime
import os
#from django.urls import reverse


def home_view(request):
    template_name = 'app/home.html'
    time = 'app/home/current_time.html'
    workdir = 'app/home/workdir.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)






def time_view(request):
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    file = os.listdir()
    f = f'Список файлов {file}'
    return HttpResponse(f)
    raise NotImplemented


