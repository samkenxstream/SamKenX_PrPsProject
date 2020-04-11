import datetime
from django.db import models
from django.utils import timezone


class table(models.Model):
    name = models.CharField('name', max_length=36)
    surname = models.CharField('surname', max_length=36)
    city = models.CharField('city', max_length=36)
    rented_rooms = models.IntegerField(0)
    #publication_date = models.DateTimeField("text") ###


    # def added_last_week(self):
    #     return self.publication_date >= (timezone.now() - datetime.timedelta(date=7))
    #
    # def added_last_day(self):
    #     return self.publication_date >= (timezone.now() - datetime.timedelta(date=1))
    #
    # def added_last_30days(self):
    #     return self.publication_date >= (timezone.now() - datetime.timedelta(date=30))

    class Meta:
        verbose_name = "Таблица"
        verbose_name_plural = "Таблицы"



