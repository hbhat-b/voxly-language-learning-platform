# from django.shortcuts import render
# import mysql.connector as sql
# fn=''
# ln=''
# g=''
# em=''
# pwd=''
# # Create your views here.
# def signaction(request):
#     global fn,ln,g,em,pwd
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",passwd="12345",database='website')
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="first_name":
#                 fn=value
#             if key=="last_name":
#                 ln=value
#             if key=="gender":
#                 g=value
#             if key=="email":
#                 em=value
#             if key=="password":
#                 pwd=value
        
#         c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,g,em,pwd)
#         cursor.execute(c)
#         m.commit()

#     return render(request,"signup_page.html")


# views.py

# signup/views.py
# from django.shortcuts import render, redirect
# from .models import User

# def signaction(request):
#     if request.method == "POST":
#         # Retrieve form data
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         gender = request.POST.get("gender")
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         # Create and save a new user
#         user = User(
#             first_name=first_name,
#             last_name=last_name,
#             gender=gender,
#             email=email,
#             password=password,
#         )
#         user.save()

#         # Redirect to the 'signup_page' URL
#         return redirect("signup")

#     return render(request, "signup_page.html")


from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User

def signaction(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.firstname = first_name
        myuser.lastname = last_name

        myuser.save()

        return redirect('login')

    return render(request, 'signup_page.html')
