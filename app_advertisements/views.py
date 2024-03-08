from django.shortcuts import render
from math import log
from datetime import date
from .forms import TaskForm


def index(request):
    advertisements = {
        'adv_1': {
            'title': 'Куплю кота',
            'description': 'Милый Касперочек',
            'created_at': date(2024, 2, 28),
            'price': 99999999,
            'image_url': 'img/cat.jpg'
        },
        'adv_2': {
            'title': 'Продам гараж',
            'description': 'Гараж на улице Пушкина, дом колотушкина',
            'created_at': date(2024, 2, 29),
            'price': 9874556,
            'image_url': 'https://gas-kvas.com/grafic/uploads/posts/2023-09/1695976337_gas-kvas-com-p-kartinki-garazh-35.jpg'
        }
    }

    return render(request, 'index.html', context=advertisements)


def top_sellers(request):
    return render(request, 'top-sellers.html')


def about(request):
    context = {
        'me': {
            'name': 'Тирская Карина Юрьевна',
            'phone': '+79101488035',
            'email': 'cari.tirskaya@ya.ru',
            'image_url': 'https://sun9-6.userapi.com/impg/DGS_WvPFlCHt5qJirCn8ZVTYgQ4-FlOFU4LeHg/r_G5UxRf9cU.jpg?size=1439x2160&quality=95&sign=ea101344feea7d1316251b584aae64e0&type=album'
        },
        'program': {
            'name': 'Фундаментальная математика',
            'description': 'Экономика должна быть экономной',
            'head': {
                'name': '',
                'email': '',
                'image_url': ''
            },
            'manager': {
                'name': '',
                'email': '',
                'image_url': ''
            }
        },
        'pal1': {
            'name': 'Куцев Владимир',
            'phone': '+79858940010',
            'mail': 'vmkutsev@edu.hse.ru',
            'imgurl': 'https://upload.wikimedia.org/wikipedia/commons/6/6c/1Dog-rough-collie-portrait.jpg'
        },
        'pal2': {
            'name': 'Ермаков Тимур',
            'phone': '+79167777070',
            'mail': 'termakov@edu.hse.ru',
            'imgurl': 'https://upload.wikimedia.org/wikipedia/commons/0/0c/Парагвайская_анаконда_в_Гродно.JPG'
        },
    }
    return render(request, 'about.html', context=context)


def task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data["x"]
            y = form.cleaned_data["y"]
            return answer(request, x, y)
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'task.html', context=context)


def answer(request, x, y):
    z = x * y if x > y else log(x + y)
    context = {
        'z': z,
        'x': x,
        'y': y
    }
    return render(request, 'answer.html', context=context)
