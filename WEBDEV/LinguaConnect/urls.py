from django.urls import path,include
from . import views
from . import views_login as log
from . import views_ticketing as tick
from django.conf import settings
from django.conf.urls.static import static


#For UI output
urlpatterns = [
    path('',log.login,name='login'),
    path('login_check/',log.login_check,name='check'),
    # path('register/',log.register,name='register'),
    # path('register/process/',log.process_register,name='process'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
