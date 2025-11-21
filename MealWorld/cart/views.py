from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from listings.models import Meal
from .forms import CartAddMealForm
from decimal import Decimal

# Create your views here.

def get_cart(request):
    cart = request.session.get(settings.CART_ID)
    if not cart:
        cart = request.session[settings.CART_ID] = {}
    return cart


def cart_add(request, meal_id):
    cart = get_cart(request)
    meal = get_object_or_404(Meal, id=meal_id)
    meal_id = str(meal.id)
    form = CartAddMealForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data

        # Add meal to cart if not already in cart
        if meal_id not in cart:
            cart[meal_id] = {
                'quantity': 0,
                'price': str(meal.price)
            }

        # Overwrite quantity or add to existing
        if request.POST.get('overwrite_qty'):
            cart[meal_id]['quantity'] = cd['quantity']
        else:
            cart[meal_id]['quantity'] += cd['quantity']

        # Mark session as modified so Django saves it
        request.session.modified = True

        return redirect('cart:cart_detail')


def cart_remove(request, meal_id):
    cart = get_cart(request)
    meal_id = str(meal_id)

    if meal_id in cart:
        del cart[meal_id]
        request.session.modified = True

    return redirect('cart:cart_detail')


def cart_clear(request):
    del request.session[settings.CART_ID]
    request.session.modified = True
    return redirect('cart:cart_detail')
