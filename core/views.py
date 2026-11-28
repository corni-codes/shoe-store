from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, ProductVariant, CartItem, Order, OrderItem
from .forms import CustomUserCreationForm, CheckoutForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db import transaction
from django.utils.crypto import get_random_string


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
@require_POST
def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, user=request.user)
    action = request.POST.get('action')

    if action == 'increase':
        if item.quantity < item.variant.stock:
            item.quantity += 1
            item.save()
        else:
            messages.error(request, 'You have reached the available stock limit.')
    elif action == 'decrease':
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()

    return redirect('cart')


@login_required
@require_POST
def remove_cart_item(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, user=request.user)
    item.delete()
    return redirect('cart')

@login_required
def cart(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.line_total for item in items)
    return render(request, 'cart.html', {'items': items, 'total': total})

@login_required
def checkout(request):
    direct_variant_id = request.session.get('direct_checkout_variant_id')

    if direct_variant_id:
        variant = get_object_or_404(
            ProductVariant.objects.select_related('product'),
            pk=direct_variant_id
        )

        checkout_items = [{
            'variant': variant,
            'quantity': 1,
            'line_total': variant.product.price,
            'cart_item_id': None,
        }]
    else:
        cart_items = CartItem.objects.filter(
            user=request.user
        ).select_related('variant__product')

        checkout_items = [{
            'variant': item.variant,
            'quantity': item.quantity,
            'line_total': item.line_total,
            'cart_item_id': item.pk,
        } for item in cart_items]

    if not checkout_items:
        messages.error(request, 'Your cart is empty.')
        return redirect('cart')

    total = sum(item['line_total'] for item in checkout_items)

    initial_data = {
        'full_name': request.user.get_full_name(),
        'phone_number': request.user.phone_number,
        'email': request.user.email,
    }

    form = CheckoutForm(request.POST or None, initial=initial_data)

    if request.method == 'POST' and form.is_valid():

        with transaction.atomic():
            locked_items = []

            for item in checkout_items:
                variant = ProductVariant.objects.select_for_update().select_related(
                    'product'
                ).get(pk=item['variant'].pk)

                if item['quantity'] > variant.stock:
                    form.add_error(
                        None,
                        f'Insufficient stock for {variant.product.name}.'
                    )
                    break

                locked_items.append((item, variant))

            if not form.errors:
                order = Order.objects.create(
                    user=request.user,
                    order_number=f"ORD-{get_random_string(10).upper()}",
                    full_name=form.cleaned_data['full_name'],
                    phone_number=form.cleaned_data['phone_number'],
                    email=form.cleaned_data['email'],
                    address=form.cleaned_data['address'],
                    city=form.cleaned_data['city'],
                    state=form.cleaned_data['state'],
                    total_amount=total,
                    payment_method= 'pay_on_delivery'
                )

                for item, variant in locked_items:
                    OrderItem.objects.create(
                        order=order,
                        product=variant.product,
                        variant=variant,
                        product_name=variant.product.name,
                        size=variant.size,
                        color=variant.color,
                        unit_price=variant.product.price,
                        quantity=item['quantity'],
                    )

                    variant.stock -= item['quantity']
                    variant.save(update_fields=['stock'])

                if direct_variant_id:
                    request.session.pop('direct_checkout_variant_id', None)
                else:
                    CartItem.objects.filter(
                        user=request.user,
                        pk__in=[
                            item['cart_item_id']
                            for item in checkout_items
                        ]
                    ).delete()

                return render(
                    request,
                    'checkout_success.html',
                    {'order': order}
                )

    return render(request, 'checkout.html', {
        'form': form,
        'cart_items': checkout_items,
        'total': total,
    })

@login_required
@require_POST
def direct_checkout(request):
    variant_id = request.POST.get('variant')

    variant = get_object_or_404(ProductVariant, pk=variant_id)

    if variant.stock <= 0:
        messages.error(request, 'This product variant is out of stock.')
        return redirect('product_detail', pk=variant.product.pk)

    request.session['direct_checkout_variant_id'] = variant.id

    return redirect('checkout')

@login_required
def order_history(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'order_history.html', {
        'orders': orders
    })

@login_required
def order_detail(request, order_number):
    order = get_object_or_404(
        Order.objects.prefetch_related('items'),
        order_number=order_number,
        user=request.user
    )

    return render(request, 'order_detail.html', {
        'order': order
    })

@login_required
def custom(request):
    return render(request, 'custom.html')


@login_required
def about(request):
    return render(request, 'about.html')


@login_required
def contact(request):
    return render(request, 'contact.html')

def health_check(request):
    return HttpResponse("OK")

def signup_view(request):
    if request.method == 'POST':
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form= CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})




