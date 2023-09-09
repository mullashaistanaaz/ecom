from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.template import loader



def base(request):
    return render(request,'base.html')


def products_list(request):
    mymembers=Product.objects.all()
    template=loader.get_template('base.html')
    context={ 'mymembers':mymembers,
             }
    return HttpResponse(template.render(context,request))
