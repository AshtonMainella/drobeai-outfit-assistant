# urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView  # Import LogoutView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Use LogoutView for logout
    path('wardrobe/', views.wardrobe, name='wardrobe'),
    path('add/', views.add_clothing, name='add_clothing'),
    path('edit/<int:item_id>/', views.edit_clothing, name='edit_clothing'),
    path('delete/<int:item_id>/', views.delete_clothing, name='delete_clothing'),
    path('generate-outfit/', views.generate_outfit, name='generate_outfit'),
    path('settings/', views.settings, name='settings'),
]
