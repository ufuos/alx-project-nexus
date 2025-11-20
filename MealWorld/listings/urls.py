# listings/urls.py
from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('<slug:category_slug>',views.meal_list,
    name='meal_list_by_category'),
    path('<slug:category_slug>/<slug:meal_slug>/',views.meal_detail,
    name='meal_detail'),  
]
