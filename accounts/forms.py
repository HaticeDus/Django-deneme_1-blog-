from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.conf import settings
from django.core.mail import send_mail


class LoginForm(forms.Form): # bu kayıtlı olan üyenin girşi
    username=forms.CharField(max_length=100,label='Kullanıcı Adı')
    password=forms.CharField(max_length=100,label='Parola', widget=forms.PasswordInput)
    email=forms.CharField(max_length=100,label='email')

    def clean(self):
         username=self.cleaned_data.get('username') 
         password=self.cleaned_data.get('password') 
         email=self.cleaned_data.get('email')

         if username and password:
            user=authenticate(username=username,password=password,email=email)
            if not user:
                raise forms.ValidationError('Kullanıcı adını veya parolayı yanlış girdiniz!')
         return super(LoginForm,self).clean()



class RegisterForm(forms.ModelForm): # yeni kaydolacak üyenin girşi Form 'u ModelForm olarak değiştiriyorum
    username=forms.CharField(max_length=100,label='Kullanıcı Adı')
    password1=forms.CharField(max_length=100,label='Parola', widget=forms.PasswordInput)
    password2=forms.CharField(max_length=100,label='Parola Doğrulama', widget=forms.PasswordInput)
    email=forms.CharField(max_length=100,label='email')
   
    class Meta: # ModelForm , bu formun hangi modeli referans alacağını gösterelim
        model=User #djangonun User modeli ve bunun için import işlemi var 
        fields = [   #hangi alanları kullanacağımızı belirttik
        'username',
        'password1',
        'password2',
        'email'
         ]

    def clean_password2(self): 
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Parolalar eşleşmiyor!") 
        return password2  

    # def clean_email(self):
    #     if self.cleaned_data.get('email').exists():
    #         raise forms.ValidationError('This email exists on system')
    #     return self.cleaned_data['email']  


class ContactForm(forms.Form):

    def get_info(self):
       
        username=self.cleaned_data.get('username') 
        email=self.cleaned_data.get('email')
        subject="Django Email Doğrulaması ile Kullanıcı Kaydı"
        message="başarılı bir şekilde kayıt yaptınız."

        msg = f'{username} with email {email} said:'
        msg += f'\n"{subject:}"\n\n'
        msg += ({message})

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )