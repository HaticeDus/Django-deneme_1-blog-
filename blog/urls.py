"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home.views import home_view

urlpatterns = [                      #web sitesindeki adreslerimizin tanımlandığı yerdir.
    path('admin/', admin.site.urls), #düzenli ifadenin bittiğini göstermek için $ işareti konur fakat admin url için konulmamış 
                                     #çünkü admin uygulaması için birden fazla adrese ihtiyaç vardır.  
                                     #, sonra diğer admin adresleri çağırılmış. 
    path('',home_view, name='home'),

    path('post/',include('post.urls')),#post dosyasındaki urls.py dosyasını referans vermiş olduk

    path('accounts/',include('accounts.urls')) #accounts/urls.py 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #static media pathini media root url ile bağlıyoruz