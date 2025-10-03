from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.core.mail import EmailMessage

# Create your views here.
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product=form.save()
            return redirect('product_details', pk=product.pk)
        else:
            form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_details(request, pk):
    product=get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})        

def pdf_download(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template=get_template('product_pdf.html')
    html=template.render({'product':product})

    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']=f'attachment; filename="product_{product.pk}.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=400)
    return response

def send_email(request,pk):
    product=get_object_or_404(Product, pk=pk)
    subject=f"product details: {product.name}"
    message=f"Product Name: {product.name}\nPrice: {product.price}\nDescription: {product.description}"
    send_email(subject, message, 'from@example.com', ['to@example.com'])
    return HttpResponse("Email sent successfully") 
    