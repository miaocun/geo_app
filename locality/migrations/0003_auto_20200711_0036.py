# Generated by Django 2.2.14 on 2020-07-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locality', '0002_auto_20200710_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locality',
            name='EandW',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='NandS',
        ),
        migrations.AddField(
            model_name='locality',
            name='E',
            field=models.BooleanField(blank=True, null=True, verbose_name='東'),
        ),
        migrations.AddField(
            model_name='locality',
            name='N',
            field=models.BooleanField(blank=True, null=True, verbose_name='北'),
        ),
    ]
