# Generated by Django 3.2.9 on 2021-12-22 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myhome', '0010_auto_20211219_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='nazvanie',
            field=models.CharField(default='Audi RS6 2019', max_length=65, verbose_name='Данные автомобиля'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='drive_unit',
            field=models.CharField(choices=[('FWD', 'передний'), ('AWD', 'автоматически подключаемый полный'), ('RWD', 'задний'), ('4WD', 'полный (постоянный и подключаемый)')], default='RWD', max_length=45, verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='interior_color',
            field=models.CharField(choices=[('dark', 'темный'), ('light', 'светлый')], default='dark', max_length=45, verbose_name='Цвет салона'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='modell',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='myhome.modell', verbose_name='Модель автомобиля'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='type_of_fuel',
            field=models.CharField(choices=[('benzine', 'бензин'), ('electro', 'электро'), ('diesel', 'дизель'), ('hybrid', 'гибрид')], default='benzine', max_length=45, verbose_name='Вид топлива'),
        ),
        migrations.AlterField(
            model_name='service',
            name='type_of_service',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='myhome.type_of_service', verbose_name='Вид услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
