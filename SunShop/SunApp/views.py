from django.shortcuts import render, HttpResponse
from .models import TodoItem
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def pending(request):
    items = TodoItem.objects.all()
    return render(request, 'pending.html',{"todo":items})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return render(request, 'home.html')
        else:
            messages.error(request, ("Error logging in - please try again..."))
            return render(request, 'login_page.html')
    else:
        return render(request, 'login_page.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out!"))
    return render(request, 'login_page.html')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate User
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return render(request, 'login_page.html')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



