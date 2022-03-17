from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .models import *



def index(request):
    return render(request, 'index.html')

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

