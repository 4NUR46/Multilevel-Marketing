from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^login',views.login,name='login'),
    url(r'^log',views.log,name='log'),
    #url(r'^catagory',views.catagory,name='catagory'),
    url(r'^register',views.register,name='register'),
    url(r'^itemDetails',views.itemDetails,name='itemDetails'),
    url(r'^Contact', views.Contact, name='Contact'),
    url(r'^About',views.About,name='About'),
    url(r'^nav',views.nav,name='nav'),
    url(r'^Login',views.Adds,name='Adds'),
    url(r'^forget',views.forget,name='forget'),
    url(r'^designDemo',views.designDemo,name='designDemo'),
    url(r'Ad_Itm',views.Ad_Itm,name='Ad_Itm'),

    # url(r'^contact', views.contact, name='contact'),
    # url(r'^about', views.about, name='about'),
    url(r'^products', views.products, name='products'),
    url(r'^books', views.books, name='books'),
    url(r'^checkout', views.checkout, name='checkout'),
    url(r'^search', views.search, name='search'),
    url(r'^payment', views.payment, name='payment'),
    url(r'^oneplus', views.oneplus, name='oneplus'),
    url(r'^k20pro', views.k20pro, name='k20pro'),
    url(r'^k20', views.k20, name='k20'),
    url(r'^note8', views.note8, name='note8'),
    url(r'^redmi8', views.redmi8, name='redmi8'),
    url(r'^vivou20', views.vivou20, name='vivou20'),
    url(r'^pocox2', views.pocox2, name='pocox2'),
    url(r'^onelite', views.onelite, name='onelite'),
    url(r'^motorazer', views.motorazer, name='motorazer'),
    url(r'^asusbook', views.asusbook, name='asusbook'),
    url(r'^hppav', views.hppav, name='hppav'),



]
