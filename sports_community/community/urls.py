from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),      
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
]