from django.contrib import admin
from .models import *
from .models import User
# Register your models here.

class Admin_login_class(admin.ModelAdmin):
	list_display = ('id','admin_email','admin_password')
admin.site.register(Admin_login ,Admin_login_class)

#admin.site.register(Signup)


class User_class(admin.ModelAdmin):
	list_display = ('id','name','email','designation','doj')
admin.site.register(User ,User_class)


class Employee_class(admin.ModelAdmin):
	list_display = ('id','destination','yearly_package','monthly_salary')
admin.site.register(Employee ,Employee_class)


class Student_class(admin.ModelAdmin):
	list_display = ('id','book_name', 'stu_name','stu_class' ,'section', 'email','issue_date', 'till_date', 'condition','img','request_generator' , 'request', 'difference','charges',"return_status", "payment_status")
admin.site.register(Student ,Student_class)


class Book_Master_Class(admin.ModelAdmin):
	list_display = ('id','book_name','author','dop','category', 'condition', 'price')
admin.site.register(Book_Master ,Book_Master_Class)


class Book_class(admin.ModelAdmin):
	list_display = ('id','book_name','author','dop','category', 'condition', 'price')
admin.site.register(Book ,Book_class)


class New_Category_Class(admin.ModelAdmin):
	list_display = ('id','category',)
admin.site.register(New_Category ,New_Category_Class)


class Rent_Category_Class(admin.ModelAdmin):
	list_display = ('id','rent','hourly_price')
admin.site.register(Rent_Category ,Rent_Category_Class)

class Daily_Visitors_Class(admin.ModelAdmin):
	list_display = ('id','visitor_name','visitor_plan' , 'email','contact_No', 'gender','book_name','visit_time','end_time','accept_status','payment_status_time','total_price' )
admin.site.register(Daily_Visitors ,Daily_Visitors_Class)

