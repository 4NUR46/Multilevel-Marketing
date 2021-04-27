from django.shortcuts import render,redirect,reverse
from . models import Register
from adminzone.models import Product,Admins
from userzone.models import Cart
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
# Create your views here.

def index(request):
    # item=Product.objects.all().filter(Item_type='New')
    # slid=Product.objects.all().filter(Item_type='Slider')
    # return render(request,'index.html',{'item':item,'slider':slid})
    item = Product.objects.all()
    # slid = Product.objects.all().filter(Item_type='Slider')
    return render(request, 'index.html', {'item': item})

def login(request):
    return render(request,'login.html')
#
# def log(request):
#     return render(request,'login.html')

def log(request):
    userid = request.POST['number']
    password = request.POST['pass']
    try:
        v = Register.objects.get(Phone_Number=userid, Password=password)
        if v is not None:
            request.session['userid'] = userid
            return redirect(reverse('home'))

    except ObjectDoesNotExist:
        try:
            a = Admins.objects.get(Phone_Number=userid, Password=password)
            if a is not None:
                request.session['userid'] = userid
                return redirect(reverse('adminhome'))

        except ObjectDoesNotExist:
            return render(request, 'login.html',{'message':'Something is wrong'})
    return render(request,'login.html')


def itemDetails(request):
    return render(request,'itemDetails.html')
#
# def catagory(request):
#     return render(request,'catagory.html')

def register(request):
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
        # UserImage = request.FILES['MyFile']
        try:
            UserImage = request.FILES['MyFile1']
            if UserImage == '' or None:
                if Gender == 'Male':
                    UserImage = 'mUser.png'
                elif Gender == 'Female':
                    UserImage = 'gUser.png'
        except:
            UserImage = 'sign-up.png'

        # if UserImage == None or ' ':
        #     if Gender == 'Male':
        #         UserImage = 'mUser.png'
        #     elif Gender == 'Female':
        #         UserImage = 'gUser.png'
        #     else:
        #         UserImage = 'sign-up.png'
        SecurityQuestion = request.POST['SecurityQuestion']
        SecurityAnswer = request.POST['SecurityAnswer']
        if Register.objects.filter(Phone_Number=PhoneNumber).exists():
            msg='Phone number already Registered'
            return render(request,'register.html',{'message':msg})
        else:
            UserDetails = Register(User_Id=FirstName[0:3]+PhoneNumber[0:10]+Gender[0:1],First_Name=FirstName,Last_Name=LastName,Date_of_Birth=DOB,Gender=Gender,Father_Name=FatherName,Address=Address,Email_id=Email,Password=Password,Phone_Number=PhoneNumber,Security_Question=SecurityQuestion,Security_Answer=SecurityAnswer,User_Image=UserImage)
            UserDetails.save()
            return render(request,'login.html',{'message':'Registration Sucessfull'})
    return render(request,'register.html')

def About(request):
    return render(request,'About.html')

def Contact(request):
    return render(request,'contact.html')

def nav(request):
    return render(request,'nav.html')

def Adds(request):
    return render(request,'login.html')


def forget(request):
    if request.method == 'POST':
        userid = request.POST['number']
        password = request.POST['pass']
        que = request.POST['SecurityQuestion']
        ans = request.POST['SecurityAnswer']
        try:
            v = Register.objects.get(Phone_Number=userid,Security_Question=que, Security_Answer=ans)
            if v is not None:
                Register.objects.filter(Phone_Number=userid).update(Password=password)
                return render(request,'login.html',{'message':'Password Changed'})
        except ObjectDoesNotExist:
            return render(request, 'login.html',{'message':'Something is wrong'})
    else:
        return render(request,'ForgetPass.html')


def designDemo(request):
    return render(request,'designDemo.html')
#
# def about(request):
#     return render(request,'about.html')

def products(request):
    return render(request,'products.html')

def books(request):
    return render(request,'books.html')

def checkout(request):
    return render(request,'checkout.html')


def search(request):
    return render(request,'search.html')

def login(request):
    return render(request,'login.html')

def payment(request):
    return render(request,'payment.html')

def oneplus(request):
    return render(request,'oneplus.html')

def k20pro(request):
    return render(request,'k20pro.html')

def k20(request):
    return render(request,'k20.html')

def note8(request):
    return render(request,'note8.html')

def redmi8(request):
    return render(request,'redmi8.html')

def pocox2(request):
    return render(request,'pocox2.html')

def vivou20(request):
    return render(request,'vivou20.html')

def onelite(request):
    return render(request,'onelite.html')

def motorazer(request):
    return render(request,'motorazer.html')

def asusbook(request):
    return render(request,'asusbook.html')


def hppav(request):
    return render(request,'hppav.html')


# Add item in cart button Action

def Ad_Itm(request):
        return render(request,'login.html')

