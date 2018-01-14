from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Country (models.Model):
    cnt_name = models.CharField(max_length=100)
    hotel_name = models.CharField(max_length=100)


class Hotel(models.Model):
    id_hotel = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=45, verbose_name='Название отеля')
    photo = models.ImageField(null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.hotel_name

    class Meta:
        verbose_name_plural = "Отели"
        verbose_name = "Отель"

    def get_hotel_name(self):
        return [u.username for u in self.hotel_name.all()]
    get_hotel_name.short_description = 'Названия отелей'


class Nomer(models.Model):
    id_nomera = models.AutoField(primary_key=True)
    kod_nomera = models.CharField(max_length=45, verbose_name='Код номера')
    hotell = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Отель')

    def __str__(self):
        return '%s %s %s' % (self.id_nomera, self.kod_nomera, self.hotell)

    # def natural_key(self):
    #     return '%s %s %s' % (self.hotell, self.kod_nomera, self.patronymic)

    class Meta:
        verbose_name_plural = "Номера"
        verbose_name = "Номер"


class Registr(models.Model):
    id_registr = models.AutoField(primary_key=True)
    code_registr = models.CharField(max_length=45, verbose_name='Код регистрации')
    nomer_registr = models.ForeignKey(Nomer, on_delete=models.CASCADE, verbose_name='Выбранная комната')

    def __str__(self):
        return self.code_registr

    def natural_key(self):
        return '%s' % (self.nomer_registr)

    class Meta:
        verbose_name_plural = "Регистрации"
        verbose_name = "Регистрация"

    def get_registr(self):
        return [r.code_registr for r in self.code_registr.all()]
    get_registr.short_description = 'Все номера брони'



class Human(models.Model):
    id_human = models.AutoField(primary_key=True)
    fio = models.CharField(max_length=100, blank=False, null=False, verbose_name='ФИО')
    registr_code = models.ManyToManyField(Registr, verbose_name='Код регистрации')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"

    def get_registr_code(self):
        return [r.code_registr for r in self.registr_code.all()]
    get_registr_code.short_description = 'Номера брони'


