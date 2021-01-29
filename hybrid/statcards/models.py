from django.db import models

# Create your models here.
class SPR_F10R1(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R01 Орган'
        verbose_name_plural = 'F1.0 R01 Органы'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R1_ORGAN(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R01 Территориальный орган'
        verbose_name_plural = 'F1.0 R01 Территориальные органы'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R2(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R02 Учесть'
        verbose_name_plural = 'F1.0 R02 Учести'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R3(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R03 Вид'
        verbose_name_plural = 'F1.0 R03 Виды'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R3_GASORG(models.Model):
    code = models.CharField(max_length=8, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R03 ГАС ОРГАН'
        verbose_name_plural = 'F1.0 R03 ГАС ОРГАН'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R8(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R08 Преступление предотвращено'
        verbose_name_plural = 'F1.0 R08 Преступления предотвращены'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R25(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R25 Решение по преступлению'
        verbose_name_plural = 'F1.1 R25 Решения по преступлениям'
    def __str__(self):
        return self.code + ' | ' + self.name