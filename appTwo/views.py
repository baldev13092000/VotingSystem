from django.shortcuts import render
from django.http import HttpResponse
from appTwo.forms import NewUserForm
from appTwo.forms import NewLoginForm
#from appTwo.models import User
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):

    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return render(request,'appTwo/signup_next.html')
        else:
            print("ERROR form invalid")
    return render(request,'appTwo/users.html',{'form':form})
def relative(request):
    return render(request,'appTwo/relative_url.html')
def login(request):
    formLogin = NewLoginForm()
    if request.method == "POST":
        formLogin = NewLoginForm(request.POST)

        if formLogin.is_valid():
            formLogin.save(commit = True)
            return index(request)
        else:
            print("ERROR form invalid")
    return render(request,'appTwo/login.html',{'form1':formLogin})
def validation1(request):
    return render(request,'appTwo/validation1.html')
def validation2(request):
    return render(request,'appTwo/validation2.html')
def validation3(request):
    return render(request,'appTwo/validation3.html')
def validation4(request):
    return render(request,'appTwo/validation4.html')
def validation5(request):
    return render(request,'appTwo/validation5.html')
def validation6(request):
    return render(request,'appTwo/validation6.html')
def validation7(request):
    return render(request,'appTwo/validation7.html')
def validation8(request):
    return render(request,'appTwo/validation8.html')
def validation9(request):
    return render(request,'appTwo/validation9.html')
def statistics(request):
    return render(request,'appTwo/statistics.html')
def signup_next1(request):
    return render(request,'appTwo/signup_next1.html')
def validation10(request):
    return render(request,'appTwo/validation10.html')
def validation11(request):
    return render(request,'appTwo/validation11.html')
def validation12(request):
    return render(request,'appTwo/validation12.html')
def NewSmartCard(request):
    return render(request,'appTwo/NewSmartCard.html')
