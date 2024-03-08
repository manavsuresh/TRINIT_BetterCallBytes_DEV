from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Student_Credentials as SCreds
from .models import Teacher_Credentials as TCreds
from . import views
from django.conf import settings
from django.core.mail import send_mail


def dets():
    return details

def login(request):
    global message   
    template = loader.get_template('dashboard.html')
    try:
        message1 = message[views.get_ip(request)]
    except KeyError:
        message1 = ''
    mess = {
        'message' : message1,
    }
    return HttpResponse(template.render(mess,request))

def login_check_student(request):
    global usr,nme,details,message,unt
    a = request.POST['UID']
    b = request.POST['password']
    login_vals = SCreds.objects.all().filter(status='Active').values()
    for i in login_vals:
        if i['u_id'] == a and i['password'] == b:
            usr = i['dept']
            nme = i['name']
            unt = i['unit']
            eid = i['emp_id']
            phone = i['phone']
            user_mail = i['email']
            ip = views.get_ip(request)    
            details[ip] = [usr,nme,unt,eid,phone]
            detail = [ip,usr,nme,eid,unt]
            message[views.get_ip(request)] = ''
            send_mail(subject='Login of your Lingua Connect Account',message=f'From {ip}',recipient_list=[user_mail],fail_silently=True,from_email=settings.EMAIL_HOST_USER)

            return HttpResponseRedirect('/index/')
    message[views.get_ip(request)] = 'Wrong Credentials!!'
    return HttpResponseRedirect('/')

def login_check_teacher(request):
    global usr,nme,details,message,unt
    a = request.POST['UID']
    b = request.POST['password']
    login_vals = TCreds.objects.all().filter(status='Active').values()
    for i in login_vals:
        if i['u_id'] == a and i['password'] == b:
            details[ip] = []
            ip = views.get_ip(request)    
            details[ip] = [nme,usr]
            detail = [ip,nme,usr,]
            message[views.get_ip(request)] = ''
            
            return HttpResponseRedirect('/index/')
    message[views.get_ip(request)] = 'Wrong Credentials!!'
    return HttpResponseRedirect('/')

def logout(request):
    global usr,nme,details,message,unt
    usr = None
    nme = None
    unt = None
    try:
        del details[views.get_ip(request)]
    except KeyError:
        pass
    message[views.get_ip(request)] = 'Logged out successfully!!'
    return HttpResponseRedirect('/')
