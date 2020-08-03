from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import RequestForm


def index(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def how_it_works(request):
    return render(request, 'main/how-it-works.html')


def testing(request):
    return render(request, 'main/testing.html')


def get_parameters(request):
    if request.method == 'POST':
        data = request.POST
        print(data)

        return HttpResponseRedirect('#clothing-test')

    else:
        form = RequestForm()

    return render(request, '../templates/main/testing.html', {'form': form})
