from django.db import models

# Create your models here.
class Owner(models.Model):   
   class Meta:
      #テーブル名の指定
      db_table ="Owner"
      verbose_name ="所有者"
      verbose_name_plural ="所有者"
   
   #カラム名の定義
   owner_name = models.CharField(max_length=10,unique=True)
   def __str__(self):
       return self.owner_name