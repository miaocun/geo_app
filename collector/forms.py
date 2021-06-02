from django import forms
from .models import Collector

class CollectorForm(forms.ModelForm):
    class Meta:
        model=Collector
        fields=['name','storage','box_number','thin_section','thin_section_box','sample']

class CollectorFindForm(forms.Form):
    collector_find=forms.CharField(label='管理者検索ワード', required=False)