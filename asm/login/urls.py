from django.urls import re_path
from . import views

urlpatterns= [
    path('login/', views.login)
    path('signup/', views.signup)
]