from django.db import models
import datetime
# Create your models here.

############# Database Table of Name Order #################
class Order(models.Model):
    Product_Id=models.CharField(max_length=20)
    Product_Name=models.CharField(max_length=35)
    Product_Price=models.CharField(max_length=10)
    Product_Quantity=models.CharField(max_length=5)
    Product_Details=models.TextField()
    Product_Seller=models.CharField(max_length=50)
    Product_Order_Date=models.CharField(default=datetime.datetime.now().strftime('%d/%m/%Y'),max_length=30)
    User_Name=models.CharField(max_length=50)
    User_Email=models.EmailField()
    User_Address=models.TextField()
    Tracking_Address=models.CharField(default="EwebgoStore",max_length=70)
    User_Number=models.CharField(max_length=15)
    Payment_Status=models.CharField(max_length=25)


############# Database Table of Name Cart #################
class Cart(models.Model):
    User_id=models.CharField(max_length=15)
    Product_id=models.CharField(max_length=15)
    Product_Name = models.CharField(max_length=35)
    Product_Price = models.CharField(max_length=10)
    Product_Quantity = models.CharField(max_length=5)
    Product_Details = models.TextField()
    Product_Add_Date=models.CharField(default=datetime.datetime.now().strftime('%d/%m/%Y'),max_length=30)
    Product_Seller = models.CharField(max_length=50)
    Product_image=models.ImageField(default="userzone/Cart/ProductImages/fav.png",upload_to="userzone/Cart/ProductImages")

