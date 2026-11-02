# from django.shortcuts import render
# import mysql.connector as sql
# em=''
# pwd=''
# # Create your views here.
# def loginaction(request):
#     global em,pwd
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",passwd="12345",database='website')
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="email":
#                 em=value
#             if key=="password":
#                 pwd=value
        
#         c="select * from users where email='{}' and password='{}'".format(em,pwd)
#         cursor.execute(c)
#         t=tuple(cursor.fetchall())
#         if t==():
#             return render(request,'error.html')
#         else:
#             return render(request,"welcome.html")

#     return render(request,"login_page.html")


# views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login

# def loginaction(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         print(email, password)
#         # Use Django's authenticate function to check user credentials
#         user = authenticate(request, Email=email, assword=password)
#         print(user)

#         if user is not None:
#             # Log in the user
#             login(request, user)
#             return render(request, "welcome.html")
#         else:
#             return render(request, 'error.html')

#     return render(request, "login_page.html")



from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

def loginaction(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # fname = user.first_name
            return render(request, "welcome.html")

        else:
            return render(request, 'error.html')
    return render(request, "login_page.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out succeffully")
    return redirect("signup")