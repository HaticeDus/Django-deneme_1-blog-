# ilk olarak blog taki ana urls bu urls i import edilmeli!

from django.urls import path
from .views import * #bütün verileri içe aktarıyorum (* anlamı bütün fonk getir demek.) 

app_name='accounts'


#temel post işlemleri ile ilgili adresleri tanımlayalım

urlpatterns = [                      
                                   
    path('login/',login_view, name='login'),

    path('register/',register_view, name='register')
    
]
   