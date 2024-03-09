from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Student_Credentials as SCreds
from .models import Teacher_Credentials as TCreds
from .models import Classes,Teacher
from . import views
from . import views_login
from . import views_teacher
from django.conf import settings
from django.core.mail import send_mail

def dashboard(request):
    template = loader.get_template('teacher_dashboard.html')
    ip = views.get_ip(request)
    try:
        name = views_login.dets()[ip][0]
        ID = views_login.dets()[ip][1]
    except KeyError:
        return HttpResponseRedirect('/')
    languages = Teacher.objects.all().values()
    languages = languages.filter(Teacher_ID = ID)
    classes_sch = Classes.objects.all().values()
    Classes_sch = Classes_sch.filter(Teacher=name)
    Classes_sch = Classes_sch.filter(Class_Date = date.today())
    content = {
        'language_prof' : languages,
        'classes' : classes_sch, 
    }
    return HttpResponse(template.render(content,request))

def add_language(request):
    template = loader.get_template('add_language.html')
    ip = views.get_ip(request)
    try:
        name = views_login.dets()[ip][0]
    except KeyError:
        return HttpResponseRedirect('/')
    
    content = {}
    return HttpResponse(template.render(content,request))

def add_language_process(request):
    ip = views.get_ip(request)
    Lang = request.POST['']
    ID = views_login.dets()[ip][1]
    prof = request.POST['']
    comm = Teacher(Teacher_ID=ID,Language=Lang,Proficiency=prof)
    comm.save()
    return HttpResponseRedirect('/teacher/dashboard/')

def add_class(request):
    template = loader.get_template('add_class.html')
    ip = views.get_ip(request)
    try:
        name = views_login.dets()[ip][0]
    except KeyError:
        return HttpResponseRedirect('/')
    
    content = {}
    return HttpResponse(template.render(content,request))

def add_class_process(request):
    ip = views.get_ip(request)
    Lang = request.POST['']
    Pr = request.POST['']
    Tim = request.POST['']
    Dt = request.POST['']
    Teach = views_login.dets()[ip][0]
    classes_ = Classes(Language=Lang,Price=Pr,Timing=Tim,Class_Date=Dt,Teacher=Teach)
    classes_.save()
    return HttpResponseRedirect('/teacher/dashboard/')
