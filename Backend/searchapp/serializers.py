from rest_framework import serializers
from .models import Customer, CustomUser

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = CustomUser
#         fields=('id','username','name','email','password','employee_code','registration_date')



class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields=('id','username','name','email','password','employee_code','registration_date')

        def create(self, validated_data):
            password=validated_data.pop('password')
            user=CustomUser.objects.create_user(password=password, **validated_data)