from django.urls import path
from . import views
from .views import shopPage,kategoryView,detayPage

urlpatterns = [
    path("",views.shopPage,name="shopPage"),
    path("kategory/<slug:kategory_slug>",views.kategoryView,name="kategorw"),
    path("detail/<int:pk>",views.detayPage,name="detay"),

]
