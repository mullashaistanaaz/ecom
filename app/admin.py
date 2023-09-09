from django.contrib import admin
from .models import User,UserProfile,Product,Category,Catelog,Order,Shipping,Content,AdminProfile
from .models import Cart,CartItem,Review,Rating,SearchQuery,UserPurchaseHistory,CustomerSupport,SalesData

# Register your models here.

admin.site.register(SalesData)
admin.site.register(AdminProfile)
admin.site.register(Content)
admin.site.register(CustomerSupport)
admin.site.register(Shipping)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Catelog)
admin.site.register(CartItem)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(SearchQuery)
admin.site.register(UserPurchaseHistory)