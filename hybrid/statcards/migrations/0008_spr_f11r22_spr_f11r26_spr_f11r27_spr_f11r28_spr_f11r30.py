# Generated by Django 3.1.5 on 2021-02-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statcards', '0007_spr_f10r27_spr_f10r28_spr_f10r29_spr_f10r29_1_spr_f10r32_spr_f10r33_spr_f10r34_spr_f10r36_spr_f10r38'),
    ]

    operations = [
        migrations.CreateModel(
            name='SPR_F11R22',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R22 Национальность',
                'verbose_name_plural': 'F1.1 R22 Национальности',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R26',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R26 Мотив',
                'verbose_name_plural': 'F1.1 R26 Мотивы',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R27',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=1, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R27 Преступление выявлено',
                'verbose_name_plural': 'F1.1 R27 Преступление выявлено',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R28',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R28 Код ущерба',
                'verbose_name_plural': 'F1.1 R28 Код ущерба',
            },
        ),
        migrations.CreateModel(
            name='SPR_F11R30',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.1 R30 Технические средства снятия информации',
                'verbose_name_plural': 'F1.1 R30 Технические средства снятия информации',
            },
        ),
    ]
