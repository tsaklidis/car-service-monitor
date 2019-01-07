from django.shortcuts import render


def home(request):
    print 'public home here'
    return render(request, 'public/home.html')
