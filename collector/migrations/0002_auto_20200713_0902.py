# Generated by Django 2.2.14 on 2020-07-13 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='thin_section_box',
            field=models.CharField(max_length=30, verbose_name='薄片箱名'),
        ),
    ]
