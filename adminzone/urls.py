from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.adminhome,name='adminhome'),
    url(r'^adminhome',views.adminhome,name='adminhome'),
    url(r'^adminProfile',views.adminProfile,name='adminProfile'),
    url(r'^AddItem',views.AddItem,name='AddItem'),
    url(r'^notifications',views.notifications,name='notifications'),
    url(r'^updateItem',views.updateItem,name='updateItem'),
    url(r'^$',views.Logout,name='Logout'),
    url(r'ad_reg',views.ad_reg,name='ad_reg'),
    url(r'^update',views.update,name='update'),
    url(r'deleteItem',views.deleteItem,name='deleteItem'),
    url(r'OrderDetails',views.OrderDetails,name='OrderDetails'),


]