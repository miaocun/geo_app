from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Locality
from django.http import Http404
from django.shortcuts import redirect   
from .forms import LocalityForm
from .forms import LocalityFindForm
from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.
def locality(request):
    positions=Locality.objects.all()
    paginator=Paginator(positions,9)

    page=request.GET.get('page',1)
    positions=paginator.page(page)

    return TemplateResponse(request, 'locality/locality.html', {'positions':positions})

def locality_detail(request, locality_id):
    try: 
        position = Locality.objects.get(id=locality_id)
    except Locality.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'locality/locality_detail.html', {'position': position})


def locality_create(request):
    if (request.method=='POST'):
        obj=Locality()
        locality=LocalityForm(request.POST, instance=obj)
        locality.save()
        return redirect(to='locality')
    params={'form':LocalityForm(),
    }

    return render(request, 'locality/locality_create.html', params)

def locality_edit(request, num):
        obj=Locality.objects.get(id=num)
        if(request.method=='POST'):
            locality=LocalityForm(request.POST, request.FILES, instance=obj)
            locality.save()
            return redirect(to='locality')
        params={
            'id':num,
            'form':LocalityForm(instance=obj),
        }
        return render(request, 'locality/locality_edit.html', params)


def locality_delete(request, num):
        locality=Locality.objects.get(id=num)
        if(request.method=='POST'):
            locality.delete()
            return redirect(to='locality')
        params={
            'id':num,
            'obj':locality,
        }
        return render(request, 'locality/locality_delete.html', params)

def locality_find(request):
    if (request.method == 'POST'):
        form=LocalityFindForm(request.POST)
        str=request.POST['locality_find']
        data=Locality.objects.filter(Q(country__contains=str)|Q(terrane__contains=str)|Q(locality__contains=str)|Q(E__contains=str)|Q(lon__contains=str)|Q(N__contains=str)|Q(lat__contains=str))
    else:
        form=LocalityFindForm()
        data=Locality.objects.all()

    params={'form':form,
            'data':data,
    }
    return render(request, 'locality/locality_find.html', params)

def photoupload(req):
    if req.method == 'GET':
        return redirect('/locality')
        
    locality = Locality.objects.get(id=req.POST['id'])
    locality.photo = req.FILES['upfile']
    locality.save()
    return redirect('/locality')


"""
#アップロード関数を以下のように定義した
def photoupload(req):
    if req.method == 'GET':
        return render(req, 'locality/')

    #locality = Locality()
    locality = Locality.objects.get(id=req.POST['id'])
    locality.photo=req.FILES['upfile']
    locality.save()

    def photoupload(req):
        if req.method == 'GET':
            return redirect('locality') """