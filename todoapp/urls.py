from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<str:pk>', views.delete,name='delete'),
    path('edit/<int:pk>', views.edit,name='edit'),
    path('login/', views.loginPage , name='login'),
    path('register/', views.registerPage , name='register'),
]