# Generated by Django 3.2.9 on 2021-12-19 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0008_auto_20211219_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobile',
            name='drive_unit',
            field=models.CharField(choices=[('AWD', 'автоматически подключаемый полный'), ('RWD', 'задний'), ('FWD', 'передний'), ('4WD', 'полный (постоянный и подключаемый)')], default='RWD', max_length=45, verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='gearbox',
            field=models.CharField(choices=[('manual', 'механика'), ('automatic', 'автомат')], default='automatic', max_length=45, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='image1',
            field=models.FileField(blank=True, upload_to='myhome', verbose_name='Ссылка картинки'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='image2',
            field=models.FileField(blank=True, upload_to='myhome', verbose_name='Ссылка картинки'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='image3',
            field=models.FileField(blank=True, upload_to='myhome', verbose_name='Ссылка картинки'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='image4',
            field=models.FileField(blank=True, upload_to='myhome', verbose_name='Ссылка картинки'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='image5',
            field=models.FileField(blank=True, upload_to='myhome', verbose_name='Ссылка картинки'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='insurance',
            field=models.ForeignKey(default='1', max_length=90, on_delete=django.db.models.deletion.PROTECT, to='myhome.insurance', verbose_name='Страхование'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='interior_color',
            field=models.CharField(choices=[('light', 'светлый'), ('dark', 'темный')], default='dark', max_length=45, verbose_name='Цвет салона'),
        ),
        migrations.AlterField(
            model_name='automobile',
            name='type_of_fuel',
            field=models.CharField(choices=[('benzine', 'бензин'), ('electro', 'электро'), ('diesel', 'дизель')], default='benzine', max_length=45, verbose_name='Вид топлива'),
        ),
    ]