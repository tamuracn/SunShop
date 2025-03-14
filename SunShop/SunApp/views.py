from django.shortcuts import render, HttpResponse
from .models import TodoItem,PurchaseRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRequestForm
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, 'home.html')

def purchase_request(request):
    purchase_requests = PurchaseRequest.objects.all()
    return render(request, 'purchase_request.html',{"purchase_requests":purchase_requests})

def request_record(request,pk):
    request_records = PurchaseRequest.objects.get(id=pk)
    # Look up PurchaseRequest by id
    return render(request, 'request_record.html',{"request_records":request_records})

def add_request(request):
    form = AddRequestForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_request = form.save()
            messages.success(request, ("Request has been added!"))
            return redirect('purchase_request')
    
    return render(request, 'add_request.html',{"form":form})

def delete_request(request,pk):
    delete_req = PurchaseRequest.objects.get(id=pk)
    delete_req.delete()
    messages.success(request, ("Request has been deleted!"))
    return  redirect('purchase_request') # render(request, 'purchase_request.html')

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


def update_request(request,pk):
    current_req = PurchaseRequest.objects.get(id=pk)
    form = AddRequestForm(request.POST or None, instance=current_req)
    if form.is_valid():
        form.save()
        messages.success(request, ("Request has been updated!"))
        return redirect('purchase_request') #render(request, 'purchase_request.html')

    return render(request, 'update_request.html',{"form":form})
