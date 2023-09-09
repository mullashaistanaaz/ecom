
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.base,name='base'),
    
    path('product/', views.products_list,name='base'),
#     # path('',views.book_detail),
    
#     # path('',),
    # path('',views.main,name='main'),
#     path('books/',views.books,name='books'),
    
]