from django.db import models

# Create your models here.
class SPR_F10R1(models.Model):
    code = models.CharField(max_length=2, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Орган'
        verbose_name_plural = 'Органы'
    def __str__(self):
        self.name

class SPR_F10R1_ORGAN(models.Model):
    code = models.CharField(max_length=2, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'Территориальный орган'
        verbose_name_plural = 'Территориальные органы'
    def __str__(self):
        self.name

