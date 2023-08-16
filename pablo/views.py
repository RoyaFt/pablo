from django.http import HttpResponse
from django.shortcuts import render


def header(request, *args, **kwargs):
    context = {
        'test':'تست2'
    }
    return render(request, 'shared/Header.html', context)

def footer(request, *args, **kwargs):
    context = {
        'setting': 'setting'
    }
    return render(request, 'shared/Footer.html', context)


def home_page(request):

    return render (request,'home_page.html')

