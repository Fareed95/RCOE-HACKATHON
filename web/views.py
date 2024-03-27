from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'home.html')

def mentor_login_view(request):
    # Implement your mentor login logic here
    return render(request, 'mentor_login.html')

def apply_for_mentor_view(request):
    # Implement your apply for mentor logic here
    return render(request, 'apply_for_mentor.html')

@login_required(login_url='login')
def HomePage(request):
    return render (request,'studentauth/dashboard.html')

def SignupPage(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            # Create the user with keyword arguments
            my_user = User.objects.create_user(username=uname, email=email, password=pass1, first_name=first_name, last_name=last_name)
            my_user.save()
            return redirect('login')

    return render(request, 'studentauth/register.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'studentauth/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')