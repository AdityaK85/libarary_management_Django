from msilib.schema import Condition
from tkinter import Widget
from django.db import models

# Create your models here.

class Admin_login(models.Model):
	admin_email = models.EmailField(max_length=150, null=True, blank=True)
	admin_password = models.CharField(max_length=150, null=True, blank=True)
 
     
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50, null=True, blank=True)
    designation=models.CharField(max_length=50)
    doj=models.DateField(max_length=50)
    
    
    def __str__(self) -> str:
        return self.name;
    
class Employee(models.Model):
    hk_user = models.ForeignKey(User ,null = True,on_delete=models.CASCADE)
    destination=models.CharField(max_length=50, null=True, blank=True)
    yearly_package=models.IntegerField(null=True, blank=True)
    monthly_salary=models.CharField(max_length=50, null=True, blank=True)
    
class Student(models.Model):
    book_name=models.CharField(max_length=50, null=True, blank=True)
    stu_name=models.CharField(max_length=50, null=True, blank=True)
    stu_class=models.CharField(max_length=50, null=True, blank=True)
    section=models.CharField(max_length=50, null=True, blank=True)
    email=models.EmailField(max_length=50, null=True, blank=True)
    issue_date=models.DateField(max_length=50, null=True, blank=True)
    till_date=models.DateField(max_length=50, null=True, blank=True)
    condition=models.CharField(max_length=50, null=True, blank=True)
    img= models.ImageField(max_length=50, null=True, blank=True, upload_to = "Student_Images/")
    request_generator=models.CharField(max_length=50, null=True, blank=True)
    request=models.CharField(max_length=50, null=True, blank=True)
    difference=models.CharField(max_length=50,null=True, blank=True)
    charges=models.CharField(max_length=50, null=True, blank=True)
    return_status=models.BooleanField(null=True, blank=True ,default=False)
    payment_status=models.BooleanField(null=True, blank=True ,default=False)
    
class Book_Master(models.Model):
    book_name=models.CharField(max_length=50, null=True, blank=True)
    author=models.CharField(max_length=50, null=True, blank=True)
    dop=models.DateField(max_length=50, null=True, blank=True)
    category=models.CharField(max_length=50, null=True, blank=True)
    condition=models.CharField( max_length=50, null=True, blank=True)
    price=models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(null = True, blank = True)
   
    
    
    def __str__(self) -> str:
        return self.book_name;
    
    
class Book(models.Model):
    hk_user = models.ForeignKey(Book_Master ,null = True,on_delete=models.CASCADE)
    book_name=models.CharField(max_length=50, null=True, blank=True)
    author=models.CharField(max_length=50, null=True, blank=True)
    dop=models.DateField(max_length=50, null=True, blank=True)
    category=models.CharField(max_length=50, null=True, blank=True)
    condition=models.CharField(max_length=50, null=True, blank=True)
    price=models.CharField(max_length=50, null=True, blank=True)
    
    
class New_Category(models.Model):
   category=models.CharField(max_length=150, null=True, blank=True)
   

class Rent_Category(models.Model):
   hk_rent = models.ForeignKey(New_Category ,null = True,on_delete=models.CASCADE)
   rent=models.CharField(max_length=50, null=True, blank=True)
   hourly_price= models.CharField(max_length=50, null=True, blank=True)
 
class Daily_Visitors(models.Model):
   visitor_name= models.CharField(max_length=50, null=True, blank=True)
   visitor_plan= models.CharField(max_length=50, null=True, blank=True)
   email= models.EmailField(max_length=50, null=True, blank=True)
   contact_No= models.IntegerField(null=True, blank=True)
   gender= models.CharField(max_length=50, null=True, blank=True)
   book_name= models.CharField(max_length=50, null=True, blank=True)
   visit_time= models.TimeField(null=True, blank=True)
   end_time= models.TimeField(null=True, blank=True)
   accept_status= models.CharField(max_length=50, null=True, blank=True)
   payment_status_time= models.BooleanField(null=True, blank=True ,default=False)
   total_price=models.CharField(max_length=50, null=True, blank=True)
   

	