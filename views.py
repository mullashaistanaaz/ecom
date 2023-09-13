import datetime
import json
from django.shortcuts import get_object_or_404, redirect, render
from .models import Order, Product,Orderitem
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .models import*
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist

def base(request):
    return render(request,'base.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'  # Change to your login template path
    success_url = reverse_lazy('home')  # Redirect to a success page (change 'home' to your desired URL name)


class SignupForm(UserCreationForm):
    # Add any additional fields you want for user registration here
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('home')  # Redirect to your desired success page (change 'home' to the appropriate URL name)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def products_list(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_item
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_item':0, 'shipping':False}
		cartItems = order.get_cart_item

	mymembers = Product.objects.all()
	context = {'mymembers':mymembers, 'cartItems':cartItems}
	return render(request, 'base.html', context)


def category_view(request, category_id):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_item
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_item':0, 'shipping':False}
		cartItems = order.get_cart_item

	category = Category.objects.get(pk=category_id)
	products = Product.objects.filter(category=category)
	context = {
        'category': category,
        'products': products,
		'cartItems':cartItems
    }
	return render(request, 'category.html', context)


def category_view_pro(request, category_id):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_item
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_item':0, 'shipping':False}
		cartItems = order.get_cart_item

	category = Category.objects.get(pk=category_id)
	products = Product.objects.filter(category=category)
	context = {
        'category': category,
        'products': products,
		'cartItems':cartItems
    }
	return render(request, 'nav.html', context)
    
    
    
    


 # Import your cart logic

def products_detail(request,id):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_item
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_item':0, 'shipping':False}
		cartItems = order['get_cart_item']

	member=Product.objects.get(id=id)
	context = {'member':member, 'cartItems':cartItems}
	return render(request, 'product_detail.html', context)

def view_cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_item
		
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)

def chechout_detail(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_item
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)


def updateitem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = Orderitem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def processorder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id
	else:
		print('User is not logged in')

	return JsonResponse('Payment submitted..', safe=False)


def create_customer(request):
    # Get the current user
    user = request.user

    # Check if the user already has a Customer object
    if not hasattr(user, 'customer'):
        # User does not have a Customer object, create one
        customer = Customer.objects.create(user=user, full_name=user.username)
        # You can add more fields to the Customer object as needed
        # For example: customer.phone_number = '123456789'
        # Make sure to save the customer object

    # Redirect or continue with your view logic
    return redirect('product')  # Replace 'home' with the appropriate URL name

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customer = Customer.objects.get(user__username=username)
        except Customer.DoesNotExist:
            customer = None

        if customer is not None:
            # Authenticate the user using the associated User model and password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Login the user if authentication is successful
                login(request, user)
                return redirect('product')  # Replace 'product' with your desired success URL
            else:
                messages.error(request, "Invalid password. Please try again.")
        else:
            messages.error(request, "User does not exist. Please try again.")

    return render(request, 'login.html')


@login_required
def profile_view(request):
    # Access the Customer instance associated with the logged-in user
    customer = request.user.customer
    
    context = {
        'customer': customer,
    }
    
    return render(request, 'profile.html', context)