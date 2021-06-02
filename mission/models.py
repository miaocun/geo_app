from django.db import models

# Create your models here.
from toppage.models import Top

class Mission(models.Model):
    type=models.BooleanField('研究')
    project=models.CharField('プロジェクト名', max_length=30)
    funding=models.CharField('研究費', max_length=20)
    publication=models.CharField('関連論文', max_length=50)
    sample=models.ForeignKey(Top, on_delete = models.CASCADE, verbose_name="サンプルID")
