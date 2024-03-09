from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Student_Credentials as SCreds
from .models import Teacher_Credentials as TCreds
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
        #user =views_login.dets()[ip][1]
    except KeyError:
        return HttpResponseRedirect('/')
    
    content = {}
    # return content,template
    return HttpResponse(template.render(content,request))

