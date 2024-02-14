from django.urls import path
from Christcourire import views


urlpatterns = [
    path  ('',index,name='index'),
    path  ('service',service,name='service'),
    path  ('about',about,name='about'), 
    path  ('contact',contact,name='contact'),
    path  ('reci',reci,name='reci'),
    path  ('reg',reg,name='reg'),
    path  ('dashboard',dashboard,name='dashboard'),
    path  ('staff',staff,name='staff'),
    path  ('staffreg',staffreg,name='staffreg'),
    
]
