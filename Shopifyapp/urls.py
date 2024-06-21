from django.contrib import admin
from django.urls import path
from Shopifyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('About/', views.about),
    path('Services/', views.services),
]
