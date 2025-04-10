from django.urls import path, include
from .views import *

app_name = 'app'
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('detail/<int:id>', detail, name='detail'),
    path('coms/<int:id>', comments, name='coms'),
    path('savat_u/', savat_u, name='savat_u'),
    path('savat_rem/<int:id>', savat_rem, name='savat_rem'),
    path('add_savat/<int:id>/', add_savat, name='add_savat'),
    path('add_product/', add_product, name='add_product'),
    path('product_list/', product_list, name='list'),
    path('delete_product/<int:id>', delete_product, name='product_delete'),
    path('my_products/', my_products, name='my_products'),
    path('xabarlar/', xabarlar, name='xabarlar'),
    path('my_coms/', my_comments, name='my_coms')

]
