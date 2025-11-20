from django.shortcuts import render, get_object_or_404
from .models import Category, Meal


# List all meals or meals within a category
def meal_list(request, category_slug=None):
    categories = Category.objects.all()
    requested_category = None
    meals = Meal.objects.all()

    if category_slug:
        requested_category = get_object_or_404(Category, slug=category_slug)
        meals = Meal.objects.filter(category=requested_category)

    return render(
        request,
        'meal/list.html',
        {
            'categories': categories,
            'requested_category': requested_category,
            'meals': meals
        }
    )


# Meal detail view (your provided function, inserted without duplication)
def meal_detail(request, category_slug, meal_slug):
    category = get_object_or_404(Category, slug=category_slug)
    meal = get_object_or_404(
        Meal,
        category_id=category.id,
        slug=meal_slug
    )
    return render(
        request,
        'meal/detail.html',
        {
            'meal': meal
        }
    )
