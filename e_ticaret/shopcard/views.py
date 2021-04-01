from django.shortcuts import render ,get_object_or_404,redirect
from django.contrib.auth.models import User
from .models import ShopCardModel
from django.contrib import messages
from shop.models import PhoneModel
from .models import ShopCardModel,ShopCard_item


def AAAAA(request):
    

    if request.user.is_authenticated:
        
        model = ShopCardModel.objects.get(user=request.user).items.all()
        return render(request,"wishlist.html",{"model":model})
    else:

        return render(request,"wishlist.html")


    



def card_addd(request,pk):
    aaa = get_object_or_404(PhoneModel,pk=pk)
    order_item, created = ShopCard_item.objects.get_or_create(
        productd = aaa,
        user = request.user,
        is_deleted = False
    )
    order_qs = ShopCardModel.objects.filter(user=request.user, is_deleted=False)

    if order_qs.exists():#doluysa
        order = order_qs[0]

        if order.items.filter(productd__pk=aaa.pk).exists():
            order_item.quantity += 1
            order_item.save()
            #messages.info(request, "Added quantity Item")
            return redirect("shopPage")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("shopPage")
    else:
       
        order = ShopCardModel.objects.create(user=request.user)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("shopPage")


    

    