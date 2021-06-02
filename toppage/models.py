from django.db import models

# Create your models here.
class Top(models.Model):
    sample_name=models.CharField('サンプル名', max_length=30)
    rock_type=models.CharField('岩石名', max_length=20)
    weight=models.IntegerField('重さ[グラム]')
    sampling_date=models.DateField('採集年月日')


