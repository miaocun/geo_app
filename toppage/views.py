from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Top
from .forms import TopForm
from django.shortcuts import redirect
from locality.models import Locality
from .forms import TopFindForm
from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.

def topcreate(request):

    if (request.method == 'POST'):
        obj=Top()
        top=TopForm(request.POST, instance=obj)
        top.save()
        return redirect(to='top')
    
    params={'form':TopForm(),
    }

    return render(request, 'toppage/top_create.html', params)


def topedit(request,num):
    obj=Top.objects.get(id=num)
    if (request.method == 'POST'):

        top=TopForm(request.POST, instance=obj)
        top.save()
        return redirect(to='top')
    
    params={'id':num,
            'form':TopForm(instance=obj),
    }

    return render(request, 'toppage/top_edit.html', params)

def topdelete(request,num):
    top=Top.objects.get(id=num)
    if (request.method == 'POST'):
        top.delete()
        return redirect(to='top')
    
    params={'id':num,
            'obj':top,
    }

    return render(request, 'toppage/top_delete.html', params)

def topfind(request):
    if (request.method == 'POST'):
        form=TopFindForm(request.POST)
        str=request.POST['find']
        data=Top.objects.filter(Q(id__contains=str)|Q(sample_name__contains=str)|Q(rock_type__contains=str)|Q(weight__contains=str)|Q(sampling_date__contains=str))
    else:
        form=TopFindForm()
        data=Top.objects.all()

    params={'form':form,
            'data':data,
    }

    return render(request, 'toppage/top_find.html', params)

def top(request):
    samples=Top.objects.all()
    paginator=Paginator(samples,10)

    page=request.GET.get('page',1)
    samples=paginator.page(page)


    return TemplateResponse(request, 'toppage/top.html',{'samples':samples})


