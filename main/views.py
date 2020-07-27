from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def how_it_works(request):
    return render(request, 'main/how-it-works.html')


def testing(request):
    return render(request, 'main/testing.html')
