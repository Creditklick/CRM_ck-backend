from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import UserProfile

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search')


class searchForm(forms.Form):
    SteftoNo_query=forms.CharField(label='Search by SteftoNo' , required=False)
    Name_query=forms.CharField(label='Search by Name' , required=False)
    Account_Number_query=forms.CharField(label='Search by Account' , required=False)
    Phone_Number_query=forms.CharField(label='Search by Phone' , required=False)
    City_query=forms.CharField(label='Search by City' , required=False)




