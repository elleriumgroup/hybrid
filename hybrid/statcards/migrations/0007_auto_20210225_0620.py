# Generated by Django 3.1.5 on 2021-02-25 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
        ('statcards', '0006_spr_f2r10_spr_f2r12_spr_f2r15_spr_f2r16'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SPR_F10R10',
        ),
        migrations.DeleteModel(
            name='SPR_F10R10_1',
        ),
        migrations.DeleteModel(
            name='SPR_F10R10_2',
        ),
        migrations.DeleteModel(
            name='SPR_F10R11',
        ),
        migrations.DeleteModel(
            name='SPR_F10R13',
        ),
        migrations.DeleteModel(
            name='SPR_F10R15',
        ),
        migrations.DeleteModel(
            name='SPR_F10R16',
        ),
        migrations.DeleteModel(
            name='SPR_F10R17',
        ),
        migrations.DeleteModel(
            name='SPR_F10R18',
        ),
        migrations.DeleteModel(
            name='SPR_F10R19_1',
        ),
        migrations.DeleteModel(
            name='SPR_F10R19_2',
        ),
        migrations.DeleteModel(
            name='SPR_F10R19_3',
        ),
        migrations.DeleteModel(
            name='SPR_F10R20',
        ),
        migrations.DeleteModel(
            name='SPR_F10R21',
        ),
        migrations.DeleteModel(
            name='SPR_F10R21_1',
        ),
        migrations.DeleteModel(
            name='SPR_F10R22',
        ),
        migrations.DeleteModel(
            name='SPR_F10R23',
        ),
        migrations.DeleteModel(
            name='SPR_F10R24',
        ),
        migrations.DeleteModel(
            name='SPR_F10R25',
        ),
        migrations.DeleteModel(
            name='SPR_F10R25_1',
        ),
        migrations.DeleteModel(
            name='SPR_F10R26',
        ),
        migrations.DeleteModel(
            name='SPR_F10R27',
        ),
        migrations.DeleteModel(
            name='SPR_F10R28',
        ),
        migrations.DeleteModel(
            name='SPR_F10R29',
        ),
        migrations.DeleteModel(
            name='SPR_F10R29_1',
        ),
        migrations.DeleteModel(
            name='SPR_F10R32',
        ),
        migrations.DeleteModel(
            name='SPR_F10R33',
        ),
        migrations.DeleteModel(
            name='SPR_F10R34',
        ),
        migrations.DeleteModel(
            name='SPR_F10R36',
        ),
        migrations.DeleteModel(
            name='SPR_F10R38',
        ),
        migrations.DeleteModel(
            name='SPR_F10R40',
        ),
        migrations.DeleteModel(
            name='SPR_F10R7_1',
        ),
        migrations.DeleteModel(
            name='SPR_F10R8',
        ),
        migrations.DeleteModel(
            name='SPR_F10R9',
        ),
        migrations.DeleteModel(
            name='SPR_F10R9_1',
        ),
        migrations.DeleteModel(
            name='SPR_F11R10',
        ),
        migrations.DeleteModel(
            name='SPR_F11R11',
        ),
        migrations.DeleteModel(
            name='SPR_F11R12',
        ),
        migrations.DeleteModel(
            name='SPR_F11R13',
        ),
        migrations.DeleteModel(
            name='SPR_F11R14',
        ),
        migrations.DeleteModel(
            name='SPR_F11R15',
        ),
        migrations.DeleteModel(
            name='SPR_F11R16',
        ),
        migrations.DeleteModel(
            name='SPR_F11R17',
        ),
        migrations.DeleteModel(
            name='SPR_F11R20',
        ),
        migrations.DeleteModel(
            name='SPR_F11R21',
        ),
        migrations.DeleteModel(
            name='SPR_F11R22',
        ),
        migrations.DeleteModel(
            name='SPR_F11R25',
        ),
        migrations.DeleteModel(
            name='SPR_F11R26',
        ),
        migrations.DeleteModel(
            name='SPR_F11R27',
        ),
        migrations.DeleteModel(
            name='SPR_F11R28',
        ),
        migrations.DeleteModel(
            name='SPR_F11R30',
        ),
        migrations.DeleteModel(
            name='SPR_F11R31',
        ),
        migrations.DeleteModel(
            name='SPR_F11R32',
        ),
        migrations.DeleteModel(
            name='SPR_F11R32_1',
        ),
        migrations.DeleteModel(
            name='SPR_F11R33',
        ),
        migrations.DeleteModel(
            name='SPR_F11R35_1',
        ),
        migrations.DeleteModel(
            name='SPR_F11R35_2',
        ),
        migrations.DeleteModel(
            name='SPR_F11R35_3',
        ),
        migrations.DeleteModel(
            name='SPR_F11R36',
        ),
        migrations.DeleteModel(
            name='SPR_F11R9',
        ),
        migrations.DeleteModel(
            name='SPR_F12R10',
        ),
        migrations.DeleteModel(
            name='SPR_F12R11',
        ),
        migrations.DeleteModel(
            name='SPR_F12R13',
        ),
        migrations.DeleteModel(
            name='SPR_F12R14_1',
        ),
        migrations.DeleteModel(
            name='SPR_F12R9',
        ),
        migrations.DeleteModel(
            name='SPR_F2R10',
        ),
        migrations.DeleteModel(
            name='SPR_F2R12',
        ),
        migrations.DeleteModel(
            name='SPR_F2R15',
        ),
        migrations.DeleteModel(
            name='SPR_F2R16',
        ),
        migrations.AlterField(
            model_name='form1',
            name='r01',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.spr_f10r1', verbose_name='Орган'),
        ),
        migrations.AlterField(
            model_name='form1',
            name='r01_organ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.spr_f10r1_organ', verbose_name='Код органа'),
        ),
        migrations.AlterField(
            model_name='form1',
            name='r02',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.spr_f10r2', verbose_name='Учесть'),
        ),
        migrations.AlterField(
            model_name='form1',
            name='r03',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.spr_f10r3', verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='form1',
            name='r03_gasorg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.spr_f10r3_gasorg', verbose_name='Код терроргана ГАС'),
        ),
        migrations.AlterField(
            model_name='form1',
            name='r51',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guide.spr_f10r51', verbose_name='Административный участок'),
        ),
        migrations.DeleteModel(
            name='SPR_F10R1',
        ),
        migrations.DeleteModel(
            name='SPR_F10R1_ORGAN',
        ),
        migrations.DeleteModel(
            name='SPR_F10R2',
        ),
        migrations.DeleteModel(
            name='SPR_F10R3',
        ),
        migrations.DeleteModel(
            name='SPR_F10R3_GASORG',
        ),
        migrations.DeleteModel(
            name='SPR_F10R51',
        ),
    ]
