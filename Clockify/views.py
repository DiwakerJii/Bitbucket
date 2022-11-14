from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def home(request):
    return render(request, "clockify/index.html")


def signup(request):
    
    if request.method == "POST":
        username = request.POST.get('username', None)
        fname = request.POST.get('fname', None)
        lname = request.POST.get('lname', None)
        mobile = request.POST.get('mobile', None)
        email= request.POST.get('email', None)
        pass1 = request.POS.get('pass1', None)
        pass2 = request.POST.get('pass2', None)

        myuser = User.objects.created_user(username, email, mobile, pass1 )
        myuser.first_name = fname
        myuser.last_name = lname 

        myuser.save()
        messages.success(request, "Your Account has been successfully created. ")

        return redirect('signin')




def signin(request):
    return render(request, "clockify/signin.html")

def signout(request):
    pass
