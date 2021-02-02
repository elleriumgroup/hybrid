from django.db import models

# Create your models here.
class SPR_F10R1(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name_plural = 'F1.0 R01 Органы'
        verbose_name = 'F1.0 R01 Орган'
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

class SPR_F10R7_1(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R7.1 Восстановлено на учет в числе ППЛ'
        verbose_name_plural = 'F1.0 R7.1 Восстановлены на учет в числе ППЛ'
    def __str__(self):
        return self.code + ' | ' + self.name

#r10.3=#r9=8112
class SPR_F10R9(models.Model):
    code = models.CharField(max_length=5, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R9 Преступление выявлено'
        verbose_name_plural = 'F1.0 R9 Преступления выявлены'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R9_1(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R9.1'
        verbose_name_plural = 'F1.0 R9.1'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R10(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R10'
        verbose_name_plural = 'F1.0 R10'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R10_1(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R10.1'
        verbose_name_plural = 'F1.0 R10.1'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R10_2(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R10.2'
        verbose_name_plural = 'F1.0 R10.2'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R11(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R11'
        verbose_name_plural = 'F1.0 R11'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R13(models.Model):
    code = models.CharField(max_length=5, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R13 Квалификация'
        verbose_name_plural = 'F1.0 R13 Квалификации'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R15(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R15 Тяжесть'
        verbose_name_plural = 'F1.0 R15 Тяжести'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R16(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R16'
        verbose_name_plural = 'F1.0 R16'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R17(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R17'
        verbose_name_plural = 'F1.0 R17'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R18(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R18'
        verbose_name_plural = 'F1.0 R18'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R19_1(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R19_1'
        verbose_name_plural = 'F1.0 R19_1'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R19_2(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R19_2'
        verbose_name_plural = 'F1.0 R19_2'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R19_3(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R19_3'
        verbose_name_plural = 'F1.0 R19_3'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R20(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R20'
        verbose_name_plural = 'F1.0 R20'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R21(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R21'
        verbose_name_plural = 'F1.0 R21'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R21_1(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R21.1'
        verbose_name_plural = 'F1.0 R21.1'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R22(models.Model):
    code = models.CharField(max_length=5, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R22 Отрасль'
        verbose_name_plural = 'F1.0 R22 Отрасли'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R23(models.Model):
    code = models.CharField(max_length=5, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R23'
        verbose_name_plural = 'F1.0 R23'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R24(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R24'
        verbose_name_plural = 'F1.0 R24'
    def __str__(self):
        return self.code + ' | ' + self.name



#r25k-8241
#r25.1k=8219
#r26-526
#r27-528
#r28-8113
#29-8205
#29.1-8114
#r32-8115
#r33-8116
#r33-8192
#r36-516
#r37-516
#r37-8117
#r40-8118

#форма 1.1
#r9-8119
#r10-8120
#r11-8121
#r12-8122
#13-8123
#14-8124
#15-8125
#16-8126
#17-8127
#18-516
#18.1-516
#19-516
#20-8128
#21-8129
#22-8128
#23-8192
#26-565
#27=8130
#28k-8131
#30-8132
#31-8133
#32-8134
#32.1-8139
#33-552
#34-8112
#35-8193-8194-8195
#35.1-8193
#36-8135

#форма 1.2

#r9-8136
#r10-255
#r11-8137
#r13-8138
#r14-8112
#14.1-8217
#r14.2-8135

