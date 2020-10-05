from django.shortcuts import render

from .forms import RequestForm


def index(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def how_it_works(request):
    return render(request, 'main/how-it-works.html')


def testing(request):
    default_parameters = {'waist': '115', 'thighs': '125',
                          'biceps': '40', 'chest': '120',
                          'height': '175', 'parameters_display': 'block',
                          'hide_display': 'inline', 'show_display': 'none'}
    if request.method == 'POST':
        return render(request, 'main/testing.html', default_parameters)

    elif request.method == 'GET':
        data = request.GET
        if len(data) == 0:
            return render(request, 'main/testing.html', default_parameters)
        else:
            return render(request, 'main/testing.html',
                          {'waist':     data['waist'],
                           'thighs':    data['thighs'],
                           'biceps':    data['biceps'],
                           'chest':     data['chest'],
                           'height':    data['height'],
                           'parameters_display':   'none',
                           'hide_display': 'none', 'show_display': 'inline'})
    else:
        form = RequestForm()

    return render(request, '../templates/main/testing.html', {'form': form})
