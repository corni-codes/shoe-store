from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Product,
    CustomUser,
    ProductVariant,
    CartItem,
    Category,
    Order,
    OrderItem,
)


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = [
        'username', 'email', 'phone_number',
        'first_name', 'last_name', 'is_staff', 'is_active'
    ]

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    list_filter = ['category']
    search_fields = ['name']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = [
        'product_name', 'size', 'color',
        'unit_price', 'quantity'
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number',
        'full_name',
        'created_at',
        'total_amount',
        'payment_method',
        'payment_status',
        'status',
    ]

    list_filter = [
        'status',
        'payment_status',
        'payment_method',
        'created_at',
    ]

    search_fields = [
        'order_number',
        'full_name',
        'email',
        'phone_number',
    ]

    list_editable = ['status', 'payment_status']

    readonly_fields = [
        'order_number',
        'created_at',
        'updated_at',
    ]

    inlines = [OrderItemInline]

    ordering = ['-created_at']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
