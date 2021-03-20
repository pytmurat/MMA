from django.db import models


class kategory(models.Model):
    name = models.CharField(max_length=100,verbose_name="kategori")
    slug = models.SlugField(max_length=100,verbose_name="slug",unique=True)
    def __str__(self):
        return self.name


class PhoneModel(models.Model):
    class Mete:
        verbose_name = "Telefon"
        verbose_name_plural ="Telefonlar"

    bellekler = [("1","2 gb"),("2","4 gb"),("3","6 gb"),("4","8 gb")]
    hafıza = [("1","16 gb"),("2","32"),("3","64"),("4","128"),("5","256")]
    renkler = [("1","Siyah"),("2","Beyaz"),("3","Gold"),("4","Gri"),("5","Kırmızı")]
    kamera = [("1","12"),("2","16"),("3","21")]
    name = models.CharField(max_length=100,verbose_name="isim")
    renk = models.CharField(max_length=10,verbose_name="renk",choices=renkler,default=1)
    fiyat = models.PositiveIntegerField(verbose_name="fiyat")
    yeniFiyat = models.PositiveIntegerField(verbose_name="yeni Fiyat")
    hafıza = models.CharField(verbose_name="hafıza",choices=hafıza,default=1,max_length=20)
    bellek = models.CharField(verbose_name="rem",max_length=20,choices=bellekler,default=1)
    kamera  = models.CharField(verbose_name="MegaPixel",choices=kamera,default=1,max_length=20)
    image = models.ImageField(blank=True,null=True ,upload_to=r"C:\Users\windows\Desktop\django\e_ticaret\media")
    kategorys = models.ForeignKey(kategory,null=True,on_delete=models.DO_NOTHING)
    yayinda_mi = models.BooleanField(verbose_name="yaynda mı",default=True,null=True,blank=True)




    def __str__(self):
       return self.name




   
      