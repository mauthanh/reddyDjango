from django.urls import path
from templates_app import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_template/', views.render_template),
    path('employee/', views.render_employee)
]
