from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user_name=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
    
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='', blank=True, null=True)
    
    def __str__(self):
        return self.user
    

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    catelog=models.ForeignKey('Catelog',on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Catelog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        
        def __str__(self):
            return f"Cart for {self.user.user_name}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user.user_name} for {self.product.name}"
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating by {self.user.user_name} for {self.product.name}"
    
class SearchQuery(models.Model):
    query = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query



class UserPurchaseHistory(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user_name} purchased {self.product.name}"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ])
    shipping_address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.order_number} by {self.user.user_name}"
    

class Shipping(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    carrier = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=50)
    shipping_date = models.DateTimeField()
    estimated_delivery_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('Shipped', 'Shipped'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Delayed', 'Delayed'),
    ])

    def __str__(self):
        return f"Shipping for Order {self.order.id}"


class CustomerSupport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ])

    def __str__(self):
        return f"Support Request #{self.id} by {self.user.user_name}"
    

class Content(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content_type = models.CharField(max_length=20, choices=[
        ('Article', 'Article'),
        ('ProductDescription', 'Product Description'),
        ('BlogPost', 'Blog Post'),
        ('FAQ', 'FAQ'),
        # Add more content types as needed
    ])
    body = models.TextField()
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

from django.utils import timezone

class AdminProfile(models.Model):
  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='admin_profile_pictures/', blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.user_name
    

class SalesData(models.Model):
  
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    date = models.DateField()
    quantity_sold = models.PositiveIntegerField(default=0)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Sales data for {self.product.name} on {self.date}"