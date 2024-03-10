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
    template = loader.get_template('student_dashboard.html')
    ip = views.get_ip(request)
    try:
        user = views_login.dets()[ip][0]
    except KeyError:
        return HttpResponseRedirect('/')
    
    content = {}
    return HttpResponse(template.render(content,request))
