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
    template = loader.get_template('homepage.html')
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

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({},request))

def process_register(request):
    global message
    a = request.POST['Name']
    b = request.POST['UID']
    h = request.POST['EID']
    e = request.POST['Email']
    g = request.POST['Phoneno']
    c = request.POST['password']
    d = request.POST['department']
    f = request.POST['unit']
    role = request.POST['role']
    if role == 'teacher':
        creds = TCreds(name=a,u_id=b,emp_id=h,password=c,dept=d,email=e,phone=g,)
        creds.save()
    elif role == 'student':
        creds = SCreds(name=a,u_id=b,emp_id=h,password=c,dept=d,email=e,phone=g,)
        creds.save()
    # message[views.get_ip(request)] = 'Registered Sucessfully!!'
    
    # return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def edit_register_student(request,u_id):
    template = loader.get_template('register_edit_student.html')
    acc = SCreds.objects.get(u_id=u_id)
    content = {
        'Acc':acc,
    }
    return HttpResponse(template.render(content,request))

def edit_register_process_student(request,u_id):
    acc = SCreds.objects.get(u_id=u_id)
    a = request.POST['Name']
    b = request.POST['UID']
    h = request.POST['EID']
    e = request.POST['Email']
    g = request.POST['Phoneno']
    c = request.POST['password']
    d = request.POST['department']
    f = request.POST['unit']
    i = request.POST['status']

    acc.name= a
    acc.u_id= b
    acc.emp_id= h
    acc.email= e
    acc.phone= g
    acc.password= c
    acc.unit= f
    acc.dept= d
    acc.status= i

    acc.save()
    return HttpResponseRedirect('/student/dashboard/')

def edit_register_teacher(request,u_id):
    template = loader.get_template('register_edit_teacher.html')
    acc = TCreds.objects.get(u_id=u_id)
    content = {
        'Acc':acc,
    }
    return HttpResponse(template.render(content,request))

def edit_register_process_teacher(request,u_id):
    acc = TCreds.objects.get(u_id=u_id)
    a = request.POST['Name']
    b = request.POST['UID']
    h = request.POST['EID']
    e = request.POST['Email']
    g = request.POST['Phoneno']
    c = request.POST['password']
    d = request.POST['department']
    f = request.POST['unit']
    i = request.POST['status']

    acc.name= a
    acc.u_id= b
    acc.emp_id= h
    acc.email= e
    acc.phone= g
    acc.password= c
    acc.unit= f
    acc.dept= d
    acc.status= i

    acc.save()
    return HttpResponseRedirect('/teacher/dashboard/')

