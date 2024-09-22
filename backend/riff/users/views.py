from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate, login, logout

from .models import Client

from .serializers import ClientSerializer

# Create your views here.

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if not user is None:
            login(request, user=user)
            return Response('Login Succesfull', status=status.HTTP_200_OK)
        
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer
            user.save()
            return Response('Account Created', status=status.HTTP_201_CREATED)
        
        return Response('Acccount Creation FAILED', status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = ClientSerializer(user)
        return Response(serializer.data)
