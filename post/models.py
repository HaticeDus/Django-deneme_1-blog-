#from unittest.util import _MAX_LENGTH
from tabnanny import verbose
from django.db import models
from django.urls import reverse


# Create your models here.

#post adında bir model oluşturduk. 
# models kütüphanesinden Model class'ını çağırdık bu şekilde bir kalıtım sağladık. 
#daha sonra bir post'da olması gereken en temel şeyleri tanımladık. 
# Bu veri türlerini Model kütüphanesinden çağırdık.

class Post(models.Model): 
   title=models.CharField(max_length=120,verbose_name='Başlık') #baslik
   content=models.TextField(verbose_name='İçerik')# metin
   publishing_date=models.DateTimeField(verbose_name='yayımlanma Tarihi',auto_now_add=True)#yayimlanma_tarihi

#özetle her model veri tabanında bir tabloya denk gelir.
#Bu modelde tablonun ismi "post", deiğer tanımladığımız alanlarda tablonun alanlarıdır.  

def __str__(self):# str fonk pythonda özel bir fonk.
   return self.title # diyerek postun başlığı neyse bize onu gösterecek

def get_absolute_url(self): #burda başka bir isim verilebilir fakat djangoda genel olarak bu isim verilir.
  # return "/post/{}".format(self.id)
   return reverse('post:detail', kwargs={'id': self.id})



