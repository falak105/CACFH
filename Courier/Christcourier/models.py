from django.db import models
# Create your models here.
Company = (
    ('amazon','amazon'),
    ('flipkart','flipkart'),
    ('myntra','myntra'),
    ('nykaa','nykaa'),
    ('meesho','meesho'),
    ('others','others'),
)
Service = (
    ('amazon','amazon'),
    ('flipkart','flipkart'),
    ('myntra','myntra'),
    ('nykaa','nykaa'),
    ('meesho','meesho'),
    ('others','others'),
)
Login = (
    ('user','user'),
    ('staff','staff'),
)
class New_User(models.Model):
    email=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    reg_no=models.CharField(max_length=200)


class P_Details(models.Model):
    rec_id = models.CharField(max_length=50)
    rec_email = models.CharField(max_length=200)
    rec_name = models.CharField(max_length=200)
    rec_phone = models.CharField(max_length=200)
    reg_date = models.DateField()
    rec_company = models.CharField(max_length=200, choices=Company)

class Return(models.Model):
    p_id = models.CharField(max_length=200,null=True)
    p_otp = models.CharField(max_length=200,null=True)
    p_name = models.CharField(max_length=200)
    p_date = models.DateField()
    p_ser = models.CharField(max_length=200,choices=Service)
    

  
