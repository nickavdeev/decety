# -*- coding: utf-8 -*-

from django.shortcuts import render
from .forms import FeedbackForm, RequestForm
from .models import Feedback
import telebot


bot = telebot.TeleBot('1315028179:AAHLtGJ8nJnlN_Dqo-l3l3m0dibfY0SOYFc')


def index(request):
    default_parameters = {'waist': '115', 'thighs': '125',
                          'biceps': '40', 'chest': '120',
                          'height': '175', 'parameters_display': 'block',
                          'hide_display': 'inline', 'show_display': 'none'}
    return render(request, 'main/index.html', default_parameters)


def done(request):
    form = FeedbackForm(request.POST)

    if form.is_valid():
        new_request = Feedback()
        new_request.name = form.cleaned_data['name']
        new_request.phone = form.cleaned_data['phone']
        new_request.email = form.cleaned_data['email']
        new_request.message = form.cleaned_data['message']
        new_request.save()

        message = f'<b>Новое сообщение с сайта!</b>\n\n'\
                  f'Имя: {new_request.name}\n'\
                  f'Email: {new_request.email}\n'\
                  f'Телефон: {new_request.phone}\n'\
                  f'Сообщение: {new_request.message}'

        bot.send_message(404417823, message, parse_mode='HTML')
        bot.send_message(399776232, message, parse_mode='HTML')

    return render(request, 'main/done.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def how_it_works(request):
    return render(request, 'main/how-it-works-dev.html')
    # return render(request, 'main/how-it-works.html')


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


def testing_gucci(request):
    default_parameters = {'waist': '115', 'thighs': '125',
                          'biceps': '40', 'chest': '120',
                          'height': '175', 'parameters_display': 'block',
                          'hide_display': 'inline', 'show_display': 'none'}
    if request.method == 'POST':
        return render(request, 'main/testing-gucci.html', default_parameters)

    elif request.method == 'GET':
        data = request.GET
        if len(data) == 0:
            return render(request, 'main/testing-gucci.html', default_parameters)
        else:
            return render(request, 'main/testing-gucci.html',
                          {'waist':     data['waist'],
                           'thighs':    data['thighs'],
                           'biceps':    data['biceps'],
                           'chest':     data['chest'],
                           'height':    data['height'],
                           'parameters_display':   'none',
                           'hide_display': 'none', 'show_display': 'inline'})
    else:
        form = RequestForm()

    return render(request, '../templates/main/testing-gucci.html', {'form': form})


def testing_new_balance(request):
    default_parameters = {'waist': '115', 'thighs': '125',
                          'biceps': '40', 'chest': '120',
                          'height': '175', 'parameters_display': 'block',
                          'hide_display': 'inline', 'show_display': 'none'}
    if request.method == 'POST':
        return render(request, 'main/testing-new-balance.html', default_parameters)

    elif request.method == 'GET':
        data = request.GET
        if len(data) == 0:
            return render(request, 'main/testing-new-balance.html', default_parameters)
        else:
            return render(request, 'main/testing-new-balance.html',
                          {'waist':     data['waist'],
                           'thighs':    data['thighs'],
                           'biceps':    data['biceps'],
                           'chest':     data['chest'],
                           'height':    data['height'],
                           'parameters_display':   'none',
                           'hide_display': 'none', 'show_display': 'inline'})
    else:
        form = RequestForm()

    return render(request, '../templates/main/testing-new-balance.html', {'form': form})
