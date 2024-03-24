from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import StudentLoginForm, MentorLoginForm, MentorApplicationForm

def index(request):
    return render(request, 'home.html')

def student_login_view(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
    else:
        form = StudentLoginForm()
    return render(request, 'student_login.html', {'form': form})

def mentor_login_view(request):
    if request.method == 'POST':
        form = MentorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
    else:
        form = MentorLoginForm()
    return render(request, 'mentor_login.html', {'form': form})

def apply_for_mentor_view(request):
    if request.method == 'POST':
        form = MentorApplicationForm(request.POST)
        if form.is_valid():
            # Process the form data and save to database
            # You can access form data using form.cleaned_data
            return redirect('home')  # Redirect to home page after successful application
    else:
        form = MentorApplicationForm()
    return render(request, 'apply_for_mentor.html', {'form': form})
