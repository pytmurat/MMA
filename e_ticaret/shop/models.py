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

    bellekler = [("2 gb","2 gb"),("4 gb","4 gb"),("6 gb","6 gb"),("8 gb","8 gb"),("12 gb","12 gb"),("16 gb","16 gb"),("32 gb","32 gb")]
    hafıza = [("16 gb","16 gb"),("32 gb","32 gb"),("64 gb","64 gb"),("128 gb","128 gb "),("256 gb","256 gb"),("512 gb","512 gb")]
    renkler = [("Siyah","Siyah"),("Beyaz","Beyaz"),("Gold","Gold"),("Gri","Gri"),("Kırmızı","Kırmızı"),("Gümüş","Gümüş"),("Grafit","Grafit"),("Pasifik Mavisi","Pasifik Mavisi"),("Yeşil","Yeşil"),("Mavi","Mavi"),("Uzay Grisi","Uzay Grisi"),("Gece Yeşili","Gece Yeşili"),("Mor","Mor"),("Sarı","Sarı"),("Rose Gold","Rose Gold"),("Pembe","Pembe")]
    kamera = [("12 px","12 px"),("16 px","16 px"),("32 px","32 px"),("64 px","64 px"),("128 px","128 px")]
    name = models.CharField(max_length=100,verbose_name="isim")
    renk = models.CharField(max_length=100,verbose_name="renk",choices=renkler,default=1)
    fiyat = models.PositiveIntegerField(verbose_name="fiyat")
    yeniFiyat = models.PositiveIntegerField(verbose_name="yeni Fiyat")
    hafıza = models.CharField(verbose_name="hafıza",choices=hafıza,default=1,max_length=20)
    bellek = models.CharField(verbose_name="rem",max_length=20,choices=bellekler,default=1)
    kamera  = models.CharField(verbose_name="MegaPixel",choices=kamera,default=1,max_length=20)
    image = models.ImageField(blank=True,null=True ,upload_to=r"C:\Users\windows\Desktop\django\e_ticaret\media")
    kategorys = models.ForeignKey(kategory,null=True,on_delete=models.DO_NOTHING)
    yayinda_mi = models.BooleanField(verbose_name="yaynda mı",default=True,null=True,blank=True)
    aciklama = models.CharField(max_length=300,verbose_name="açıklama",null=True,blank=True)
    stok = models.PositiveIntegerField(verbose_name="stok",null=True,blank=True)




    def __str__(self):
       return self.name




   
      