from django.contrib import admin
from .models import PhoneModel,kategory

class KategoryModel(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}




class AdminModel(admin.ModelAdmin):
    list_display = ("name","renk","fiyat","yeniFiyat","hafıza","bellek","kamera","stok")


admin.site.register(PhoneModel,AdminModel)
admin.site.register(kategory,KategoryModel)


