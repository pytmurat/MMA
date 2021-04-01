from django.urls import path
from .import views
from .views import card_addd,AAAAA

urlpatterns = [
    #path("<int:pk>",views.modelll,name="card"),
    path("<int:pk>",views.card_addd,name="shopcarview"),
    path("wishlist",views.AAAAA,name="shopcarview"),


]
