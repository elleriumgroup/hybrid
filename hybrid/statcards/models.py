from django.db import models

# Create your models here.
class SPR_F10R1(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0R01 Орган'
        verbose_name_plural = 'F1.0R01 Органы'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R1_ORGAN(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0R01 Территориальный орган'
        verbose_name_plural = 'F1.0R01 Территориальные органы'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R2(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0R02 Учесть'
        verbose_name_plural = 'F1.0R02 Учести'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R3(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0R03 Вид'
        verbose_name_plural = 'F1.0R03 Виды'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R3_GASORG(models.Model):
    code = models.CharField(max_length=8, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0R03 ГАС ОРГАН'
        verbose_name_plural = 'F1.0R03 ГАС ОРГАН'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R8(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0R08 Преступление предотвращено'
        verbose_name_plural = 'F1.0R08 Преступления предотвращены'
    def __str__(self):
        return self.code + ' | ' + self.name

