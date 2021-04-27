from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    #url(r'^$',views.home,name='home'),
    url(r'^home',views.home,name='home'),
    url(r'^about',views.about,name='about'),
    url(r'^cart',views.cart,name='cart'),
    url(r'^ItemDetails',views.ItemDetails,name='ItemDetails'),
    # url(r'^ItemDetls',views.ItemDetls,name='ItemDetls'),
    url(r'^userProfile',views.userProfile,name='userProfile'),
    #url(r'^Logout',views.Logout,name='Logout'),
    url(r'^$',views.Logout,name='Logout'),
    url(r'^navigation',views.navigation,name='navigation'),
    #url(r'^home',views.home,name='Add_it'),
    url(r'^Add_Item',views.Add_Item,name='Add_Item'),
    url(r'^Category',views.Category,name='Category'),
    url(r'^deletecart',views.deletecart,name='deletecart'),
    url(r'^deleteOredr',views.deleteOredr,name='deleteOredr'),
    url(r'^Buy',views.Buy,name='Buy'),
    url(r'^CatagoryItem',views.CatagoryItem,name='CatagoryItem'),



]
