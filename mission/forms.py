from django import forms

# Create your models here.
from .models import Mission
from toppage.models import Top

class MissionForm(forms.ModelForm):
    class Meta:
        model=Mission
        fields=['type','project','funding','publication','sample']

class MissionFindForm(forms.Form):
    mission_find=forms.CharField(label='プロジェクト検索ワード',required=False)