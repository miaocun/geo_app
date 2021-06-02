# Generated by Django 2.2.13 on 2020-07-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locality', '0005_auto_20200719_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='lat',
            field=models.DecimalField(decimal_places=5, help_text='単位はディグリー', max_digits=8, verbose_name='緯度[°]'),
        ),
        migrations.AlterField(
            model_name='locality',
            name='lon',
            field=models.DecimalField(decimal_places=5, help_text='単位はディグリー', max_digits=8, verbose_name='経度[°]'),
        ),
    ]
