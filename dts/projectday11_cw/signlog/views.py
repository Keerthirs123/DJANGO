from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout 
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('products')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def products(request):
    return render(request, 'products.html')

@login_required(login_url='/login/')
def logout_view(request):
    username = request.user.username  # store username before logout
    logout(request)
    return render(request, 'logout.html', {'username': username})


@login_required(login_url='/login/')    
def visitor_count(request):
    count = request.session.get('count', 0)
    count += 1
    request.session['count'] = count
    return render(request, 'visitorcount.html', {'count': count})    
