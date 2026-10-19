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
]

