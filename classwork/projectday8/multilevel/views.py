from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'multilevel/homepage.html')
def aboutus(request):
    return render(request,'multilevel/aboutus.html')