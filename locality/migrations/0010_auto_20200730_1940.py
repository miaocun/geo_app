# Generated by Django 2.2.13 on 2020-07-30 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locality', '0009_auto_20200730_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='画像'),
        ),
    ]
