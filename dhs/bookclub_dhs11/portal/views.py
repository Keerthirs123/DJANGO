from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form}) 

@login_required
def welcome(request):
    count=request.session.get('count',0)
    count+=1
    request.session['visit_count']=count
    return render(request, 'welcome.html',{'username':request.username})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
   