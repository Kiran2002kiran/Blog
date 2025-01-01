from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog_app.models import Country , User , Blog
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from .serializer import RegisterSerializer , CountrySerializer , UserSerializer , BlogSerializer
from django_filters.rest_framework import DjangoFilterBackend





class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    

class LogoutView(APIView):
    def post(self,request):
        token = RefreshToken(request.data["refresh"])
        token.blacklist()
        return Response({"message" : "Logged out successfully"})



class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["continent", "country"]
    permission_classes = [AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country", "date_of_birth"]
    permission_classes = [AllowAny]

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["created_by", "created_at"]
    permission_classes = [IsAuthenticated] 
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    

    
    
