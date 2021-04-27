from django.shortcuts import render,redirect,reverse
from adminzone.models import Product
from . models import Cart,Order
import datetime
from generalzone.models import Register
# Create your views here.

########## Home Page Access #########
def home(request):
    if request.session['userid']:
        ############ Get Items From Database and store in a variable ##################
        item=Product.objects.all()
        message='Welcome'
        ######### Return the value on the page home #########
        return render(request,'home.html',{'item':item,'message':message})
    else:
        return render(request,'login.html')

########### About Page Access ###########
def about(request):
    if request.session['userid']:
        return render(request,'about.html')
    else:
        return render(request,'login.html')


# def cart(request):
#     if request.session['userid']:
#         uid = request.session.get('userid')
#         addva = Cart.objects.all().filter(User_id=uid)
#         for i in addva:
#             a = i.Cart_Item
#         b = 0
#         k = 0
#         for j in a:
#             if j==",":
#                 continue
#             else:
#                 b=b*10+j
#                 k=k+1
#             if k==10:
#                 k=0
#                 list=list.append(b)
#         for c in list:
#             ad = Product.objects.all().filter(Item_id=c)
#             return render(request, 'cart.html',{'a':ad})
#         return render(request,'cart.html')
#     else:
#         return render(request,'login.html')


########### Access Cart Page with the details of user to get number of cart items ##########
def cart(request):
    if request.session['userid']:
        uid = request.session.get('userid')
        addva = Cart.objects.all().filter(User_id=uid)
        # user_email= Register.objects.all().filter(User_Id=uid)
        # email=''
        # for i in user_email:
        #     email=i.Email_id
        # orders=Order.objects.all().filter(User_Email=email)
        orders=Order.objects.all().filter(User_Number=uid)
        return render(request,'cart.html',{'adv':addva,'orders':orders,'uid':uid})
    else:
        return render(request,'login.html')

############## Catagory of Items ##################
def Category(request):
    if request.session['userid']:
        return render(request,'Category.html')
    else:
        return render(request,'login.html')

############# Details of Items ################
def ItemDetails(request):
    # if request.session['userid']:
        pid = request.POST['it']
        #uid=request.session.get('userid')
        pids = Cart.objects.filter(id=pid)
        b='None'
        try:
            for a in pids:
                b = a.Product_id
        except:
            b=='None'
        if b=='None':
            pob=Product.objects.all().filter(Item_id=pid)
        else:
            pob = Product.objects.all().filter(Item_id=b)
        return render(request,'ItemDetails.html',{'dtl':pob})
    # else:
    #     return render(request,'login.html')

#
# def ItemDetails(request):
#     if request.session['userid']:
#         return render(request,'ItemDetails.html')
#     else:
#         return render(request,'login.html')


############ User LogOut ##############
def Logout(request):
    if request.session['userid']:
        return render(request,'index.html')
    else:
        return render(request, 'login.html')

############## User Details ###############
def userProfile(request):
    if request.session['userid']:
        uid = request.session.get('userid')
        user=Register.objects.all().filter(Phone_Number=uid)
        return render(request,'userProfile.html',{'user':user,'uid':uid})
    else:
        return render(request,'login.html')

########### External Nevigation Bar #############
def navigation(request):
    if request.session['userid']:
        return render(request,'navigation.html')
    else:
        return render(request,'login.html')

# def Add(request):
#     if request.session['userid']:
#         return render(request,'home.html')
#     else:
#         return render(request,'login.html')

# def Add_Item(request):
#     if request.session['userid']:
#         uid=request.session.get('userid')
#         it = request.POST['it']
#         addv=Register.objects.all().filter(Phone_Number=uid)
#         for i in addv:
#             a=i.Cart_Item
#         addva=a
#         addval=str(it)+","+str(addva)
#         Register.objects.filter(Phone_Number=uid).update(Cart_Item=addval)
#         return render(request,'home.html',{'message':'item added'})
#     else:
#         return render(request,'login.html')
#
# def Add_Item(request):
#     if request.session['userid']:
#         return render(request, 'home.html')
#     else:
#         return render(request,'login.html')

############## Manage Item adding in cart ################
def Add_Item(request):
    try:
        if request.session['userid']:
            pid = request.POST['it']
            uid=request.session.get('userid')
            bb=cc=dd=ee=ff=gg=""
            pob=Product.objects.all().filter(Item_id=pid)
            for a in pob:
                bb=a.Item_name
            b=bb
            for a in pob:
                cc=a.Price
            c=cc
            for a in pob:
                dd=a.Quantity
            d=dd
            for a in pob:
                ee=a.Descriptions
            e=ee
            for a in pob:
                ff=a.Sellars_Name
            f=ff
            for a in pob:
                gg=a.Item_Image
            g=gg
            dat=datetime.datetime.now().strftime('%d/%m/%Y')
            if Cart.objects.filter(Product_id=pid).exists():
                message='Item already added in cart'
            else:
                ca=Cart(User_id=uid, Product_id=pid, Product_Name=b, Product_Price=c, Product_Quantity=d, Product_Details=e, Product_Add_Date=dat , Product_Seller=f, Product_image=g)
                ca.save()
                message='Item added Sucessfully'
            return redirect('home.html',{'message':message})
            #return render(request,'home.html',{'message': 'Item added'})
        else:
             return render(request,'login.html')
    except:
        return render(request, 'login.html')


############### Delete Items from Cart ###################
def deletecart(request):
    if request.session['userid']:
        if request.method == 'POST':
            idval=request.POST['idval']
            cdel=Cart.objects.filter(id=idval)
            cdel.delete()
            #return render(request,'cart.html')
            return redirect('cart.html',{'idval':idval})
    else:
        return render(request,'home.html')


############### Cancel Order ##################
def deleteOredr(request):
    if request.session['userid']:
        if request.method == 'POST':
            idval=request.POST['idval']
            cdel=Order.objects.filter(Product_Id=idval)
            cdel.delete()
            # return render(request,'cart.html',{'idval':idval,'cdel':cdel})
            return redirect('cart.html')
    else:
        return render(request,'home.html')

############## Buy Item ################
def Buy(request):
    if request.session['userid']:
        pid = request.POST['it']
        uid = request.session.get('userid')
        b=0
        nbr=bb=cc=dd=ee=ff=un=ua=productid=img=''
        pids=Cart.objects.filter(id=pid)      # Product_id=pid
        for a in pids:
            b=a.Product_id
        #pob = Product.objects.all().filter(Item_id=b)
        user = Register.objects.all().filter(Phone_Number=uid)
        for a in user:
            u=a.First_Name
            n=a.Last_Name
            un=u+' '+n
        em=''
        for a in user:
            em=a.Email_id
        for a in user:
            ua=a.Address
        for a in user:
            nbr=a.Phone_Number

        pob = Product.objects.all().filter(Item_id=b)
        for a in pob:
            bb = a.Item_name
        for a in pob:
            productid=a.Item_id
        b = bb
        for a in pob:
            cc = a.Price
        c = cc
        for a in pob:
            dd = a.Quantity
        d = dd
        for a in pob:
            ee = a.Descriptions
        e = ee
        for a in pob:
            ff = a.Sellars_Name
        f = ff
        for a in pob:
            img=a.Item_Image

        dt = datetime.datetime.now().strftime('%d/%m/%Y')
        pyst='Cash on Delivery'

        if Order.objects.filter(User_Number=pid,User_Email=em).exists():
            message = 'Item already added in order'
        else:
            # ca = Order(User_Name=un, Product_Id=pid, Product_Name=b, Product_Price=c, Product_Quantity=d,Product_Details=e, User_Email=em, Product_Seller=f, User_Number=nbr,Product_Order_Date=dt,User_Address=ua,Payment_Status=pyst)
            # ca.save()
            # Decrease the value of quantity from stock when product be buyed
            qty=Product.objects.all().filter(Item_id=pid)
            qtyn=0
            for a in qty:
                qtyn=a.Quantity
            qnty=int(qtyn)-1
            Product.objects.all().filter(Item_id=pid).update(Quantity=qnty)

            # Delete Item From Cart After Order.
            cdel = Cart.objects.filter(id=pid)
            cdel.delete()

            ca = Order(User_Name=un, Product_Id=productid, Product_Name=b, Product_Price=c, Product_Quantity=d,
                       Product_Details=e, User_Email=em, Product_Seller=f, User_Number=nbr, Product_Order_Date=dt,
                       User_Address=ua, Payment_Status=pyst)
            ca.save()
            message = 'Item Ordered'
        # products = Product.objects.all().filter(Item_id=pid)
        # img = ''
        # for a in products:
        #     img = a.Item_Image
        pobs = Order.objects.all().filter(Product_Id=productid,User_Email=em)
        #return render(request, 'Buy.html', {'message':message,'dtl': pob,'user': user})
        return render(request, 'Buy.html', {'message':message,'dtl': pobs,'img':img})
    else:
        return render(request, 'login.html')


############## Divide Items in catagory #################3
def CatagoryItem(request):
    if request.session['userid']:
        itemid = request.POST['itmtyp']
        msg = itemid
        if 'Books' == msg :
            return render(request,'books.html')
        else:
            item = Product.objects.filter(Item_type=itemid)
            return render(request, 'CatagoryItem.html',{'itemtypes': item, 'message': msg})
    else:
        return render(request,'login.html')


