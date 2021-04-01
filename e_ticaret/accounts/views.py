from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from .forms import Login,Register
from django.contrib import messages
from  django.contrib.auth.decorators import login_required

def loginViews(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request,username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect("anasayfa")
                else:
                    messages.info(request,"kullanacı aktif değil")
            else:
                messages.info(request,"kullanıcı adı ve ya şifre hatalı")
    else:
        form = Login()

    return render(request,"login.html",{"form":form})    


def registerView(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Başarılı Bir Şekilde Kayıt Oldunuz Lütfen Giriş Yapınız")
            return redirect("login")
    else:
        form = Register()

    return render(request,"register.html",{"form":form})

def user_logout(request):
    logout(request)
    return redirect("anasayfa")
    
@login_required(login_url="login")
def dashbord(request):
    currunt_user = request.user

    return render(request,"my-account.html")



                     
