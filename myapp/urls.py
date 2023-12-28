from django.urls import path
from . import views

urlpatterns = [
    # path('',views.base,name='base'),
    path('',views.adminlogin,name='adminlogin'),
    path('adminlogins/',views.adminlogins,name='adminlogins'),

    
    path('welcome/',views.welcome,name='welcome'),
    path('signup/',views.signup,name='signup'),
    path('userlogin/',views.userlogin,name='userlogin'),
    
    path('adminpannel/',views.adminpannel,name='adminpannel'),
    path('notice/',views.notice,name='notice'),
    path('adminevent/',views.adminevent,name='adminevent'),
    path('adminnotice/',views.adminnotice,name='adminnotice'),
    path('event/',views.event,name='event'),
    path('addevent/',views.addevent,name='addevent'),
    path('addnotice/',views.addnotice,name='addnotice'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
]
