from django import forms

from .models import Request


class FeedbackForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=100, required=False)
    phone = forms.CharField(label="Телефон", max_length=100, required=False)
    email = forms.CharField(label="Email", max_length=100, required=False)
    message = forms.CharField(label="Сообщение", max_length=800, required=False)

    class Meta:
        model = Request

        fields = [
            'name',
            'phone',
            'email',
            'message',
        ]


class RequestForm(forms.Form):
    waist = forms.CharField(label="Талия", max_length=100)
    hips = forms.CharField(label="Бёдра", max_length=100)
    hand = forms.CharField(label="Рука", max_length=100)
    chest = forms.CharField(label="Грудь", max_length=100)
    height = forms.CharField(label="Рост", max_length=100)

    class Meta:
        model = Request

        fields = [
            'waist',
            'hips',
            'hand',
            'chest',
            'height',
        ]
