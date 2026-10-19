from django.contrib import admin
from .models import Product
from .models import CustomUser
from .models import ProductVariant
from .models import CartItem
from django.contrib.auth.admin import UserAdmin
from .models import Category


# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number','first_name', 'last_name',  'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )

class ProductAdmin(admin.ModelAdmin):
    list_display= ['name', 'price', 'category']
    list_filter= ['category']
    search_fields= ['name']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant)
admin.site.register(CartItem)


   



