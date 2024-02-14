from django.contrib import admin
from .models import New_User,P_Details,Return
# Register your models here.

class Admin(admin.ModelAdmin):
    list_display=('email','name','phone','reg_no')

admin.site.register(New_User,Admin)

class Recipient(admin.ModelAdmin):
    list_display=('rec_id','rec_email','rec_name','rec_phone','reg_date','rec_company')

admin.site.register(P_Details,Recipient)

class rReturn(admin.ModelAdmin):
    list_display=('p_id','p_otp','p_name','p_date','p_ser')




