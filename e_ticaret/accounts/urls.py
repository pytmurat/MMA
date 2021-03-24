from .views import loginViews
from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.loginViews,name="login"),
]
