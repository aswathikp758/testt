from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
]
