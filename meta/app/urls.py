
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    
    path('checkout/', views.chechout_detail,name='checkout'),
    path('cart/', views.view_cart,name='cart'),
    path('', views.base,name='base'),
    
    path('product/', views.products_list,name='product'),
    path('details/<int:id>', views.products_detail,name='detail'),
#     # path('',views.book_detail),
    
#     # path('',),
    # path('',views.main,name='main'),
#     path('books/',views.books,name='books'),
    
]