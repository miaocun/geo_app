from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):   
   class Meta:
      #テーブル名の指定
      db_table ="category"
      verbose_name ="カテゴリ"
      verbose_name_plural ="カテゴリ"
   
   #カラム名の定義
   category_name = models.CharField(max_length=255,unique=True)
   def __str__(self):
       return self.category_name

   
class Sample(models.Model):
   
   class Meta:
       #テーブル名
       db_table ="Sample"
       verbose_name ="試料"
       verbose_name_plural ="試料"
       
   #カラムの定義
   date = models.DateField(verbose_name="日付",default=datetime.now)
   category = models.ForeignKey(Category, on_delete = models.PROTECT, verbose_name="カテゴリ")
   rocktype = models.CharField(verbose_name="岩石名", max_length=20)
   memo = models.CharField(verbose_name="メモ", max_length=50)
   def __str__(self):
       return self.memo
