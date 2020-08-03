from django import forms

from .models import Request


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
