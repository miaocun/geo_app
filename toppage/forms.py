from django import forms
from .models import Top

class TopForm(forms.ModelForm):
    class Meta:
        model=Top
        fields=['sample_name','rock_type','weight','sampling_date']

class TopFindForm(forms.Form):
    find=forms.CharField(label='岩石試料検索ワード', required=False)