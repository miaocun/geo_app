from django import forms
from .models import Locality

# Create your models here.

class LocalityForm(forms.ModelForm):
    class Meta:
        model=Locality
        fields=['country','terrane','locality','E','lon','N','lat','photo','sample',]

class LocalityFindForm(forms.Form):
    locality_find=forms.CharField(label='地理情報検索ワード',required=False)


