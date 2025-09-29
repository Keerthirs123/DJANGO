from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status   
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
class ProductListCreateView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailView(APIView):
    def put(self,request,pk):
        try:
             product=Product.objects.get(pk=pk)
        except Product.DoesNotExist:
             return Response({"error":"Product not found "},status= status.HTTP_404_NOT_FOUND)
                
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        product.delete()
        return Response({"message": "Product deleted"},status=status.HTTP_204_NO_CONTENT)
        
