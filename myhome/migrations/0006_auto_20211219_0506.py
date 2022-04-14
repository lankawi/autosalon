# Generated by Django 3.2.9 on 2021-12-19 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0005_auto_20211219_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobile',
            name='drive_unit',
            field=models.CharField(choices=[('FWD', 'передний'), ('RWD', 'задний'), ('4WD', 'полный (постоянный и подключаемый)'), ('AWD', 'автоматически подключаемый полный')], default='RWD', max_length=45, verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='interior_color',
            field=models.CharField(choices=[('light', 'светлый'), ('dark', 'темный')], default='dark', max_length=45, verbose_name='Цвет салона'),
        ),
    ]
