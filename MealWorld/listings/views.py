
from django.shortcuts import render
from .models import Category, Meal

# Create your views here.
def meal_list(request):
    categories = Category.objects.all()
    meals = Meal.objects.all()
    return render(
        request,
        'meal/list.html',
        {
            'categories': categories,
            'meals': meals
        }
    )
