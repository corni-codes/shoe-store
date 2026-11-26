from django.urls import path
from . import views
from .views import signup_view
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('custom/', views.custom, name='custom'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('products/<str:category_name>/', views.product_by_category, name='product_by_cat'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/direct/', views.direct_checkout, name='direct_checkout'),
    path('orders/', views.order_history, name='order_history'),
    path('orders/<str:order_number>/',views.order_detail, name='order_detail'),
]

