from cmd import IDENTCHARS
from configparser import SectionProxy
import email
import traceback
from unicodedata import name
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from django.conf import settings

from .models import *
from datetime import datetime, date, time, timedelta
from django.conf import settings
from django.http import HttpResponse
import json
from datetime import datetime
from calendar import monthrange
import ast
import csv
from django.forms.models import model_to_dict
from django.http import JsonResponse

from .models import User
import time
import datetime as dt
from django.contrib.auth import logout
from django.shortcuts import redirect


from django.conf import settings
from django.core.mail import send_mail


def last_day_of_month(date_value):
    return date_value.replace(day = monthrange(date_value.year, date_value.month)[1])



@csrf_exempt
def test(request):
    var= request.POST.get("name")
    return JsonResponse({'var': var})

def login(request):
    return render(request, 'login.html')


@csrf_exempt
def login_check(request):
	email=request.POST.get('email')
	password=request.POST.get('password')

	if not Admin_login.objects.filter(admin_email=email,admin_password=password).exists():
		return HttpResponse("error")
	else:
		obj= Admin_login.objects.get(admin_email=email,admin_password=password)
		request.session['user_id'] = str(obj.id)
		#request.session['user_email'] = str(obj.email)
		return HttpResponse("success")



""" @csrf_exempt
def login_check_1(request):
    #username = request.POST.get('username')
    email=request.POST.get('email')
    password = request.POST.get('password')

    if not User.objects.filter(email=email, password=password).exists():
        return HttpResponse("error")
    else:
        obj = User.objects.get(email=email, password=password)
        request.session['user_id'] = str(obj.id)
        request.session['user_name'] = str(obj.email)
        return HttpResponse("success") """


def logout(request):
    print(request.session['user_id'])
    del request.session['user_id']
    return redirect('/') 


@csrf_exempt
def dashboard(request):
    session_id = request.session.get('user_id')
    obj = Student.objects.all()
    print(session_id)
    context = {
        'obj':obj
    }

    return render(request, 'dashboard.html', context)


@csrf_exempt
def employee_view(request):
    session_id = request.session.get('user_id')
    login_user = request.session.get('user_name')
    print(login_user)
    print(session_id)
    obj = User.objects.all().order_by("-id")
    list = []
    dict = {}
    for i in obj:
        dict["id"] = i.id
        dict["name"] = i.name
        dict["email"] = i.email
        dict["designation"] = i.designation
        dict["doj"] = i.doj
        list.append(dict)
        dict = {}
         
    today = date.today()
    given_date = datetime.today().date() 
    end_date =last_day_of_month(given_date)
	
    given_date = datetime.today().date()
    first_day_of_month = given_date - timedelta(days = int(given_date.strftime("%d"))-1)

    if session_id:
        
        return render(request, 'employee_view.html', {"list": list, "start_day":first_day_of_month, "end_date":end_date, })
    else:
        return redirect("/")
    
def add_employee(request):
    return render(request, 'add.html' )   

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        designation = request.POST.get('designation')

        date= datetime.now()
        
        
        if User.objects.filter(email=email).exists():
            print("check")
            return HttpResponse('error')

        else:
            User.objects.create(
                name=name,
                email=email,
                designation=designation,
                doj=date,
            )
        return HttpResponse('success')
    
    

def edit_details(request, id):
    obj= User.objects.get(id=id)
    return render(request, 'edit.html', {"user_id": id, "obj":obj})
    
@csrf_exempt
def create_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        user_id= request.POST.get('user_id')
        designation = request.POST.get('designation')
        doj = request.POST.get('doj')
        

        obj = User.objects.get(id= user_id)
        obj.name = name
        obj.email = email
        obj.designation = designation
        obj.doj = doj
        obj.save()
        return HttpResponse('success')  
    

    
@csrf_exempt   
def Delete_employee(request):
    id = request.POST.get("id")
    obj = User.objects.get(id=id).delete()
    return HttpResponse("success")  

@csrf_exempt
def search_employee_report(request):
    start_date = request.POST.get("start_date")
    end_date = request.POST.get("end_date")
    
    if User.objects.filter(doj__gte= start_date, doj__lte = end_date).exists():
        obj = User.objects.filter(doj__gte = start_date, doj__lte = end_date).order_by("-doj")
        rendered= render_to_string('search_employee_report.html', {'obj':obj, 'start_date':start_date, 'end_date':end_date})
        return HttpResponse(rendered)
    else:
        return HttpResponse("error")




    
@csrf_exempt
def book_master(request):
    session_id = request.session.get('user_id')
    print(session_id)
    
    obj = Book_Master.objects.all().order_by("-id")
    list = []
    dict = {}
    for i in obj:
     dict["id"] = i.id
     dict["book_name"] = i.book_name
     dict["author"] = i.author
     dict["dop"] = i.dop
     dict["category"] = i.category
     dict["condition"] = i.condition
     dict["price"] = i.price
     list.append(dict)
     dict = {}
     
    today = date.today()
    given_date = datetime.today().date() 
    end_date =last_day_of_month(given_date)
	
    given_date = datetime.today().date()
    first_day_of_month = given_date - timedelta(days = int(given_date.strftime("%d"))-1)
     
    
    if session_id:
        
        return render(request, 'book_master.html', {"list": list, "start_day":first_day_of_month, "end_date":end_date, })
    else:
        return redirect("/")

def add_book(request):
    obj = New_Category.objects.all().order_by("-id")
    return render(request, 'add_book.html', {"obj":obj})



@csrf_exempt
def create_book(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        dop = request.POST.get('dop')
        category = request.POST.get('category')
        condition = request.POST.get('condition')
        price = request.POST.get('price')
        date=datetime.now()
        print(date)
        if Book_Master.objects.filter(book_name=book_name, created_date= date).exists():
            print("check")
            return HttpResponse('error')

        else:
            Book_Master.objects.create(
                book_name=book_name,
                author=author,
                dop=dop,
                category=category,
                condition=condition,
                price=price,
                created_date= date,
            )
        return HttpResponse('success')
    
def edit_book(request, id):
    obj=Book_Master.objects.get(id=id)
    obj1 = New_Category.objects.all().order_by("-id")
    return render(request, 'edit_book.html', {"user_id": id, "obj":obj, "obj1":obj1})

 
@csrf_exempt
def editbook(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        dop = request.POST.get('dop')
        category = request.POST.get('category')
        condition = request.POST.get('condition')
        price = request.POST.get('price')
        user_id= request.POST.get('user_id')
        

        obj = Book_Master.objects.get(id= user_id)
        obj.book_name = book_name
        obj.author = author
        obj.dop = dop
        obj.category = category
        obj.price = price
        obj.condition = condition
        
        obj.save()
        return HttpResponse('success')
    
@csrf_exempt   
def Delete_book(request):
    id = request.POST.get("id")
    obj = Book_Master.objects.get(id=id).delete()
    return HttpResponse("success")  


@csrf_exempt
def search_book_report(request):
   start_date = request.POST.get("start_date")
   end_date = request.POST.get("end_date")
 
   if Book_Master.objects.filter(created_date__gte = start_date, created_date__lte = end_date).exists():
      obj1 = Book_Master.objects.filter(created_date__gte = start_date, created_date__lte = end_date).order_by('-created_date')

      rendered = render_to_string('filter_book_report.html',{'obj1':obj1,"start_date":start_date,"end_date":end_date,})
      return HttpResponse(rendered)
   else:
       return HttpResponse("error")
   
   
   
@csrf_exempt  
def book_issue_report(request):
    session_id = request.session.get('user_id')
    login_user = request.session.get('user_name')
    print(login_user)
    print(session_id)

    obj = Student.objects.all().order_by("-id")
    list = []
    dict = {}
    for i in obj:
     dict["id"] = i.id
     dict["book_name"] = i.book_name
     dict["stu_name"] = i.stu_name
     dict["email"] = i.email
     dict["stu_class"] = i.stu_class
     dict["issue_date"] = i.issue_date
     dict["till_date"] = i.till_date
     dict["condition"] = i.condition
     dict["img"] = i.img
     dict["request"]= i.request
     dict["charges"]= i.charges
     dict["request_generator"] = i.request_generator
     print(i.request)
     list.append(dict)
     dict = {}
     
    today = date.today()
    given_date = datetime.today().date() 
    end_date =last_day_of_month(given_date)
	
    given_date = datetime.today().date()
    first_day_of_month = given_date - timedelta(days = int(given_date.strftime("%d"))-1)
     
    if session_id:
        
        return render(request, 'book_issue_report.html', {"list": list, "start_day":first_day_of_month, "end_date":end_date})
    else:
        return redirect("/")
    

from django.core.mail import send_mail ,EmailMultiAlternatives
    

@csrf_exempt    
def change_request_status(request):
    id = request.POST.get("id")
    status = request.POST.get("status")
    
    print(id)
    print(status)
    
    
    if Student.objects.filter(id = id).exists():
        
        obj = Student.objects.get(id = id)
        obj.request = status
        obj.save()
        recipient_list = [obj.email, ]
        print(obj.email)
        
        if status == "Accept":
          
          message = 'your request has been accepetd'
        else:
          message = 'your request has been rejected'
          return HttpResponse("error") 
        
    else:
        return HttpResponse("error") 
    
def request_book(request):
    obj= Book_Master.objects.all().order_by("id")
    obj1= User.objects.all().order_by("id")
    return render(request, 'request_book.html', {"obj": obj,"obj1" :obj1})



@csrf_exempt
def create_request(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        stu_name = request.POST.get('stu_name')
        stu_class = request.POST.get('stu_class')
        section = request.POST.get('section')
        email = request.POST.get('email')
        issue_date = request.POST.get('issue_date')
        till_date = request.POST.get('till_date')
        condition = request.POST.get('condition')
        request_generator = request.POST.get('request_generator')
        img = request.FILES.get('img')
      
        
        # print(type(issue_date))
        date1 = datetime.strptime(issue_date, "%Y-%m-%d")
        date2 = datetime.strptime(till_date, "%Y-%m-%d")
        # print(date1)
       
        
        difference= (date2- date1).days
        print(difference)
        print(type(difference))
        
        cat_id = Book_Master.objects.get(book_name = book_name).category
        sbk1 = New_Category.objects.get(category=cat_id)
        print(cat_id)
        sbm = Rent_Category.objects.get(hk_rent_id = sbk1.id).rent
        print(sbk1)
        print(sbm)
        
        charges= int(difference)*int(sbm)
        print(charges)
       
        print("img......................",img)
    
        if Student.objects.filter(book_name=book_name,stu_name=stu_name,stu_class=stu_class, section=section).exists():
            print("check")
            return HttpResponse('error')

        else:
            Student.objects.create(
                book_name=book_name,
                stu_name=stu_name,
                stu_class=stu_class,
                section=section,
                email=email,
                condition=condition,
                issue_date=issue_date,
                till_date= till_date,
                request= "pending",
                img=img,
                request_generator=request_generator,
                difference=str(difference),
                charges=charges,
            )
        return HttpResponse('success')
    
  
    
def edit_request(request, id):
    obj=Student.objects.get(id=id)
    obj1= Book_Master.objects.all().order_by("id")
    obj2= User.objects.all().order_by("id")
    return render(request, 'edit_request.html', {"user_id": id, "obj":obj, "obj1":obj1, "obj2":obj2})


    
@csrf_exempt
def editrequest(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        stu_name = request.POST.get('stu_name')
        stu_class = request.POST.get('stu_class')
        section = request.POST.get('section')
        email = request.POST.get('email')
        issue_date = request.POST.get('issue_date')
        till_date = request.POST.get('till_date')
        condition = request.POST.get('condition')
        
     
        request_generator = request.POST['request_generator']
        user_id= request.POST['user_id']
        img = request.FILES.get('img')
        
     
        

        obj = Student.objects.get(id= user_id)
        obj.book_name = book_name
        obj.stu_name = stu_name
        obj.stu_class= stu_class
        obj.section = section
        obj.email = email
        obj.issue_date = issue_date
        obj.till_date = till_date
        obj.condition = condition
     
        obj.request_generator = request_generator
        
        if img:
          obj.img = img
          
        else:
            pass
       
        
        obj.save()
        return HttpResponse('success')
    
@csrf_exempt   
def Delete_book1(request):
    id = request.POST.get("id")
    obj = Student.objects.get(id=id).delete()
    return HttpResponse("success")  

     
@csrf_exempt    
def change_request_status(request):
    id = request.POST.get("id")
    status = request.POST.get("status")
    
    print(id)
    print(status)
    
    
    if Student.objects.filter(id = id).exists():
        
        obj = Student.objects.get(id = id)
        obj.request = status
        obj.save()
        
        print(obj.email)
        
        if status == "Accept":
          
          message = 'your request has been accepetd'
        else:
          message = 'your request has been rejected'
        
        try:
            subject = 'welcome to library management'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [obj.email, ]
            send_mail( subject, message, email_from, recipient_list )
          
            return HttpResponse("success") 
            
        except:
            print(traceback.print_exc())
            return HttpResponse("error") 
        
    else:
        return HttpResponse("error") 
        
@csrf_exempt
def search_issue_request(request):
   start_date = request.POST.get("start_date")
   end_date = request.POST.get("end_date")
 
   if Student.objects.filter(issue_date__gte = start_date, issue_date__lte = end_date).exists():
      obj1 = Student.objects.filter(issue_date__gte = start_date,issue_date__lte = end_date).order_by('-issue_date')

      rendered = render_to_string('filter_issue_request.html',{'obj1':obj1,"start_date":start_date,"end_date":end_date,})
      return HttpResponse(rendered)
   else:
       return HttpResponse("error")      
       
       
       
@csrf_exempt  
def book_count(request):
    session_id = request.session.get('user_id')
    print(session_id)
  
    obj = New_Category.objects.all().order_by("-id")
    
    list = []
    dict = {}
    for i in obj:
        dict["id"] = i.id
        
        dict["category"] = i.category
        if Book_Master.objects.filter(category=i.category).exists():
            count= Book_Master.objects.filter(category=i.category).count()
            dict["count"] = count
            list.append(dict)
            dict = {}
        else:
            pass
    print("list.....", list)
    if session_id:
    
        return render(request, 'book_count.html', {"list": list,})
    else:
        return redirect("/")
    
    
   
def view_books(request,id):
    print(id)
    obj=  New_Category.objects.get(id= id).category
    print(obj)
    obj1 =  Book_Master.objects.filter(category= obj)
    
    
    return render(request, 'view_books.html', {"obj1":obj1,} )  
    
    
    
@csrf_exempt
def book_category(request):
    session_id = request.session.get('user_id')
    print(session_id)
    
    obj = New_Category.objects.all().order_by("category")
    list = []
    dict = {}
    for i in obj:
     dict["id"] = i.id
     dict["category"] = i.category
     
     list.append(dict)
     dict = {}
     
    if session_id:
        
        return render(request, 'book_category.html', {"list": list,})
    else:
        return redirect("/")
        
        
def add_category(request):
    return render(request, 'add_category.html' )
    
@csrf_exempt
def new_category(request):
    if request.method == "POST":
      
        category = request.POST['category']
        
      
        if New_Category.objects.filter(category=category,).exists():
            print("check")
            return HttpResponse('error')

        else:
            New_Category.objects.create(
              
                category=category,
                )
        return HttpResponse('success')
        
@csrf_exempt   
def Delete_category(request):
    id = request.POST.get("id")
    obj = New_Category.objects.get(id=id).delete()
    return HttpResponse("success") 


    
def book_rent(request):
    obj = Rent_Category.objects.all().order_by("id")
    return render(request, 'book_rent.html', {"obj": obj})  
    

def add_rent(request):
    obj = New_Category.objects.all().order_by("-id")
    return render(request, 'add_rent.html', {"obj": obj})
    
    
@csrf_exempt
def new_rent(request):
    if request.method == "POST":
      
        rent = request.POST.get('rent')
        category = request.POST.get('category')
        hourly_price = request.POST.get('hourly_price')
       
      
        if Rent_Category.objects.filter(hk_rent = category).exists():
            print("check")
            return HttpResponse('error')

        else:
            Rent_Category.objects.create(
                hk_rent_id=category,
                rent=rent,
                hourly_price=hourly_price,
                )
        return HttpResponse('success')
        
        
        
 # TRANSACTIONS VIEWS:-
 
def borrow(request):
    obj = Student.objects.filter(request="Accept", return_status = False)
    today = date.today()
    print(today)
    list = []
    dict = {}
    
    for i in obj:
        date1 = i.till_date
        book= i.book_name
        paise= i.charges
        
        if today>date1 :
            modal= (today- date1).days
            print(modal) 
            print(date1)
            cat= Book_Master.objects.get(book_name=book).category
            sbk1 = New_Category.objects.get(category=cat)
            price= Rent_Category.objects.get(hk_rent__id= sbk1.id).rent
            print(price)
            differ= int(price)*int(modal)
            print(differ)
            add= int(differ)+int(paise)
            print(add)
        else:
            cat= Book_Master.objects.get(book_name=book).category
            sbk1 = New_Category.objects.get(category=cat)
            price= Rent_Category.objects.get(hk_rent__id= sbk1.id).rent
            add= int(paise)
            print(add)
       
        dict["add"] = add
        dict["id"] = i.id
        dict["book_name"] = i.book_name
        dict["stu_name"] = i.stu_name
        dict["issue_date"] = i.issue_date
        dict["till_date"] = i.till_date
        dict["return_status"] = i.return_status
        dict["request"] = i.request
        dict["charges"] = i.charges
        dict["payment_status"] = i.payment_status
        list.append(dict)
        dict = {}
    
    print(list) 
    return render(request, "borrow.html", {'obj': list })
  


    
    
@csrf_exempt    
def change_return_status(request):
    id = request.POST.get("id")
    status1 = request.POST.get("status1")
    
    print(id)
    print(status1)
    
    
    if Student.objects.filter(id = id).exists():
        
        obj = Student.objects.get(id = id)
        obj.return_status = status1
        obj.save()
        
        return HttpResponse("success") 
        
def view_return_books(request):
   obj1 = Student.objects.filter(request="Accept", return_status= True)
   return render(request, 'view_return_books.html', {"obj1":obj1} )



@csrf_exempt    
def payment_status_completed(request):
    if request.method == "POST":
        id = request.POST.get("id")
        charges = request.POST.get("charges")
        
        print(id)
        print(charges)
        
        obj = Student.objects.get(id=id)
        obj.payment_status = True
        obj.charges = charges
        obj.save()
        return HttpResponse("success")
    
    
    
# Daily Visitors Views:

def daily_visitors(request):
    obj= Daily_Visitors.objects.all().order_by("-id")
   
    time_span=datetime.now()
    time_obj= (time_span).time()
    print(time_span)
    print(time_obj)
    list= []
    dict= {}
    for i in obj: 
       
       
            book_id_list =i.book_name  
            end = i.end_time
            visit = i.visit_time
            print(book_id_list)
            print(type(book_id_list))

  
            # Converting string to list
           
            res = ast.literal_eval(book_id_list)
            print(type(res))
            
            for lst in res:
                
              
                obj3= Book_Master.objects.get(book_name=lst).category
                
                if time_obj>end:
                    
                    print("lst...........", lst)
                   
                    obj4= New_Category.objects.get(category=obj3)
                    obj5= Rent_Category.objects.get(hk_rent__id= obj4.id).hourly_price
                    print(obj5)
                    print('end..........',end)
                    
                    differ= datetime.combine(date.today(), end) - datetime.combine(date.today(), visit)
                    print("differ........",  differ)
                    differ1= datetime.combine(date.today(), time_obj) - datetime.combine(date.today(), end)
                    print("differ1........", differ1)
                    t3=differ.seconds//3600
                    t4= differ1.seconds//3600
                    
                    price= int(t3)*int(obj5)
                    #print(price)
                    
                    total_price= int(obj5)+int(t4)+int(price)
                    print(total_price)
                    
                else:
                    
                    obj3= Book_Master.objects.get(book_name=lst).category
                    obj4= New_Category.objects.get(category=obj3)
                    obj5= Rent_Category.objects.get(hk_rent__id= obj4.id).hourly_price
                    print(obj5)
                    print('end..........',end)
                    differ= datetime.combine(date.today(), end) - datetime.combine(date.today(), visit)
                    print(differ)
                    t3=differ.seconds//3600
                    total_price= int(t3)*int(obj5)
                    
            print("id.........", i.id)      
            
            dict["id"] = i.id
            dict["total_price"] = total_price
            dict["visitor_name"] = i.visitor_name
            dict["visitor_plan"] = i.visitor_plan
            dict["email"] = i.email
            dict["contact_No"] = i.contact_No
            dict["gender"] = i.gender
            dict["book_name"] = ",".join(res)
            dict["visit_time"] = i.visit_time
            dict["end_time"] = i.end_time
            dict["accept_status"] = i.accept_status
            dict["payment_status_time"] = i.payment_status_time
        
            list.append(dict)
            dict = {}
            
    #print(list)   
    return render(request, 'daily_visitors.html', {'obj':list} )




def add_new_entry(request):
    obj= Book_Master.objects.all()
    return render(request, 'add_new_entry.html', {'obj': obj} )



@csrf_exempt
def new_entry(request):
    if request.method == "POST":
        visitor_name = request.POST.get('visitor_name')
        visitor_plan = request.POST.get('visitor_plan')
        email= request.POS.get('email')
        contact_No = request.POST.get('contact_No')
        gender = request.POST.get('gender')
        visit_time = request.POST.get('visit_time')
        end_time = request.POST.get('end_time')
        book_id_list = request.POST.get('book_id_list')
     
        print(book_id_list)
        if Daily_Visitors.objects.filter(email=email, visitor_name=visitor_name,).exists():
            print("check")
            return HttpResponse('error')

        else:
            Daily_Visitors.objects.create(
                visitor_name=visitor_name,
                visitor_plan=visitor_plan,
                email=email,
                contact_No= contact_No,
                gender=gender,
                visit_time=visit_time,
                end_time=end_time,
                book_name = json.loads(book_id_list)
            )
        return HttpResponse('success')
    

    
@csrf_exempt
def send_mail(request):
    obj= Daily_Visitors.objects.all()
    cr=datetime.now()
    cr_time=(cr).time()
    print("cr_time...........................",cr_time)
   
    for i in obj:
        end_time= (i.end_time)
        email= i.email
        
        print("end_time...........................",end_time)
        
        if end_time <= cr_time:
          
            message = 'your session has been expired'
        
        
            try:
                subject = 'welcome to library management'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email,]
                send_mail(recipient_list)
            
                return HttpResponse("success") 
            except:
                print(traceback.print_exc())
                return HttpResponse("error") 
        
        else:
          return HttpResponse("error1111111111111111") 
     
    
    
    
@csrf_exempt    
def change_request_time(request):
    id = request.POST.get("id")
    status = request.POST.get("status")
    
    print(id)
    print(status)
    
    
    if Daily_Visitors.objects.filter(id = id).exists():
        
        obj = Daily_Visitors.objects.get(id = id)
        obj.accept_status = status
        obj.save()
        
        return HttpResponse("success")  
    
    
@csrf_exempt    
def payment_status_required(request):
    if request.method == "POST":
        id = request.POST.get("id")
        total_price = request.POST.get("total_price")
        
        print(id)
        print(total_price)
        
        obj = Daily_Visitors.objects.get(id=id)
        obj.payment_status_time = True
        obj.total_price = total_price
        obj.save()
        return HttpResponse("success")
    
@csrf_exempt    
def edit_modal(request):
    if request.method == "POST":
        id = request.POST.get("id")
        category = request.POST.get("category")
        rent = request.POST.get("rent")
        hourly_price = request.POST.get("hourly_price")
        
        print(id)
        print(category)
        print(rent)
        print(hourly_price)
        
        obj = Rent_Category.objects.get(id=id)
        obj.payment_status_time = True
        obj.hk_rent__id = category
        obj.rent = rent
        obj.hourly_price = hourly_price
        obj.save()
        return HttpResponse("success")
    
