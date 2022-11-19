from django.urls import path
from .views import * #bütün verileri içe aktarıyorum (* anlamı bütün fonk getir demek.) 

app_name='post'


#temel post işlemleri ile ilgili adresleri tanımlayalım

urlpatterns = [                      
                                   
    path('index/',post_index, name='index'),
    path('<int:id>/',post_detail, name='detail'),
    path('index/<int:id>/',post_detail, name='test'),
    path('create/',post_create, name='create'),
    path('<int:id>/update/',post_update, name='update'),
    path('<int:id>/delete/',post_delete, name='delete'),
    path('hatice/',post_merhaba,name='hatice'),
    path('kareal/<int:sayi>/',kare_al)
]
    #bu adreslerin verilerini oluşturacağız


