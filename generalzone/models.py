from django.db import models
import datetime
# Create your models here.

############# Database Table of Name Register for storing user details of regestration #################
class Register(models.Model):
    User_Id=models.CharField(max_length=15,auto_created=True)
    First_Name=models.CharField(max_length=40)
    Last_Name=models.CharField(max_length=40)
    Date_of_Birth=models.CharField(max_length=30)
    Gender=models.CharField(max_length=6)
    Father_Name=models.CharField(max_length=50)
    Address=models.TextField()
    Phone_Number=models.CharField(max_length=15,primary_key=True)
    Email_id=models.EmailField()
    Password=models.CharField(max_length=30)
    Security_Question=models.CharField(max_length=50)
    Security_Answer=models.CharField(max_length=50)
    UserType=models.CharField(max_length=20,default='User')
    User_Image=models.ImageField(default="userzone/mUser.png", upload_to="userzone/User_Images")
    Cart_Item=models.TextField()
    Balance=models.CharField(max_length=7,default=0)
    Date_of_Register=models.CharField(default=datetime.datetime.now().strftime('%d/%m/%Y'),max_length=30)

