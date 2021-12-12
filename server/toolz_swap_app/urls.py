from django.urls import path

from . import views

urlpatterns = [
    path('api/user', views.users_view),
    path('auth/login', views.login),
    path('auth/logout', views.logout)
]
