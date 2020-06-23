from django.contrib import admin

# Register your models here.
from .models import Category, Sample

class SampleAdmin(admin.ModelAdmin):
    list_display=('date','category','rocktype','memo')

admin.site.register(Category)
admin.site.register(Sample,SampleAdmin)

