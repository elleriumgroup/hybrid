# Generated by Django 3.1.5 on 2021-02-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SPR_F10R7o',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'F1.0 R7o Отдел, выявивший преступление',
                'verbose_name_plural': 'F1.0 R7o Отделы, выявившие преступления',
            },
        ),
    ]