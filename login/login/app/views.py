# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def get_name(request):
    return render(request, 'home.html',context=None)

def redirect_view(request):
   # response = redirect('welcome.html')
    return render(request, 'welcome.html')

def register(request):
    return render(request, 'register.html')

def reg(request):
	import mysql.connector
	from passlib.hash import sha256_crypt
	uname= request.GET.get('name')
	uemail=request.GET.get('email')
	upass=request.GET.get('pass')
	uconpass=request.GET.get('conpass')
	umobile=request.GET.get('mobile')

#connecting to the database

	mydb=mysql.connector.connect(
	host="localhost",
	user="user",
	passwd="Sushma@12345",
	database="customer_db",
	)
	password = sha256_crypt.encrypt(upass)
	mycursor = mydb.cursor()
	
#Inserting value into the database
	try:
	 sql= "INSERT INTO customer_db VALUES (%s, %s, %s, %s)"
	 val = (uname, password, umobile, uemail)
	 mycursor.execute(sql,val)
	 mydb.commit()
	 return render(request,'home.html', context=None)
	
	except mysql.connector.Error as error :
		mydb.rollback()
		return HttpResponse("Creation of Account Failed,User Already exists") 


def logging(request):
	import mysql.connector
	from passlib.hash import sha256_crypt
	uemail=request.GET.get('email')
	upasswd=request.GET.get('pass')
	mydb= mysql.connector.connect(
	host="localhost",
	user="user",
	passwd="Sushma@12345",
	database="customer_db",
	)
	mycursor = mydb.cursor()
	mycursor.execute("SELECT password FROM customer_db where email=%s", [uemail])
        myresult = mycursor.fetchall()
	val = myresult[0]
	verify = sha256_crypt.verify(upasswd, val[0])
	if(verify == True):
		return render(request,'welcome.html', context=None)
	else:
		return HttpResponse("Incorrect UserID or Password")
	
