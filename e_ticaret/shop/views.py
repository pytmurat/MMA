from django.shortcuts import render,get_object_or_404
from .models import PhoneModel,kategory

def shopPage(request):

    model = PhoneModel.objects.all()
    kmodel = kategory.objects.all()
    adet = PhoneModel.objects.all().filter(yayinda_mi=True).count()
    


    contex = {

        "model":model,
        "kmodel":kmodel,
        "adet":adet

    }

    return render(request,"shop.html",contex)

def kategoryView(request,kategory_slug):
    model = PhoneModel.objects.all().filter(kategorys__slug = kategory_slug)
    adet = PhoneModel.objects.all().filter(yayinda_mi=True,kategorys__slug=kategory_slug).count()
    kmodel = kategory.objects.all()

 
    contex = {
        "phoneModel":model,
        "adet":adet,
        "kmodel":kmodel,
    }

    return render(request,"kategory.html",contex)

    
def detayPage(request,pk):
    model = get_object_or_404(PhoneModel,pk=pk)
    stokadeti = PhoneModel.objects.only("stok").count()
   
    return render(request,"shop-detail.html",{
        "model":model,
        "stokadeti":stokadeti,
    })

def search(request):
    model = PhoneModel.objects.filter(name__contains = request.GET["search"])


    return render(request,"shop.html",{
        "model":model,
        

        })






