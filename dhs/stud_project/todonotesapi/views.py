from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status ,permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import TodoNote
from .serializers import TodoNoteSerializer, UserSerializer
# Create your views here.

class SignUpView(APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token':token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class LoginView(APIView):
    def post(self, request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username, password=password)
        if user:
            token, _= Token.objects.get_or_create(user=user)
            return Response({'token':token.key, "username":user.username,})
        return Response({'error':'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class AddNoteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer =TodoNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListNotesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notes = TodoNote.objects.filter(user=request.user)
        serializer = TodoNoteSerializer(notes, many=True)
        return Response(serializer.data)