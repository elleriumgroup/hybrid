# Generated by Django 3.1.5 on 2021-02-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statcards', '0008_spr_f11r22_spr_f11r26_spr_f11r27_spr_f11r28_spr_f11r30'),
    ]

    operations = [
        migrations.CreateModel(
            name='SPR_F10R51',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.0 R51 Административный участок',
                'verbose_name_plural': 'F1.0 R51 Административные участки',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R31',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R31 Примененние криминалистических средств и методов',
                'verbose_name_plural': 'F1.1 R31 Примененние криминалистических средств и методов',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R32',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R32 Использование АБД, ИПС',
                'verbose_name_plural': 'F1.1 R32 Использование АБД, ИПС',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R32_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R32.1 Использование аппаратно-программных средств',
                'verbose_name_plural': 'F1.1 R32.1 Использование аппаратно-программных средств',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R33',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R33 Уголовное дело расследовано',
                'verbose_name_plural': 'F1.1 R33 Уголовное дело расследовано',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R35_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R35_1 Сообщение',
                'verbose_name_plural': 'F1.1 R35_1 Сообщение',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R35_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R35_2 Сообщение',
                'verbose_name_plural': 'F1.1 R35_2 Сообщение',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R35_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R35_3 Сообщение',
                'verbose_name_plural': 'F1.1 R35_3 Сообщение',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R36',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R36 Применялся',
                'verbose_name_plural': 'F1.1 R36 Применялся',
            },
        ),
        migrations.CreateModel(
            name='SPR_F12R10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.2 R10 Лицу, совершившему преступление предъявлено обвинение',
                'verbose_name_plural': 'F1.2 R10 Лицу, совершившему преступление предъявлено обвинение',
            },
        ),
        migrations.CreateModel(
            name='SPR_F12R11',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.2 R11 В отношении обвиняемого избраны меры пресечения',
                'verbose_name_plural': 'F1.2 R11 В отношении обвиняемого избраны меры пресечения',
            },
        ),
        migrations.CreateModel(
            name='SPR_F12R13',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.2 R13 УД находится в производстве',
                'verbose_name_plural': 'F1.2 R13 УД находится в производстве',
            },
        ),
        migrations.CreateModel(
            name='SPR_F12R14_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.2 R14.1 Установлено отедалми УУР УМВД',
                'verbose_name_plural': 'F1.2 R14.1 Установлено отедалми УУР УМВД',
            },
        ),
        migrations.CreateModel(
            name='SPR_F12R9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.2 R9 Лицо задержано в порядке',
                'verbose_name_plural': 'F1.2 R9 Лицо задержано в порядке',
            },
        ),
    ]
