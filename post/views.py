from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect  
from.models import Post
from .forms import PostForm
from django.contrib import messages


# Create your views here.

def post_index(request):
    posts=Post.objects.all()
    return render(request,'post/index.html',{'posts': posts}) #templates klasörü içide oluşturduğumuz post dosyası içindeki html dosyasının adresini verdik 2. parametre olarak.


def post_detail(request,id):
    post=get_object_or_404(Post,id=id)
    context={
        'post': post,
    }
    return render(request,'post/detail.html', context)


def post_create(request):
    # if request.method=="POST":
    # print(request.POST)

    # title=request.POST.get('title') #title alanındaki değeri title değişkenine aktarıyorum.
    # content=request.POST.get('content')
    # Post.objects.create(title=title,content=content)

    # if request.method=="POST": #formdan gelen bilgileri kaydet
       
    #     form=PostForm(request.POST)
    #     if form.is_valid(): #formun doğru bir şekilde doldurulup doldurulmadığını kontrol ediyoruz. ardından form bilgileri doğruysa 
    #         form.save() #metodunu çalıştırıyoruz
    # else:
    #     #Formu kullanıcıya göster    
    #     form=PostForm()
    
    form=PostForm(request.POST or None)#bunun anlamı şu eğer request.POST dolu gelirse parametre olarak al eğer boş gelirse hiçbir parametre alma böylelikle her iki senaryoya uyacak şekilde dinamik hale getirdik.   
    if form.is_valid():
        post=form.save()
        messages.success(request, 'Başarılı bir şekilde Oluşturdunuz.')
        #return HttpResponseRedirect(post.get_absolute_url())

    context={
        'form':form,
    }

    return render(request,'post/form.html',context)


def post_update(request, id):

    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)#forma bilgileri bu şekilde aktarıyoruz. kullanıcının yapacağı değişiklikleri kaydetmek yine save() metodunu kullanıyoruz.
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde Oluşturdunuz.',extra_tags='mesaj-basarili')
       
        
        return HttpResponseRedirect(post.get_absolute_url())
    context={ #form nesnesini içerik olarak gönderelim
        'form':form,
    }    
    #return HttpResponse('Burası Post update sayfası')#daha sonra render metoduna çevirelim
    return render(request,'post/form.html', context)

def post_delete(request,id):
    post = get_object_or_404(Post, id=id)
    return redirect('post:index')

def post_merhaba(request):
    
    return HttpResponse("merhaba")



def kare_al(request,sayi):
    
    return HttpResponse(sayi*sayi)
