from django.urls import path
from Christcourier.views import index,service,about,reci,register,dashboard,contact,sdashboard,receive,pstatus,admin_db,forgot_password

urlpatterns = [
    path  ('',index,name='index'),
    path  ('service',service,name='service'),
    path  ('about',about,name='about'), 
    path  ('contact',contact,name='contact'),
    path  ('reci',reci,name='reci'),
    path  ('reg',register,name='reg'),
    path  ('dashboard',dashboard,name='dashboard'),
    path  ('sdashboard',sdashboard,name='sdashboard'),
    path  ('receive',receive,name='receive'),
    path  ('pstatus',pstatus,name='pstatus'),
    path ('admin_db',admin_db,name='admin_db'),
    path('forgot_password',forgot_password,name='forgot_password'),
]  

  
