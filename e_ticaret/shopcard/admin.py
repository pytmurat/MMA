from django.contrib import admin
from .models import ShopCardModel,ShopCard_item



class ShopCardItemAdmin(admin.ModelAdmin):
    list_display = ["productd","price","is_deleted"]

class ShopCardAdmin(admin.ModelAdmin):
    list_display = ["user","shopcard_update"]    


admin.site.register(ShopCard_item,ShopCardItemAdmin)
admin.site.register(ShopCardModel,ShopCardAdmin)




