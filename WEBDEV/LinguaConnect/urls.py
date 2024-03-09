from django.urls import path,include
from . import views
from . import views_login as log
from . import views_teacher as teacher
from . import views_student as student
from django.conf import settings
from django.conf.urls.static import static


#For UI output
urlpatterns = [
    path('',log.login,name='login'),
    path('student/login_check/',log.login_check_student,name='student_check'),
    path('teacher/login_check/',log.login_check_teacher,name='teacher_check'),
    path('register/',log.register,name='register'),
    path('teacher/register_edit/<str:u_id>',log.edit_register_student,name='student_regedit'),
    path('teacher/register_edit/done/<str:u_id>',log.edit_register_process_student,name='student_regedit_process'),

    path('teacher/register_edit/<str:u_id>',log.edit_register_student,name='teacher_regedit'),
    path('teacher/register_edit/done/<str:u_id>',log.edit_register_process_student,name='teacher_regedit_process'),
    path('register/process/',log.process_register,name='process'),
    path('teacher/dashboard/',teacher.dashboard,name="Teacher_Dashboard"),
    path('teacher/dashboard/',student.dashboard,name="Student_Dashboard")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
