from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Customer App</h1><p><a href='/customers/add/'>Add Customer</a> | <a href='/customers/all/'>All Customers</a></p>")


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            customers = Customer.objects.all().order_by('name')
            return render(request, 'all_customers.html', {'customers': customers})
    else:
        form = CustomerForm()
    return render(request, "add_customer.html", {'form': form})

def all_customers(request):
    customers = Customer.objects.all().order_by('name')
    return render(request, 'all_customers.html', {'customers': customers})

def filtered_customers(request):
    customers = Customer.objects.filter(email__endswith="@example.com").order_by('name')
    return render(request, 'filtered_customer.html', {"customers": customers})
