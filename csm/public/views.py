from django.shortcuts import render


def home(request):
    return render(request, 'public/home.html')


def no_rights(request):
    return render(request, 'public/no_rights.html')
