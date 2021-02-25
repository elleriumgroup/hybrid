from django.db import models

class SPR_F10R1(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name_plural = 'F1.0 R01 Органы'
        verbose_name = 'F1.0 R01 Орган'
        #db_table = 'spr_f10r1'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R1_ORGAN(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R01 Территориальный орган'
        verbose_name_plural = 'F1.0 R01 Территориальные органы'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R2(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R02 Учесть'
        verbose_name_plural = 'F1.0 R02 Учести'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R3(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R03 Вид'
        verbose_name_plural = 'F1.0 R03 Виды'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R3_GASORG(models.Model):
    code = models.CharField(max_length=8, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R03 ГАС ОРГАН'
        verbose_name_plural = 'F1.0 R03 ГАС ОРГАН'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R8(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R08 Преступление предотвращено'
        verbose_name_plural = 'F1.0 R08 Преступления предотвращены'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R7_1(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R7.1 Восстановлено на учет в числе ППЛ'
        verbose_name_plural = 'F1.0 R7.1 Восстановлены на учет в числе ППЛ'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

#r10.3=#r9=f1.1r34=f1.2r14=8112
class SPR_F10R9(models.Model):
    code = models.CharField(max_length=5, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R9 Преступление выявлено'
        verbose_name_plural = 'F1.0 R9 Преступления выявлены'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R9_1(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R9.1'
        verbose_name_plural = 'F1.0 R9.1'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R10(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R10'
        verbose_name_plural = 'F1.0 R10'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R10_1(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R10.1'
        verbose_name_plural = 'F1.0 R10.1'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R10_2(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R10.2'
        verbose_name_plural = 'F1.0 R10.2'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R11(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R11'
        verbose_name_plural = 'F1.0 R11'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R13(models.Model):
    code = models.CharField(max_length=5, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R13 Квалификация'
        verbose_name_plural = 'F1.0 R13 Квалификации'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R15(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R15 Тяжесть'
        verbose_name_plural = 'F1.0 R15 Тяжести'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R16(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R16 Стадия совершения'
        verbose_name_plural = 'F1.0 R16 Стадии совершения'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R17(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R17'
        verbose_name_plural = 'F1.0 R17'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R18(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R18'
        verbose_name_plural = 'F1.0 R18'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R19_1(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R19_1'
        verbose_name_plural = 'F1.0 R19_1'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R19_2(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R19_2'
        verbose_name_plural = 'F1.0 R19_2'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R19_3(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R19_3'
        verbose_name_plural = 'F1.0 R19_3'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R20(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R20'
        verbose_name_plural = 'F1.0 R20'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R21(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R21'
        verbose_name_plural = 'F1.0 R21'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R21_1(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R21.1'
        verbose_name_plural = 'F1.0 R21.1'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R22(models.Model):
    code = models.CharField(max_length=5, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R22 Отрасль'
        verbose_name_plural = 'F1.0 R22 Отрасли'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R23(models.Model):
    code = models.CharField(max_length=5, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R23'
        verbose_name_plural = 'F1.0 R23'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R24(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R24'
        verbose_name_plural = 'F1.0 R24'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R25(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R25 Код причиненного ущерба'
        verbose_name_plural = 'F1.0 R25 Код причиненного ущерба'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R25_1(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R25.1 Код наркотических средств'
        verbose_name_plural = 'F1.0 R25.1 Код наркотических средств'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R26(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R26 Способ совершения'
        verbose_name_plural = 'F1.0 R26 Способы совершения'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R27(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R27 Дополнительная характеристика'
        verbose_name_plural = 'F1.0 R27 Дополнительные характеристики'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R28(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R28 Совершено с приминением'
        verbose_name_plural = 'F1.0 R28 Совершены с принимением'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R29(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R29 Характеристика охраны объекта'
        verbose_name_plural = 'F1.0 R29 Характеристика охраны объекта'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R29_1(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R29.1 Результаты осмотра места происшествия'
        verbose_name_plural = 'F1.0 R29.1 Результаты осмотра места происшествия'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R32(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R32 Личность потерпевшего не установена'
        verbose_name_plural = 'F1.0 R32 Личность потерпевшего не установена'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R33(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R33 Характеристика потерпевших'
        verbose_name_plural = 'F1.0 R33 Характеристика потерпевших'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name
#f1r34=f11r23=8192
class SPR_F10R34(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R34 Социальное положение'
        verbose_name_plural = 'F1.0 R34 Социальное положение'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name
#f1r36=f1r37=f11r18=f11r18.1=f11r19=516
class SPR_F10R36(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    ordering = ['code']
    class Meta:
        verbose_name = 'F1.0 R36 Гражданство'
        verbose_name_plural = 'F1.0 R36 Гражданство'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R38(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R38 Цель приезда'
        verbose_name_plural = 'F1.0 R38 Цель приезда'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R40(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R40 В производстве'
        verbose_name_plural = 'F1.0 R40 В производстве'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

# Статистическая карточка Форма 1.1
class SPR_F11R9(models.Model):
    code = models.CharField(max_length=5, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R09 Преступление совершено неоднократно'
        verbose_name_plural = 'F1.1 R09 Преступление совершено неоднократно'
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R10(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R10 Характеристика группы'
        verbose_name_plural = 'F1.1 R10 Характеристика группы'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R11(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R11 Характеристика связей группы'
        verbose_name_plural = 'F1.1 R11 Характеристика связей группы'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R12(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R12 Характеристика лица'
        verbose_name_plural = 'F1.1 R12 Характеристика лица'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R13(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R13 В состоянии опьянения'
        verbose_name_plural = 'F1.1 R13 В состоянии опьянения'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R14(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R14 Ранее совершавшим'
        verbose_name_plural = 'F1.1 R14 Ранее совершавшим'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R15(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R15 Ранее судимым'
        verbose_name_plural = 'F1.1 R15 Ранее судимым'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R16(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R16 Рецидив преступления'
        verbose_name_plural = 'F1.1 R16 Рецидив преступления'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R17(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R17 Преступление совершено обвиняемым'
        verbose_name_plural = 'F1.1 R17 Преступление совершено обвиняемым'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R20(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R20 Место проживания'
        verbose_name_plural = 'F1.1 R20 Место проживания'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R21(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R21 Цель приезда'
        verbose_name_plural = 'F1.1 R21 Цель приезда'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R22(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R22 Национальность'
        verbose_name_plural = 'F1.1 R22 Национальности'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R25(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R25 Решение по преступлению'
        verbose_name_plural = 'F1.1 R25 Решения по преступлениям'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R26(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R26 Мотив'
        verbose_name_plural = 'F1.1 R26 Мотивы'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R27(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R27 Преступление выявлено'
        verbose_name_plural = 'F1.1 R27 Преступление выявлено'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R28(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R28 Код ущерба'
        verbose_name_plural = 'F1.1 R28 Код ущерба'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R30(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R30 Технические средства снятия информации'
        verbose_name_plural = 'F1.1 R30 Технические средства снятия информации'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R31(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R31 Примененние криминалистических средств и методов'
        verbose_name_plural = 'F1.1 R31 Примененние криминалистических средств и методов'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R32(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R32 Использование АБД, ИПС'
        verbose_name_plural = 'F1.1 R32 Использование АБД, ИПС'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R32_1(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R32.1 Использование аппаратно-программных средств'
        verbose_name_plural = 'F1.1 R32.1 Использование аппаратно-программных средств'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R33(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R33 Уголовное дело расследовано'
        verbose_name_plural = 'F1.1 R33 Уголовное дело расследовано'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R35_1(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R35_1 Сообщение'
        verbose_name_plural = 'F1.1 R35_1 Сообщение'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R35_2(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R35_2 Сообщение'
        verbose_name_plural = 'F1.1 R35_2 Сообщение'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R35_3(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R35_3 Сообщение'
        verbose_name_plural = 'F1.1 R35_3 Сообщение'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F11R36(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.1 R36 Применялся'
        verbose_name_plural = 'F1.1 R36 Применялся'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F12R9(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.2 R9 Лицо задержано в порядке'
        verbose_name_plural = 'F1.2 R9 Лицо задержано в порядке'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F12R10(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.2 R10 Лицу, совершившему преступление предъявлено обвинение'
        verbose_name_plural = 'F1.2 R10 Лицу, совершившему преступление предъявлено обвинение'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F12R11(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.2 R11 В отношении обвиняемого избраны меры пресечения'
        verbose_name_plural = 'F1.2 R11 В отношении обвиняемого избраны меры пресечения'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F12R13(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.2 R13 УД находится в производстве'
        verbose_name_plural = 'F1.2 R13 УД находится в производстве'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F12R14_1(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.2 R14.1 Установлено отедалми УУР УМВД'
        verbose_name_plural = 'F1.2 R14.1 Установлено отедалми УУР УМВД'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F10R51(models.Model):
    code = models.CharField(max_length=4, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F1.0 R51 Административный участок'
        verbose_name_plural = 'F1.0 R51 Административные участки'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

# Форма 2
class SPR_F2R10(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F2 R10 Пол'
        verbose_name_plural = 'F2 R10 Пол'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F2R12(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F2 R12 Образование'
        verbose_name_plural = 'F2 R12 Образование'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F2R15(models.Model):
    code = models.CharField(max_length=1, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F2 R15 Место проживания'
        verbose_name_plural = 'F2 R15 Место проживания'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name

class SPR_F2R16(models.Model):
    code = models.CharField(max_length=2, unique=True, verbose_name='Код')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    class Meta:
        verbose_name = 'F2 R16 Цель приезда'
        verbose_name_plural = 'F2 R16 Цель приезда'
        ordering = ['code']
    def __str__(self):
        return self.code + ' | ' + self.name
