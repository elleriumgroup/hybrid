from django.db import models
from guide.models import *
# from guide.models import SPR_F10R1_ORGAN
# from guide.models import SPR_F10R2
# from guide.models import SPR_F10R1
# from guide.models import SPR_F10R51
# from guide.models import SPR_F10R3
# from guide.models import SPR_F10R3_GASORG



# Статистическая карточка Форма 1


# Форма 1-1.1-1.2 (полная)
class FORM1(models.Model):
    r01 = models.ForeignKey(SPR_F10R1, on_delete=models.CASCADE, verbose_name='Орган', blank=False)
    r01_organ = models.ForeignKey(SPR_F10R1_ORGAN, on_delete=models.CASCADE, verbose_name='Код органа', blank=False)
    r02 = models.ForeignKey(SPR_F10R2, on_delete=models.CASCADE, verbose_name='Учесть', blank=False)
    r51 = models.ForeignKey(SPR_F10R51, on_delete=models.CASCADE, verbose_name='Административный участок', blank=True, null=True)
    r03 = models.ForeignKey(SPR_F10R3, on_delete=models.CASCADE, verbose_name='Вид', blank=False)
    r03_year = models.CharField(max_length=4, verbose_name='Год', blank=False)
    r03_gasorg = models.ForeignKey(SPR_F10R3_GASORG, on_delete=models.CASCADE, verbose_name='Код терроргана ГАС', blank=False)
    r03_gasps = models.CharField(max_length=17, verbose_name='Номер УД', blank=False)
    r04 = models.CharField(max_length=2, verbose_name='Эпизод', blank=False)
    r05 = models.CharField(max_length=10, verbose_name='№ заявления', blank=True, null=True)
    r05_data = models.DateField(verbose_name='Дата регистрации заявления', blank=True, null=True)
    r05_delo_nomer = models.CharField(max_length=20, verbose_name='Дело №...', blank=True, null=True)
    r05_delo_post = models.CharField(max_length=100, verbose_name='поступило из...', blank=True, null=True)
    r05_delo_podsled = models.CharField(max_length=500, verbose_name='по подследственности из...', blank=True, null=True)
    d06 = models.DateField(verbose_name='Дата направления в ИЦ')
    d07 = models.DateField(verbose_name='Дата поступления в ИЦ')
    # ------ добавь новые поля
    r11 = models.DateField(verbose_name='Дата возбуждения УД', blank=False)
    class Meta:
        verbose_name = 'Статкарточка на выявленное преступление (ФОРМА 1)'
        verbose_name_plural = 'Статкарточки на выявленное преступление (ФОРМА 1)'
        indexes = [
            models.Index(fields=['r01', 'r02', 'r03_year', 'r03_gasorg', 'r04'], name='inx_form1_gasps')
        ]
    def __str__(self):
        return self.r03_gasps