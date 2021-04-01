from django.contrib import admin
from .models import FormModel,Contact

class FormAdmin(admin.ModelAdmin):
    list_display = ("isim","email","konu","message")

class ContactAdmin(admin.ModelAdmin):
    list_display = ("baslık","acıklama","adres","email","telefon")


admin.site.register(FormModel,FormAdmin)
admin.site.register(Contact,ContactAdmin)
