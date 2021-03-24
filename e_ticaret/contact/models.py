from django.db import models

class FormModel(models.Model):
    isim = models.CharField(max_length=50,verbose_name="isim")
    email = models.EmailField(max_length=50,verbose_name="email")
    konu = models.CharField(max_length=100,verbose_name="konu")
    message = models.TextField(blank=True)

    def __str__(self):
        return self.isim
            