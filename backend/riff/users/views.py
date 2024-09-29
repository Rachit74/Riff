# Rest framework imports

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Django imports
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token # used to generate csrf token
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# App imports
from .models import Client

from .serializers import ClientSerializer

# Views

"""
View to handle user login at /users/login/
"""
class LoginView(APIView):
    """
    post method to handle post requests
    gets username and password and autheticates them
    if the use is found then user is logged in else Invalid Credentials error!
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if not user is None:
            login(request, user=user)
            return Response('Login Succesfull', status=status.HTTP_200_OK)
        
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)


"""
View to handle user registration at /users/register/
"""
class RegisterView(APIView):
    """
    post method to handle post requests
    takes in username, email and password to create a user account
    validates the data and hashes the password (overridden in create method in serializers.py)
    """
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer
            user.save()
            return Response('Account Created', status=status.HTTP_201_CREATED)
        
        return Response('Acccount Creation FAILED', status=status.HTTP_400_BAD_REQUEST)
    
"""
Profile View
returns the user profile of current logged in user
user must be authenticated to access this endpoint at /users/profile/
"""
class ProfileView(APIView):
    # permission_classes = [IsAuthenticated]

    """
    get method to handle get request
    serializes the current user data and return it in the response
    """
    def get(self, request):
        user = request.user
        serializer = ClientSerializer(user)
        return Response(serializer.data)

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    """
    get method to handle get request
    logs the user out
    """
    def get(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


"""
Token View
used to generate csrf token which can be used in frontend while form submission
token access at /users/token
"""
class TokenView(APIView):
    """
    get method to handle get request
    returns a csrf token
    """
    def get(self, request):
        csrf_token = get_token(request)
        return Response(csrf_token)