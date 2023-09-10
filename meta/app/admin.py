from django.contrib import admin
from .models import Customer,Product,Category,Catelog,Order,ShippingAddress,Content,AdminProfile
from .models import Orderitem,Review,Rating,SearchQuery,UserPurchaseHistory,CustomerSupport,SalesData

# Register your models here.

admin.site.register(SalesData)
admin.site.register(AdminProfile)
admin.site.register(Content)
admin.site.register(CustomerSupport)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Catelog)
admin.site.register(Orderitem)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(SearchQuery)
admin.site.register(UserPurchaseHistory)