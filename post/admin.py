from django.contrib import admin

# Register your models here.
from .models import Post
#from post.models import Post



class PostAdmin(admin.ModelAdmin):

 list_display = ['title','publishing_date']#postumuzdaki alanları ekranda gösteriyoruz.
 list_display_links=['publishing_date']#link haline getirip detaylara bakabiliyoruz
 list_filter=['publishing_date'] #yayımlanma tarihine göre filtreledik
 search_fields=['title','content'] #başlık ve metin alanlarına göre arama yapabiliriz.
 list_editable=['title']# güncelleme yapmak için
 
 class Meta:
        model=Post #bu modelin hangi uygılamauya ait old. belirttik


admin.site.register(Post,PostAdmin) #PostAdmin classını admin paneline ekliyoruz