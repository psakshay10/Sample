from django.contrib import admin
from django.urls import path, include
from home import views
from .views import AddPostView

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('signup/', views.handleSignup, name='handleSignup'),
    path('login/', views.handleLogin, name='handleLogin'),
    path('logout/', views.handleLogout, name='handleLogout'),

]
