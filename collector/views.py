from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from .models import Collector
from django.http import Http404
from .forms import CollectorForm
from django.shortcuts import redirect
from .forms import CollectorFindForm
from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.
def collector(request):
    owners=Collector.objects.all()
    paginator=Paginator(owners,9)

    page=request.GET.get('page',1)
    owners=paginator.page(page)

    return TemplateResponse(request, 'collector/collector.html', {'owners':owners})

def collector_detail(request, collector_id):
    try: 
        owner = Collector.objects.get(id=collector_id)
    except Collector.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'collector/collector_detail.html', {'owner': owner})

def collector_create(request):
    if (request.method=='POST'):
        obj=Collector()
        collector=CollectorForm(request.POST, instance=obj)
        collector.save()
        return redirect(to='collector')
    
    params = {'form':CollectorForm(),
    }
    return render(request, 'collector/collector_create.html', params)

def collector_edit(request,num):
    obj=Collector.objects.get(id=num)
    if (request.method=='POST'):
        collector=CollectorForm(request.POST, instance=obj)
        collector.save()
        return redirect(to='collector')
    params = {
        'id':num,
        'form':CollectorForm(instance=obj),
    }
    return render(request, 'collector/collector_edit.html', params)


def collector_delete(request,num):
    collector=Collector.objects.get(id=num)
    if (request.method=='POST'):
        collector.delete()
        return redirect(to='collector')
    params = {
        'id':num,
        'obj':collector,
    }
    return render(request, 'collector/collector_delete.html', params)

def collector_find(request):
    if (request.method == 'POST'):
        form=CollectorFindForm(request.POST)
        str=request.POST['collector_find']
        data=Collector.objects.filter(Q(name__contains=str)|Q(storage__contains=str)|Q(box_number__contains=str)|Q(thin_section__contains=str)|Q(thin_section_box__contains=str))
    else:
        form=CollectorFindForm()
        data=Collector.objects.all()

    params={'form':form,
            'data':data,
    }
    return render(request,'collector/collector_find.html', params)
