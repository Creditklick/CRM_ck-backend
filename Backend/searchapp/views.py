# from django.shortcuts import render , redirect
from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer , CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
# from .forms import SignUpForm , LoginForm
from .serializers import CustomerSerializer , CustomUserSerializer
from rest_framework import generics , status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password , make_password




@api_view(['GET'])
def searchapp(request):
    Name_query = request.GET.get('Name_query', '')
    Account_Number_query = request.GET.get('Account_Number_query', '')
    Phone_Number_query = request.GET.get('Phone_Number_query', '')
    City_query = request.GET.get('City_query', '')
    SteftoNo_query = request.GET.get('SteftoNo_query', '')

    print("Name_query:", Name_query)
    print("Account_Number_query:", Account_Number_query)
    print("Phone_Number_query:", Phone_Number_query)
    print("City_query:", City_query)
    print("SteftoNo_query:", SteftoNo_query)




    customers = Customer.objects.all()

    if Name_query:
        customers = customers.filter(Name__icontains=Name_query)
    if Account_Number_query:
        customers = customers.filter(Account_Number__icontains=Account_Number_query)
    if Phone_Number_query:
        customers = customers.filter(Phone__icontains=Phone_Number_query)
    if City_query:
        customers = customers.filter(City__icontains=City_query)
    if SteftoNo_query:
        customers = customers.filter(SteftoNo__icontains=SteftoNo_query)

    if City_query and Name_query:
        customers = customers.filter(City__icontains=City_query, Name__icontains=Name_query)
    if SteftoNo_query and Name_query:
        customers = customers.filter(Name__icontains=Name_query, SteftoNo__icontains=SteftoNo_query)
    if SteftoNo_query and City_query:
        customers = customers.filter(City__icontains=City_query, SteftoNo__icontains=SteftoNo_query)

    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)





# @ensure_csrf_cookie
# def user_logout(request):
#     if request.method =='POST':
#         logout(request)
#         return JsonResponse({'message': 'logged out successfully'})
#     else:
        
#         return JsonResponse({'error': 'Method not allowed'}, status=405)





@csrf_exempt
def user_logout(request):
    if request.method in ['GET', 'POST']:
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({'message': 'Logged out successfully'})
        else:
            return JsonResponse({'error': 'User is not authenticated'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)







@api_view(['POST'])
def register_user(request):
    serializer=CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        password=request.data.get('password')
        hashed_password=make_password(password)
        serializer.validated_data['password']=hashed_password
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        try:
            user=CustomUser.objects.get(username=username)
            
            print("retrived user:", user)
        except CustomUser.DoesNotExist:
            print("user not found")
            return Response({'error':'user not found'}, status=status.HTTP_404_NOT_FOUND)
        if check_password(password, user.password):
            print('password matched')
            return Response({'message': 'Login successful','session_key': request.session.session_key})
        else:
            print('invalid password')
            return Response({'error': 'Login invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        print('username and password is required ')
        return Response({'error': 'username and password is required'}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def test_session(request):
    request.session['test_key'] = 'test_value'
    return JsonResponse({'session_key': request.session.session_key})
