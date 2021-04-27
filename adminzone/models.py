from django.db import models
import datetime
# Create your models here.

############# Database Table of Name Product it will contains Product added by admin #################
class Product(models.Model):
    Item_id=models.CharField(max_length=20,auto_created=True,primary_key=True)
    Item_name=models.CharField(max_length=70)
    Author=models.CharField(default='Ewebgo',max_length=50)
    Type=models.CharField(default='Item',max_length=20)
    Item_type=models.CharField(max_length=50)
    Price=models.CharField(max_length=12)
    Quantity=models.CharField(max_length=6)
    Sellars_Name=models.TextField()
    Sellars_Shop_Address=models.TextField()
    Post_Date=models.CharField(default=datetime.datetime.now().strftime('%d/%m/%Y'),max_length=30)
    Item_Image=models.ImageField(default="adminzone/Product_Images/fav.png", upload_to="adminzone/Product_Images")
    Extra_Images1=models.ImageField(default="adminzone/Product_Images/fav.png", upload_to="adminzone/Product_Images")
    Extra_Images2=models.ImageField(default="adminzone/Product_Images/fav.png", upload_to="adminzone/Product_Images")
    Descriptions=models.TextField()
    Specifications=models.TextField()
    Updater_Admin_Id=models.CharField(max_length=100)

############# Database Table of Name Admins. It saved details of an admin registration #################
class Admins(models.Model):
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
    UserType=models.CharField(max_length=20,default='Admin')
    User_Image=models.ImageField(default="adminzone/mUser.png", upload_to="adminzone/Admin_Images")
    Cart_Item=models.TextField()
    Balance=models.CharField(max_length=7,default=0)
    Date_of_Register=models.CharField(default=datetime.datetime.now().strftime('%d/%m/%Y'),max_length=30)

