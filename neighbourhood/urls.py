from . import views
from django.conf.urls import url 
from django.contrib.auth import views as auth_views


urlpatterns=[
    url(r'register/',views.registerPage,name='register'),
    url(r'login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    url(r'^$',views.index,name = 'index'),
    url(r'^logout/',auth_views.LogoutView.as_view(), {"next_page": '/login'}, name='logout',),
    url(r'profile/',views.profileView,name='profile'),
    url(r'lanet/',views.lanet,name='lanet'),
    url(r'milimani/',views.milimani,name='milimani'),
]
