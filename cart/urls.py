from django.urls import path

from . import views

urlpatterns = [

    path('', views.cart_summory, name='cart-summory'),

    path('add/', views.cart_add, name='cart-add'), #use in ajax - cart-summary.html

    path('delete/', views.cart_delete, name='cart-delete'),

    path('update/', views.cart_update, name='cart-update'),


]










