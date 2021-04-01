from .views import loginViews,registerView,user_logout,dashbord
from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.loginViews,name="login"),
    path("register/",views.registerView,name="register"),
    path("logout/",views.user_logout,name="logout"),
    path("dashbord/",views.dashbord,name="dashbord"),


]
