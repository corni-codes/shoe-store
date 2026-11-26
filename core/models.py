from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=100)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description= models.TextField(blank=True)
    image= models.ImageField(upload_to='products/')
    category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    is_featured= models.BooleanField(default=False)

    def __str__(self):
        return f" {self.name} -{self.price}"
  
class ProductVariant(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    size= models.CharField(max_length=10)
    color=models.CharField(max_length=30)
    stock=models.PositiveIntegerField(default=0)
    available_date= models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.size} - {self.color} - {self.stock}"
    
class CartItem(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    variant= models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user} - {self.variant} - {self.quantity}"
    @property
    def line_total(self):
        return self.variant.product.price * self.quantity

class CustomUser(AbstractUser):
    phone_number= models.CharField(max_length=15,unique=True)
    email= models.EmailField(unique=True)
    first_name= models.CharField(max_length= 150)
    last_name= models.CharField(max_length= 150)
   

    def __str__(self):
        return self.username

class Order(models.Model):

    ORDER_STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    PAYMENT_METHODS = [
        ('pay_on_delivery', 'Pay on Delivery'),
    ]

    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    order_number = models.CharField(max_length=30, unique=True)

    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS,
        default='pending'
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number
    
class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True
    )

    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.SET_NULL,
        null=True
    )

    product_name = models.CharField(max_length=150)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=30)

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField()

    @property
    def line_total(self):
        return self.unit_price * self.quantity

    def __str__(self):
        return f"{self.product_name} - {self.order.order_number}"




    

    