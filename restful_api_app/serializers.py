from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User   
        fields = ['id','first_name', 'last_name', 'phone_number', 'client_member_id', 'account_id']
        

