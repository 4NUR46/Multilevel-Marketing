from django.shortcuts import render,redirect,reverse
import datetime
from . models import Product,Admins
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
from userzone .models import Order
# Create your views here.

def adminhome(request):
    if request.session['userid']:
        itms=Product.objects.all()
        return render(request,'adminhome.html',{'itms':itms})
    else:
        return redirect(request,'login.html')


def AddItem(request):
    if request.session['userid']:
        if request.method=='POST':
            ItemName=request.POST['itemName']
            Author=request.POST['authorName']
            ItemType=request.POST['itemType']
            Price=request.POST['itemPrice']
            Quantity=request.POST['quantity']
            SellerName=request.POST['sellerName']
            SellerAddress=request.POST['sellerAddress']
            Description=request.POST['description']
            # Description=Descripte.split(".")
            Specification=request.POST['specifications']
            # Specification =Specificate.split(".")
            #ItemDisplayImage=request.POST['MyFile1']
            #ItemExtraImage2=request.POST['MyFile2']
            #ItemExtraImage3=request.POST['MyFile3']
            try:
                ItemDisplayImage = request.FILES['MyFile1']
                if ItemDisplayImage == '' or None:
                    ItemDisplayImage = 'fav.png'
            except:
                ItemDisplayImage = 'fav.png'
            try:
                ItemExtraImage2 = request.FILES['MyFile2']
                if ItemExtraImage2 == '' or None:
                    ItemExtraImage2 = 'fav.png'
            except:
                ItemExtraImage2 = 'fav.png'
            try:
                ItemExtraImage3 = request.FILES['MyFile3']
                if ItemExtraImage3 == '' or None:
                    ItemExtraImage3 = 'fav.png'
            except:
                ItemExtraImage3 = 'fav.png'

            PostDate=datetime.datetime.now().strftime('%d/%m/%Y')
            UpdaterId=request.session['userid']
            itemId=Price+PostDate[0:2]+UpdaterId[0:10]

            ItemDetails=Product(Item_name=ItemName,Author=Author,Item_type=ItemType,Price=Price,Quantity=Quantity,Sellars_Name=SellerName,Sellars_Shop_Address=SellerAddress,Item_Image=ItemDisplayImage,Extra_Images1=ItemExtraImage2,Extra_Images2=ItemExtraImage3,Descriptions=Description,Specifications=Specification,Updater_Admin_Id=UpdaterId,Post_Date=PostDate,Item_id=itemId)
            ItemDetails.save()
            return render(request,'AddItem.html',{'message':'Item added Sucessfully'})
        return render(request,'AddItem.html')
    else:
        return redirect(request,'login.html')


def adminProfile(request):
    if request.session['userid']:
        uid = request.session.get('userid')
        user = Admins.objects.all().filter(Phone_Number=uid)
        return render(request,'adminProfile.html',{'user':user})
    else:
        return redirect(request,'login.html')


def notifications(request):
    if request.session['userid']:
        uid = request.session.get('userid')
        itms = Product.objects.all()
        # addva = Cart.objects.all().filter(User_id=uid)
        # orders = Order.objects.all().filter(User_Number=uid)
        orders = Order.objects.all()
        return render(request,'notifications.html',{'orders':orders,'itms':itms})
    else:
        return redirect(request,'login.html')

def OrderDetails(request):
    if request.session['userid']:
        # uid=request.session.get('userid')
        pid = request.POST['it']
        pidpic = request.POST['it']
        orderdtls = Order.objects.all().filter(Product_Id=pid)
        products=Product.objects.all().filter(Item_id=pidpic)
        img=''
        for a in products:
            img=a.Item_Image
        return render(request,'OrderDetail.html',{'orderdtls':orderdtls,'img':img,'pid':pid})
def updateItem(request):
    if request.session['userid']:
        pid = request.POST['it']
        itms = Product.objects.all().filter(Item_id=pid)
        return render(request,'updateItem.html',{'itms':itms})
    else:
        return redirect(request,'login.html')

def update(request):
    if request.session['userid']:
        pid=request.POST['it']
        pnm=request.POST['pnm']
        prd = Product.objects.all().filter(Item_id=pid)
        for i in prd:
            img=i.Item_Image
            img1=i.Extra_Images1
            img2=i.Extra_Images2
        ItemName = request.POST['itemName']
        Author = request.POST['authorName']
        ItemType = request.POST['itemType']
        Price = request.POST['itemPrice']
        Quantity = request.POST['quantity']
        SellerName = request.POST['sellerName']
        SellerAddress = request.POST['sellerAddress']
        Description = request.POST['description']
        # if des==Descripte:
        #     Description=des
        # else:
        #     Description = Descripte.split(".")
        Specification = request.POST['specifications']
        # if spe==Specificate:
        #     Specification=spe
        # else:
        #     Specification = Specificate.split(".")
        # ItemDisplayImage=request.POST['MyFile1']
        # ItemExtraImage2=request.POST['MyFile2']
        # ItemExtraImage3=request.POST['MyFile3']
        try:
            ItemDisplayImage = request.FILES['MyFile1']
            imgsnm = ItemDisplayImage.name
            fs = FileSystemStorage()
            fs.save(imgsnm, ItemDisplayImage)
            # if ItemDisplayImage == '' or None:
            #     ItemDisplayImage = 'fav.png'
        except:
            ItemDisplayImage = img
        try:
            ItemExtraImage2 = request.FILES['MyFile2']
            imgsnm1=ItemExtraImage2.name
            fs=FileSystemStorage()
            fs.save(imgsnm1,ItemExtraImage2)
            # if ItemExtraImage2 == '' or None:
            #     ItemExtraImage2 = 'fav.png'
        except:
            ItemExtraImage2 = img1
        try:
            ItemExtraImage3 = request.FILES['MyFile3']
            imgsnm2 = ItemExtraImage3.name
            fs = FileSystemStorage()
            fs.save(imgsnm2, ItemExtraImage3)
            # if ItemExtraImage3 == '' or None:
            #     ItemExtraImage3 = 'fav.png'
        except:
            ItemExtraImage3 = img2

        PostDate = datetime.datetime.now().strftime('%d/%m/%Y')
        UpdaterId = request.session['userid']
        itemId = Price + PostDate[0:2] + UpdaterId[0:10]

        try:
            v = Product.objects.get(Item_id=pid)
            if v is not None:
                message="Details Updated Sucessfully"
                # Product.objects.all().filter(Item_id=pid,Item_name=pnm).update(Price=Price, Quantity=Quantity)
                Product.objects.all().filter(Item_id=pid).update(Item_name=ItemName,Author=Author,Item_type=ItemType,Price=Price,Quantity=Quantity,Sellars_Name=SellerName,Sellars_Shop_Address=SellerAddress,Item_Image=ItemDisplayImage,Extra_Images1=ItemExtraImage2,Extra_Images2=ItemExtraImage3,Descriptions=Description,Specifications=Specification,Updater_Admin_Id=UpdaterId,Post_Date=PostDate,Item_id=itemId)
                return render(request, 'updateItem.html',{'message':message})
        except ObjectDoesNotExist:
            return render(request, 'updateItem.html', {'message': 'Something is wrong'})
    else:
        return render(request,'adminhome.html')

def Logout(request):
    if request.session['userid']:
        return render(request,'index.html')
    else:
        return redirect(request,'login.html')

def ad_reg(request):
    if request.method == 'POST': # and request.FILES['MyFile']:
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        DOB = request.POST['DateOfBirth']  # To understand the coading just please read this line
        Gender = request.POST['Gender']
        FatherName = request.POST['FatherName']
        Email = request.POST['Email']
        Password = request.POST['Password']
        PhoneNumber = request.POST['PhoneNumber']
        Address = request.POST['Address']
        try:
            UserImage = request.FILES['MyFiles']
            if UserImage == '' or None:
                if Gender == 'Male':
                    UsrImg = 'mUser.png'
                elif Gender == 'Female':
                    UsrImg = 'gUser.png'
                else:
                    UsrImg = 'sign-up.png'
            else:
                UsrImg=UserImage
        except:
            if UserImage == '' or None:
                if Gender == 'Male':
                    UsrImg = 'mUser.png'
                elif Gender == 'Female':
                    UsrImg = 'gUser.png'
                else:
                    UsrImg = 'sign-up.png'
            # else:
            #     UserImage = 'sign-up.png'
        SecurityQuestion = request.POST['SecurityQuestion']
        SecurityAnswer = request.POST['SecurityAnswer']
        UserDetails = Admins(User_Id=FirstName[0:3]+PhoneNumber[0:10]+Gender[0:1],First_Name=FirstName,Last_Name=LastName,Date_of_Birth=DOB,Gender=Gender,Father_Name=FatherName,Address=Address,Email_id=Email,Password=Password,Phone_Number=PhoneNumber,Security_Question=SecurityQuestion,Security_Answer=SecurityAnswer,User_Image=UsrImg)
        UserDetails.save()
        return render(request,'login.html',{'message':'Registration Sucessfull'})
    return render(request,'ad_reg.html')


def deleteItem(request):
    if request.session['userid']:
        pid=request.POST['idval']
        itm=Product.objects.filter(Item_id=pid)
        itm.delete()
        return redirect('adminhome')
    else:
        return render(request,'login.html')


