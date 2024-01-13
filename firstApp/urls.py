from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.display),
    path('datetime/', views.displaydatetime),
]