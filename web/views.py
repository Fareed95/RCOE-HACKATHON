from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest

# Create your views here.
def index(request):
    return render(request,'home.html')

def student_login_view(request):
    # Implement your student login logic here
    return render(request, 'studentauth/register.html')

def mentor_login_view(request):
    # Implement your mentor login logic here
    return render(request, 'mentor_login.html')

def apply_for_mentor_view(request):
    # Implement your apply for mentor logic here
    return render(request, 'apply_for_mentor.html')
@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'studentauth/register.html',{'form':form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'studentauth/login.html',{'form':form}) 

@auth
def dashboard_view(request):
    return render(request, 'studentauth/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')