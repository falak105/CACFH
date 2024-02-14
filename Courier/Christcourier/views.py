from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from io import BytesIO
import base64
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from Christcourier.models import New_User, P_Details,Return
from django.db.models import Count

def index(request):
    if request.method == 'POST':
        username = request.POST.get('Email')
        pass1 = request.POST.get('pass')
        print(username,pass1)
        
        # Check if password matches for a specific user
        user = authenticate(request, username=username, password=pass1)
        print(user)
        
        if user is not None:
            # Check user role and redirect accordingly
            if user.is_superuser:
                login(request, user)
                return redirect('admin_db')
            elif user.is_staff:
                login(request,user)
                return redirect('sdashboard')
            else:
                login(request, user)
                return redirect('dashboard')
        else:
            # Handle invalid credentials
            return render(request, "user/index.html", {'error_message': 'Invalid credentials'})

    return render(request, "user/index.html")

def service(request):
    return render(request,"user/service.html")

def about(request):  
    return render(request,"user/about.html")

def contact(request):
    return render(request,"user/contact.html")

def reci(request):
    return render(request,"user/dashboard.html")

def register(request):
    if request.method == 'POST':
        usertype = request.POST.get('choice')
        Email = request.POST.get('Email')
        Name = request.POST.get('Name')
        Phone_Number = request.POST.get('Phone_Number')
        reg_Number = request.POST.get('Reg_No')
        pass1 = request.POST.get('pass')

        if usertype == 'staff':
            my_user = User.objects.create_user(username=Email,email=Email,password=pass1,first_name=Name,is_staff=True)
            my_user.save()
        else:
            my_user1 = User.objects.create_user(username=Email,email=Email,password=pass1,first_name=Name)
            my_user1.save()

        Regs=New_User(email=Email,
        name=Name,
        phone=Phone_Number,
        reg_no=reg_Number)
        Regs.save()
        return redirect('index')    
    return render(request,"user/reg.html")

def receive(request):  
    if request.method=="POST":
        Id = request.POST.get('parcelId')
        email = request.POST.get('recEmail')
        Recname = request.POST.get('recName')
        Recphone = request.POST.get('recContact')  # Assuming recContact is the correct name
        Deldate = request.POST.get('delDate')
        Company = request.POST.get('company')
        
        add=P_Details(
            rec_id=Id,
            rec_email=email,
            rec_name=Recname,
            rec_phone=Recphone,
            reg_date=Deldate,
            rec_company=Company
        )
        add.save()
        # data = add.save()
        # if data:
    #         print("save")
    #     else:
    #         print("no") 
    # else:
    #     print("Not in Cond")           

    return render(request,"user/receive.html")

# def dashboard(request):
#     u_email = request.user.username
    
#     # Fetch data from P_Details model
#     p_details_res = P_Details.objects.filter(rec_email=u_email)
#     p_details_data = p_details_res[0] if p_details_res.exists() else None
    
    # Fetch data from Return model
    # return_res = Return.objects.all()  # Assuming p_id is related to user email
    # return_data = return_res[0] if return_res.exists() else None
    
    # return render(request, "user/dashboard.html", {'p_details_data': p_details_data, 'return_data': return_data})

# def dashboard(request):
#     u_email=request.user.username
#     res=P_Details.objects.filter(rec_email=u_email)
#     data=res[0]

def dashboard(request):
    # Check if the user is authenticated
    # if request.user.is_authenticated:
    #     # Assuming `rec_email` in `P_Details` corresponds to the logged-in user's email
    #     u_email = request.user.email
    #     # Fetch P_Details objects related to the logged-in user's email
    #     res = P_Details.objects.filter(rec_email=u_email)
    #     # data=res[0]
    #     # print(data)
    #     # Check if any results were returned
    #     if res.exists():
    #         # If results exist, take the first one (assuming only one result is expected)
    #         data = res.first()
    #         return render(request, "user/dashboard.html", {'data': data})
    #     else:
    #         # Handle the case where no matching records are found
    #         return render(request, "user/index.html")
    # else:
    #     # Handle the case where the user is not authenticated
    #     return render(request, "user/not_authenticated.html")
    
    return render(request,"user/dashboard.html")

def sdashboard(request):
    return render(request,"staff/sdashboard.html")

def pstatus(request):
    return render(request,"staff/pstatus.html")

def admin_db(request):
    return render(request,"admin/admin_db.html")
def forgot_password(request):
    return render(request,"user/forgot_password.html")
    if request.method == "POST":
        pId = request.POST.get('pId')
        Rotp = request.POST.get('rOtp')
        Rname = request.POST.get('rName')
        Rdate = request.POST.get('rDate')  # Assuming recContact is the correct name
        Ser = request.POST.get('company')
        print(pId,Rotp,Rname,Rdate)
        ad = Return.objects.create(p_id=pId,p_otp=Rotp,p_name=Rname,p_date=Rdate,p_ser=Ser,)
        ad.save()
        return redirect('dashboard')   
    else:
        return render(request,"user/Return.html")

def plot_graph(request):
    # Graph 1: Bar graph between Names and Company
    data1 = P_Details.objects.values('rec_company').annotate(count=Count('rec_name'))
    companies = [entry['rec_company'] for entry in data1]
    counts = [entry['count'] for entry in data1]

    plt.figure(figsize=(8, 4))
    plt.bar(companies, counts)
    plt.xlabel('Companies')
    plt.ylabel('Number of Names')
    plt.title('Graph between Names and Company')

    buffer1 = BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    plt.clf()
    image_base64_1 = base64.b64encode(buffer1.read()).decode('utf-8')

    # Graph 2: Scatter plot between Registration Dates and Company
    data2 = P_Details.objects.values('reg_date', 'rec_company')
    dates = [entry['reg_date'] for entry in data2]
    companies_2 = [entry['rec_company'] for entry in data2]

    plt.figure(figsize=(8, 4))
    plt.scatter(dates, companies_2)
    plt.title('Registration Date vs Company')
    plt.xlabel('Registration Date')
    plt.ylabel('Company')
    plt.xticks(rotation=45)

    buffer2 = BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    plt.clf()
    image_base64_2 = base64.b64encode(buffer2.read()).decode('utf-8')

    # Graph 3: Pie chart of Company counts
    data3 = P_Details.objects.values('rec_company').annotate(count=Count('rec_name'))

    companies_pie = [entry['rec_company'] for entry in data3]
    counts_pie = [entry['count'] for entry in data3]

    plt.figure(figsize=(8, 8))
    plt.pie(counts_pie, labels=companies_pie, autopct='%1.1f%%', startangle=140)
    plt.title('Pie Chart of Company Counts')

    buffer3 = BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    plt.clf()
    image_base64_3 = base64.b64encode(buffer3.read()).decode('utf-8')

    return render(request, "admin/dash.html", {'image_base64_1': image_base64_1, 'image_base64_2': image_base64_2, 'image_base64_3': image_base64_3})

def retdet(request):
    ret=Return.objects.all()
    return render(request,"admin/retdet.html",{'ret':ret})
  
def profile(request):
    u_email = request.user.username
    res = New_User.objects.filter(email=u_email)
    data = res.first()  # Retrieve the first object or None if queryset is empty
    return render(request, 'user/profile.html', {'data': data})

