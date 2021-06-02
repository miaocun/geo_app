from django.db import models

# Create your models here.
from toppage.models import Top

class Locality(models.Model):
    country=models.CharField('産地国', max_length=20)
    terrane=models.CharField('テレーン', max_length=20, null=True, blank=True,)
    locality=models.CharField('産地詳細', max_length=50)
    E=models.BooleanField('東', null=True, blank=True,)
    lon=models.DecimalField('経度[°]', max_digits=8, decimal_places=5, help_text="単位はディグリー")
    N=models.BooleanField('北', null=True, blank=True,)
    lat=models.DecimalField('緯度[°]', max_digits=8, decimal_places=5, help_text="単位はディグリー")
    photo = models.ImageField(upload_to='images', null=True, blank=True,verbose_name="画像",)
    sample=models.ForeignKey(Top, on_delete = models.CASCADE, verbose_name="サンプルID")
