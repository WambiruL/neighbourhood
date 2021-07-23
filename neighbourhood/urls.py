from . import views
from django.conf.urls import url 
from django.contrib.auth import views as auth_views


urlpatterns=[
    url(r'register/',views.registerPage,name='register'),
    url(r'login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
]
