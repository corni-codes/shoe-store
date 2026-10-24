from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, ProductVariant, CartItem
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST


# Create your views here.
@login_required
def home(request):
    featured_product= Product.objects.filter(is_featured= True)
    return render (request, 'home.html', {'featured_product': featured_product})

@login_required
def shop(request):
    products= Product.objects.all()
    categories= Category.objects.all()
    return render(request, 'shop.html', {'products': products, 'categories': categories})

@login_required
def product_by_category(request, category_name):
    products= Product.objects.filter(category__name= category_name)
    categories= Category.objects.all()
    return render(request, 'shop.html', {'products': products, 'categories': categories})

@login_required
def product_detail(request, pk):
    product= get_object_or_404(Product, pk=pk)
    variants= ProductVariant.objects.filter(product=product)
    in_stock=variants.filter(stock__gt=0).exists()
    return render(request, 'product_detail.html', {'product': product, 'variants': variants, 'in_stock': in_stock})

@login_required
@require_POST
def add_to_cart(request):
    variant_id = request.POST.get('variant')
    variant = get_object_or_404(ProductVariant, pk=variant_id)

    if variant.stock <= 0:
        return JsonResponse({
            'success': False,
            'message': 'This variant is out of stock.'
        }, status=400)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        variant=variant
    )

    if not created:
        if cart_item.quantity < variant.stock:
            cart_item.quantity += 1
            cart_item.save()
        else:
            return JsonResponse({
                'success': False,
                'message': 'You have reached the available stock limit.'
            }, status=400)

    return JsonResponse({
        'success': True,
        'message': 'Added to cart!',
        'cart_quantity': cart_item.quantity
    })



@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.line_total for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})


@login_required
def custom(request):
    return render(request, 'custom.html')


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def contact(request):
    return render(request, 'contact.html')

def signup_view(request):
    if request.method == 'POST':
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form= CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})




