from django.urls import path, re_path

from django.urls import path

from .views import CustomLoginView
from . import views
from django.conf.urls.static import static


urlpatterns = [
    
    path('category_pro/<int:category_id>/', views.category_view_pro, name='category_view_pro'),
    path('category/<int:category_id>/', views.category_view, name='category_view'),

    path('checkout/', views.chechout_detail,name='checkout'),
    path('cart/', views.view_cart,name='cart'),
    path('', views.products_list,name='master'),
    path('update_item/', views.updateitem,name='update_item'),
    
    path('processorder/', views.processorder,name='processorder'),
    path('product/', views.products_list,name='product'),
    path('details/<int:id>', views.products_detail,name='detail'),
    path('signup/', views.signup, name='signup'),
    
    path('login/', CustomLoginView.as_view(), name='login'),

    path('create_customer/', views.create_customer, name='create_customer'),

    path('login_comp/', views.login_view, name='login_comp'),
    
    path('accounts/profile/', views.profile_view, name='profile'),
    


    


#     # path('',views.book_detail),
    
#     # path('',),
    # path('',views.main,name='main'),
#     path('books/',views.books,name='books'),
    
]