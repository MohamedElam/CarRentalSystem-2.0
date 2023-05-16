
from django.urls import path
from accounts.views import *
from django.contrib import admin
from system.views import *


urlpatterns = [
    path('', home, name="home"),

    path('carlist/', car_list, name="car_list"),
    path('createOrder/', order_created, name="order_create"),

    path('<int:id>/edit/', car_update, name="car_edit"),


    path('<int:id>/', car_detail, name="car_detail"),
    path('detail/<int:id>/', order_detail, name="order_detail"),

    path('<int:id>/delete/', car_delete, name="car_delete"),
    path('<int:id>/deleteOrder/', order_delete, name="order_delete"),

    path('contact/', contact, name="contact"),

    path('newcar/', newcar, name="newcar"),
    path('<int:id>/like/', like_update, name="like"),
    path('popularcar/', popular_car, name="popularcar"),
]
