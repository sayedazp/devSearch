from django.urls import path
from . import views
urlpatterns = [
    path('', views.users, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile")
]
