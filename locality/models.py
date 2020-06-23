from django.db import models

# Create your models here.
class Locality(models.Model):   
   class Meta:
      #テーブル名の指定
      db_table ="locality"
      verbose_name ="場所"
      verbose_name_plural ="場所"
   
   #カラム名の定義
   locality_name = models.CharField(max_length=255,unique=True)
   def __str__(self):
       return self.locality_name