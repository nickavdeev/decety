from django.db import models


class Request(models.Model):
    waist = models.CharField("Талия", max_length=100)
    hips = models.CharField("Бёдра", max_length=100)
    hand = models.CharField("Рука", max_length=100)
    chest = models.CharField("Грудь", max_length=100)
    height = models.CharField("Рост", max_length=100)

    class Meta:
        verbose_name_plural = "Параметры"
        verbose_name = "Параметр"

    def __str__(self):
        return f'Запрос'
