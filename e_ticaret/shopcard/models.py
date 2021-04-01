from django.db import models
from django.contrib.auth.models import User
from shop.models import PhoneModel
from django.forms import ModelForm
from django.db.models.signals import post_save , m2m_changed#bu 2 satır da signal işlemleri için gerekli kutuphaneler
from django.dispatch import receiver

#bir shopcard olusturuken 2 sınıf olusturmak lazım 
 #1.sınıf shopcaritem olur
 # 2.kısım ise shopcarın kendısı



class ShopCard_item(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True)
    productd = models.ForeignKey(PhoneModel,on_delete=models.CASCADE)#product Phone modelden gelir ana model
    price = models.IntegerField(default=0) #price ise direk modelden gelecek 
    is_deleted = models.BooleanField(default=False) # ürün gostermede bız kullnıcaz
    quantity = models.IntegerField(default=1)


    
    def __str__(self):
        return self.productd.name




class ShopCardModel(models.Model):

    STATUS = [("waiting","beklemede"),("deleted","silindi")]
    user      = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True)
    items     = models.ManyToManyField(ShopCard_item,blank=True) #burda 1 item 1den fazla sepete eklı olabılır 1 sepet 1 den fazla item ıcerebılır
    status    = models.CharField(choices=STATUS , max_length=30,default="waiting")
    is_deleted = models.BooleanField(default=False) # ürün gostermede bız kullnıcaz

    
    def __str__(self):
        return self.status

    @property
    def shopcard_update(self):
        total_price = 0
        for item in self.items.all():#shopcarda ki bütün itemler i al 
            if self.status == "waiting" and item.is_deleted ==False:
                total_price += item.price
             #sinmedıyse hepsi aktif ise butun hepsini topla ve totalpriceye gonder
                
        self.totalprice = total_price
        self.save() #bu işlemleri kaydet
        print(self.totalprice)
        
        return self.totalprice
    
   

    


@receiver(post_save,sender=ShopCard_item)#shopcard itemde bir değişiklik olursa bunları uygula
def shop_card_item_reciver(sender,instance,created,*args ,**kwargs):
    if created == True:
        instance.price = instance.productd.fiyat #otomatikmal cart item in içindeki faiyatı productan alır
        instance.shopcard_update
        instance.save()
        #instance.shopcard_update


   


@receiver(m2m_changed,sender = ShopCardModel.items.through)
def shop_card_receiver(sender,instance,*args ,**kwargs):
    instance.shopcard_update     







           


    