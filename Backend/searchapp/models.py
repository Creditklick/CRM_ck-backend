
# import datetime

# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.db import models
# from .models import CustomUserPermission


# # Create your models here.

# class Customer(models.Model):
#     SteftoNo=models.CharField(max_length=20, default=0000)
#     Name=models.CharField(max_length=20)
#     Account_Number=models.CharField(max_length=20, unique=True)
#     City=models.CharField(max_length=20)
#     Phone=models.IntegerField(max_length=10, unique=True)
#     Email=models.EmailField()
#     Address=models.CharField(max_length=50)
#     Process_Name=models.CharField(max_length=20)
#     DOB=models.DateField(max_length=20)



# # class UserProfile(models.Model):
# #     username=models.OneToOneField(User, on_delete=models.CASCADE)
# #     Email=models.EmailField( blank=True)
# #     EmpCode=models.CharField(max_length=10)
# #     Process=models.CharField(max_length=20 , blank=True)
# #     RegisterDate= models.DateTimeField(auto_now_add=True)

# #     class Meta:
# #         db_table='custom_user_profile_table'
    


# class CustomUser(AbstractUser):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     employee_code = models.CharField(max_length=50)
#     registration_date = models.DateField(auto_now_add=True)

#     groups = models.ManyToManyField(
#         Group,
#         through='CustomUserGroup',
#         through_fields=('user', 'group'),
#         related_name='custom_users',
#     )

#     user_permissions = models.ManyToManyField(
#         Permission,
#         through=CustomUserPermission, 
#         through_fields=('user', 'permission'),
#         related_name='custom_users_permissions', 
#     )

# class CustomUserPermission(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     permission = models.ForeignKey(Permission, on_delete=models.CASCADE)


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .permissions import CustomUserPermission 

class Customer(models.Model):
    SteftoNo = models.CharField(max_length=20, default=0000)
    Name = models.CharField(max_length=20)
    Account_Number = models.CharField(max_length=20, unique=True)
    City = models.CharField(max_length=20)
    Phone = models.IntegerField(unique=True)
    Email = models.EmailField()
    Address = models.CharField(max_length=50)
    Process_Name = models.CharField(max_length=20)
    DOB = models.DateField()

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    employee_code = models.CharField(max_length=50)
    registration_date = models.DateField(auto_now_add=True)

    groups = models.ManyToManyField(
        Group,
        through='CustomUserGroup',
        through_fields=('user', 'group'),
        related_name='custom_users',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        through=CustomUserPermission,
        through_fields=('user', 'permission'),
        related_name='custom_users_permissions',
    )

class CustomUserGroup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
