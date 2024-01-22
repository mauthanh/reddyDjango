from django.urls import path
from django.contrib import admin
from product_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.products_view),
    path('electronics/', views.electronics_view),
    path('toys/', views.toys_view),
    path('shoes/', views.shoe_view),
]