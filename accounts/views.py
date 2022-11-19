from django.shortcuts import render, redirect # redirect yönlendirme için import edildi 
from.forms import LoginForm   #forms.py import edildi
from.forms import RegisterForm  
from django.contrib.auth import authenticate, login #kullanıcının sisteme giriş yapabilmesi için import ettik.

from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy

def login_view(request):
    form=LoginForm(request.POST or None)
    if form.is_valid(): #eğer kullanıcı doğru ise
        username=form.cleaned_data.get('username') #formdan gelen kullanıcı adı ve şifreyi değişkene atadık
        password=form.cleaned_data.get('password') #cleaned_data.get() metodu is_valid metodu true old kullanılabilen bir metod
        email=form.cleaned_data.get('email')
        user=authenticate(username=username,password=password,email=email) #kullanıcıyı sisteme dahil etmeden önce bu kullanıcıyı sisteme dahil etmemiz gerekir.

        login(request,user)# eğer authenticate kullanıcıyı dogruladıysa user atadık ve login ile kayıt ettik
        return redirect('home')  #accounts için html dosyası oluşturalım
    return render(request,'accounts/form.html',{'form':form, 'title':'Giriş Yap'})   #bu form için temp oluşturmak gerekiyor.



def register_view(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password1') # formdaki parolayı getirdik
         #user.password=password #girilen parolayı yeni parolamız olarak atadık fakat doğrudan atama iişlemi yapamayız çünkü user şifresini admin göremez. fakat django şifreyi elde etmemiz için fonksiyon sağlıyor
        user.set_password(password)
        #user.is_staff=True
        user.save() # user bilgilerini aldık ve bu metod ile kullanıcıyı database'e kaydediyoruz
        
        new_user=authenticate(username=user.username, password=password,email=user.email)
        login(request,new_user) # djangonun bize sağlamış old method new_user ın bilgilerini veriyoruz
        return redirect('home') # kullanıcıyı redirect ile home sayfasına yönlendiriyoruz.  
    return render(request,'accounts/form.html',{'form':form ,'title':'Üye Ol'})
# view de fonk oluşturduk şimdide adresi oluşturmamız lazım account/urls.py de
 
