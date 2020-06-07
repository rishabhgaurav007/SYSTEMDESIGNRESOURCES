from django.urls import path,include
from main import views

urlpatterns = [
    path('',views.home, name='home'),
    path('<int:pk>/', views.resource_requested, name='resource_requested'),
]