from django.contrib import admin
from django.urls import path, re_path
from library_app import views


urlpatterns = [
    path('test/', views.test, name='test'),

    # Login URLS:-
    
    path('', views.login, name='login'),
    path('login_check/', views.login_check, name='login_check'),
    path('logout/', views.logout, name='logout'),
    
    #dashboard URls:-
    
    path('dashboard/', views.dashboard, name='dashboard'),
    
    
    #employee view URLS:-
    path('employee_view/', views.employee_view, name='employee_view'),
    path('addup/',views.add_employee,name ='add_employee'),
    re_path('edit_details/(?P<id>[0-9]+)/$', views.edit_details, name='edit_details'),
    path('Delete_employee/',views.Delete_employee,name = 'Delete_employee'),
    path('user', views.create_user, name='create_user'),
    path('student', views.create_student, name='create_student'),
   
    #Book Master URLS:-
    path('book_master/', views.book_master, name='book_master'),
    path('book', views.create_book, name='create_book'),
    path('editbook', views.editbook, name='editbook'),
    re_path('edit_book/(?P<id>[0-9]+)/$', views.edit_book, name='edit_book'),
    path('Delete_book/',views.Delete_book,name = 'Delete_book'),
   

    #re_path('edit/', views.edit_details, name='edit_details'),
    
    
    # Employee Report Urls:-
    
    path('Delete_book1/',views.Delete_book1,name = 'Delete_book1'), 
    path('addbook/',views.add_book,name ='add_book'),
    path('search_book_report/',views.search_book_report,name ='search_book_report'),
    path('search_employee_report/',views.search_employee_report,name ='search_employee_report'),
    
    # Book Issues URLS:-
    
    path('book_issue_report/',views.book_issue_report,name ='book_issue_report'),
    path('request_book/',views.request_book,name ='request_book'),
    path('book_request', views.create_request, name='create_request'),
    re_path('edit_request/(?P<id>[0-9]+)/$', views.edit_request, name='edit_request'),
    path('editrequest', views.editrequest, name='editrequest'),
    path('book_category/',views.book_category,name ='book_category'),
    path('change_request_status/',views.change_request_status,name='change_request_status'),
    path('search_issue_request/',views.search_issue_request,name ='search_issue_request'),
    
    
    
    #Available Books Urls:-
    path('book_count/',views.book_count,name ='book_count'),
    re_path('view_books/(?P<id>[0-9]+)/$', views.view_books, name='view_books'),
    path('add_category/',views.add_category,name ='add_category'),
    path('new_category/', views.new_category, name='new_category'),
    path('Delete_category/',views.Delete_category,name = 'Delete_category'), 
    
    
    # Book_Rent URLS:-
    
    path('book_rent/',views.book_rent,name ='book_rent'),
    path('add_rent/',views.add_rent,name ='add_rent'),
    path('new_rent/',views.new_rent,name ='new_rent'),
    
    
    # Transactions URLS:-
    path('borrow/',views.borrow,name ='borrow'),
    path('change_return_status/',views.change_return_status,name='change_return_status'),
    path('view_return_books/',views.view_return_books,name ='view_return_books'),
    path('payment_status_completed/',views.payment_status_completed,name='payment_status_completed'),
    
    
    
    #Daily Visitors URLS:
    
    path('daily_visitors/', views.daily_visitors, name='daily_visitors'),
    path('add_new_entry/', views.add_new_entry, name='add_new_entry'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('change_request_time/', views.change_request_time, name='change_request_time'),
    path('payment_status_required/', views.payment_status_required, name='payment_status_required'),
    path('edit_modal/', views.edit_modal, name='edit_modal'),
    path('send_mail/', views.send_mail, name='send_mail'),
    

]