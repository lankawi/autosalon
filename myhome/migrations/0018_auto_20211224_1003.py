# Generated by Django 3.2.9 on 2021-12-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0017_auto_20211224_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='nazvanie',
        ),
        migrations.AlterField(
            model_name='automobile',
            name='drive_unit',
            field=models.CharField(choices=[('FWD', 'передний'), ('RWD', 'задний'), ('4WD', 'полный (постоянный и подключаемый)'), ('AWD', 'автоматически подключаемый полный')], default='RWD', max_length=45, verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='gearbox',
            field=models.CharField(choices=[('automatic', 'автомат'), ('manual', 'механика')], default='automatic', max_length=45, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='interior_color',
            field=models.CharField(choices=[('dark', 'темный'), ('light', 'светлый')], default='dark', max_length=45, verbose_name='Цвет салона'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='type_of_fuel',
            field=models.CharField(choices=[('diesel', 'дизель'), ('benzine', 'бензин'), ('electro', 'электро'), ('hybrid', 'гибрид')], default='benzine', max_length=45, verbose_name='Вид топлива'),
        ),
    ]
