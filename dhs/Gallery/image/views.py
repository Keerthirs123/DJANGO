from django.shortcuts import render

# Create your views here.
def view_image(request):
    return render(request, 'gallery.html')

def contact_me(request):
    return render(request,'contact.html')