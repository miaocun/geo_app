from django.db import models

# Create your models here.
from toppage.models import Top

class Collector(models.Model):
    name=models.CharField('採集者', max_length=20)
    storage=models.CharField('保管場所', max_length=20)
    box_number=models.IntegerField('保管箱番号')
    thin_section=models.BooleanField('薄片の有無', null=True, blank=True,)
    thin_section_box=models.CharField('薄片箱名', max_length=30)
    sample=models.ForeignKey(Top, on_delete = models.CASCADE, verbose_name="サンプルID")
