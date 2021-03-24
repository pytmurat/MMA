from django.contrib import admin
from .models import FormModel

class FormAdmin(admin.ModelAdmin):
    list_display = ("isim","email","konu","message")


admin.site.register(FormModel,FormAdmin)
