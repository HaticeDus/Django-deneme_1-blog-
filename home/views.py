from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request) : #home_view() python fonk, request'de parametre(genel olarak bu yazılır) yani bu komut kullanıcının isteklerini yerine getiriyor.
  if request.user.is_authenticated:
     context={
    'isim': 'Hatice',
     }
  else:
      context={
        'isim': 'Misafir',
      }   
  return render(request,'home.html',context)
