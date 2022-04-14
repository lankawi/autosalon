# Generated by Django 3.2.9 on 2021-12-19 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myhome', '0002_modell'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(default='черный', max_length=45, verbose_name='Цвет кузова')),
            ],
        ),
        migrations.CreateModel(
            name='Body_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_type', models.CharField(default='универсал', max_length=45, verbose_name='Тип кузова')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='Германия', max_length=45, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance', models.CharField(default='каско', max_length=45, verbose_name='Страхование')),
            ],
        ),
        migrations.CreateModel(
            name='Type_of_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_service', models.CharField(default='бронь', max_length=45, verbose_name='Вид услуги')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_service', models.DateTimeField(verbose_name='Дата услуги')),
                ('type_of_service', models.ForeignKey(default='1', max_length=45, on_delete=django.db.models.deletion.PROTECT, to='myhome.type_of_service', verbose_name='Вид услуги')),
                ('user', models.ForeignKey(default='1', max_length=45, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default='2021', max_length=45, verbose_name='Год')),
                ('type_of_fuel', models.CharField(choices=[('diesel', 'дизель'), ('benzine', 'бензин'), ('electro', 'электро')], default='benzine', max_length=45, verbose_name='Вид топлива')),
                ('engine_volume', models.CharField(default='4.0 л', max_length=6, verbose_name='Объем двигателя')),
                ('power', models.CharField(default='600 л.с.', max_length=10, verbose_name='Мощность')),
                ('gearbox', models.CharField(choices=[('automatic', 'автомат'), ('manual', 'механика')], default='automatic', max_length=45, verbose_name='КПП')),
                ('drive_unit', models.CharField(choices=[('4WD', 'полный (постоянный и подключаемый)'), ('FWD', 'передний'), ('RWD', 'задний'), ('AWD', 'автоматически подключаемый полный')], default='RWD', max_length=45, verbose_name='Привод')),
                ('interior_color', models.CharField(choices=[('light', 'светлый'), ('dark', 'темный')], default='dark', max_length=45, verbose_name='Цвет салона')),
                ('vin', models.CharField(default='1', max_length=16, verbose_name='VIN')),
                ('date', models.DateTimeField(verbose_name='Дата выхода')),
                ('description', models.TextField(default='4-х дверная', max_length=1000, verbose_name='Описание')),
                ('price', models.IntegerField(default='BYN', verbose_name='Цена')),
                ('image1', models.FileField(blank=True, help_text='150x150px', upload_to='static/myhome/image', verbose_name='Ссылка картинки')),
                ('image2', models.FileField(blank=True, help_text='150x150px', upload_to='static/myhome/image', verbose_name='Ссылка картинки')),
                ('image3', models.FileField(blank=True, help_text='150x150px', upload_to='static/myhome/image', verbose_name='Ссылка картинки')),
                ('image4', models.FileField(blank=True, help_text='150x150px', upload_to='static/myhome/image', verbose_name='Ссылка картинки')),
                ('image5', models.FileField(blank=True, help_text='150x150px', upload_to='static/myhome/image', verbose_name='Ссылка картинки')),
                ('body_color', models.ForeignKey(default='1', max_length=45, on_delete=django.db.models.deletion.PROTECT, to='myhome.body_color', verbose_name='Цвет кузова')),
                ('body_type', models.ForeignKey(default='1', max_length=45, on_delete=django.db.models.deletion.PROTECT, to='myhome.body_type', verbose_name='Тип кузова')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhome.brand', verbose_name='Марка автомобиля')),
                ('country', models.ForeignKey(default='1', max_length=45, on_delete=django.db.models.deletion.PROTECT, to='myhome.country', verbose_name='Страна')),
                ('insurance', models.ForeignKey(default='1', max_length=45, on_delete=django.db.models.deletion.PROTECT, to='myhome.insurance', verbose_name='Страхование')),
                ('modell', models.ForeignKey(default='1', max_length=45, on_delete=django.db.models.deletion.PROTECT, to='myhome.modell', verbose_name='Модель автомобиля')),
            ],
        ),
    ]