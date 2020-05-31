from django.db import models


class Rooms(models.Model):
    country = models.CharField(verbose_name='country', max_length=50)
    city = models.CharField(verbose_name='city', max_length=50)
    street = models.CharField(verbose_name='street', max_length=50)
    house_number = models.PositiveIntegerField(verbose_name='house number')

    room_area = models.PositiveIntegerField(verbose_name='room area')
    basement_area = models.PositiveIntegerField(verbose_name='basement area')
    basement_ratio = models.PositiveSmallIntegerField(verbose_name='basement ratio')
    KT = models.PositiveSmallIntegerField(verbose_name='KT')
    author_id = models.PositiveIntegerField(verbose_name='author name', null=True, blank=True)
    tenant_email = models.CharField(verbose_name='tenant email', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = "Таблица помещений"
        verbose_name_plural = "Таблица помещений"


class Tenant(models.Model):
    name = models.CharField(verbose_name='name', max_length=50, default="")
    surname = models.CharField(verbose_name='surname', max_length=50, default="")
    middle_name = models.CharField(verbose_name='surname', max_length=50, default="")
    rented_rooms_count = models.PositiveIntegerField(verbose_name='rented rooms count')
    rented_room = models.ManyToManyField(Rooms, verbose_name='rented room')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Таблица арендаторов"
        verbose_name_plural = "Таблица арендаторов"
