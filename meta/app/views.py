from django.shortcuts import render
from .models import Order, Product,Orderitem
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


def products_detail(request,id):
    member=Product.objects.get(id=id)
    template=loader.get_template('product_detail.html')
    context={ 'member':member,
             }
    return HttpResponse(template.render(context,request))
 # Import your cart logic


def view_cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'cart.html', context)

def chechout_detail(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'checkout.html', context)