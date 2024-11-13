# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path("Home",Base.as_view(),name="base"),
    path("",login,name="logn"),
    path('logout/',user_logout, name='logout'),
    
    #  Order
    path('order/', OrderListView.as_view(), name='o_list'),
    path('order/add/', OrderCreateView.as_view(), name='o_cr'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='o_detail'),
    path('order/<int:pk>/edit/', OrderUpdateView.as_view(), name='o_up'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='o_delete'),
    
    # Product
    path('products/', ProductListView.as_view(), name='p_list'),
    path('product/add/', ProductCreateView.as_view(), name='p_cr'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='p_detail'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='p_up'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='p_delete')
    
]