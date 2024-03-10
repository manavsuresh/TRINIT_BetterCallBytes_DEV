from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Student_Credentials as SCreds
from .models import Teacher_Credentials as TCreds
from . import views
from django.conf import settings
from django.core.mail import send_mail
message = {}
details = {}
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
def student_login(request):
    global message
    template = loader.get_template('login_student.html')
    try:
        message1 = message[views.get_ip(request)]
    except KeyError:
        message1 = ''
    mess = {
        'message' : message1,
    }
    return HttpResponse(template.render(mess,request))

def teacher_login(request):
    global message
    template = loader.get_template('login_teacher.html')
    try:
        message1 = message[views.get_ip(request)]
    except KeyError:
        message1 = ''
    mess = {
        'message' : message1,
    }
    return HttpResponse(template.render(mess,request))


def login_check_student(request):
    global nme,details,message
    a = request.POST['UID']
    b = request.POST['password']
    login_vals = SCreds.objects.all().filter(status='Active').values()
    for i in login_vals:
        if i['u_id'] == a and i['password'] == b:
            nme = i['name']
            id = i['student_id']
            ip = views.get_ip(request)    
            details[ip] = [nme,id]
            message[views.get_ip(request)] = ''

            return HttpResponseRedirect('/student/dashboard/')
    message[views.get_ip(request)] = 'Wrong Credentials!!'
    return HttpResponseRedirect('/')

def login_check_teacher(request):
    global usr,nme,details,message,unt
    a = request.POST['UID']
    b = request.POST['password']
    login_vals = TCreds.objects.all().filter(status='Active').values()
    for i in login_vals:
        if i['u_id'] == a and i['password'] == b:
            ip = views.get_ip(request)  
            nme = i['name']
            id = i['teacher_id']
            details[ip] = [nme,id]
            message[views.get_ip(request)] = ''
            
            return HttpResponseRedirect('/teacher/dashboard')
    message[views.get_ip(request)] = 'Wrong Credentials!!'
    return HttpResponseRedirect('/')

def logout(request):
    global details,message
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
    a = request.POST['name']
    b = request.POST['username']
    e = request.POST['email']
    g = request.POST['phoneNumber']
    c = request.POST['password']
    role = request.POST['role']
    if role == 'tutor':
        creds = TCreds(name=a,u_id=b,password=c,email=e,phone=g,)
        creds.save()
    elif role == 'student':
        creds = SCreds(name=a,u_id=b,password=c,email=e,phone=g,)
        creds.save()
    # message[views.get_ip(request)] = 'Registered Sucessfully!!'
    
    return HttpResponseRedirect('/')

def edit_register_student(request):
    ip = views.get_ip(request)
    try:
        ID = details[ip][1]
    except KeyError:
        return HttpResponseRedirect('/student/dashboard/')
    
    template = loader.get_template('register_edit_student.html')
    acc = SCreds.objects.get(student_id=ID)
    content = {
        'Acc':acc,
    }
    return HttpResponse(template.render(content,request))

def edit_register_process_student(request,u_id):
    return HttpResponseRedirect('/student/dashboard/')

def edit_register_teacher(request,u_id):
    ip = views.get_ip(request)
    template = loader.get_template('register_edit_teacher.html')
    acc = TCreds.objects.get(teacher_id=details[ip][0])
    content = {
        'Acc':acc,
    }
    return HttpResponse(template.render(content,request))

def edit_register_process_teacher(request,u_id):
    return HttpResponseRedirect('/teacher/dashboard/')

