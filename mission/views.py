from django.shortcuts import render
from django.template.response import TemplateResponse
# Create your views here.

from .models import Mission
from django.http import Http404
from django.shortcuts import redirect   

from .forms import MissionFindForm
from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.
def mission(request):
    missions=Mission.objects.all()
    paginator=Paginator(missions,9)

    page=request.GET.get('page',1)
    missions=paginator.page(page)
    return TemplateResponse(request, 'mission/mission.html', {'missions':missions})

def mission_detail(request, mission_id):
    try: 
        mission = Mission.objects.get(id=mission_id)
    except Mission.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'mission/mission_detail.html', {'mission': mission})

from .forms import MissionForm

def mission_create(request):
    if (request.method=='POST'):
        obj=Mission()
        mission=MissionForm(request.POST, instance=obj)
        mission.save()
        return redirect(to='mission')
    params={'form':MissionForm(),
    }
    return render(request, 'mission/mission_create.html', params)

def mission_edit(request,num):
    obj=Mission.objects.get(id=num)
    if (request.method=='POST'):
        mission=MissionForm(request.POST, instance=obj)
        mission.save()
        return redirect(to='mission')
    params={
        'id':num,
        'form':MissionForm(instance=obj),
    }
    return render(request, 'mission/mission_edit.html', params)

def mission_delete(request,num):
    mission=Mission.objects.get(id=num)
    if (request.method=='POST'):
        mission.delete()
        return redirect(to='mission')
    params={
        'id':num,
        'obj':mission,
    }
    return render(request, 'mission/mission_delete.html', params)

def mission_find(request):
    if (request.method == 'POST'):
        form=MissionFindForm(request.POST)
        str=request.POST['mission_find']
        data=Mission.objects.filter(Q(type__contains=str)|Q(project__contains=str)|Q(funding__contains=str)|Q(publication__contains=str))
    else:
        form=MissionFindForm()
        data=Mission.objects.all()

    params={'form':form,
            'data':data,
    }
    return render(request, 'mission/mission_find.html', params)