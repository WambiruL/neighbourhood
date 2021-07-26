from . import views
from django.conf.urls import url 
from django.contrib.auth import views as auth_views


urlpatterns=[
    url(r'register/',views.registerPage,name='register'),
    url(r'login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    url(r'^$',views.index,name = 'index'),
    url(r'^logout/',auth_views.LogoutView.as_view(), {"next_page": '/index'}, name='logout',),
    url(r'profile/',views.profileView,name='profile'),
    url(r'lanet/',views.lanet,name='lanet'),
    url(r'milimani/',views.milimani,name='milimani'),
    url(r'kiamunyi/',views.kiamunyi,name='kiamunyi'),
    url(r'Lbusiness/',views.lanetBusiness,name='Lbusiness'),
    url(r'Lauth/',views.lanetAuth,name='Lauth'),
    url(r'Mauth/',views.milimaniAuth,name='Mauth'),
    url(r'Lhealth/',views.lanetHealth,name='Lhealth'),
    url(r'Mhealth/',views.milimaniHealth,name='Mhealth'),
    url(r'Mbusiness/',views.milimaniBusiness,name='Mbusiness'),
    url(r'kiamunyiB/',views.kiamunyiBusiness,name='kiamunyiB'),
    url(r'business_form/',views.submitBusinessK,name='business_form'),
    url(r'business_form/',views.submitBusinessL,name='business_form'),
    url(r'business_form/',views.submitBusinessM,name='business_form'),
    url(r'Kbusiness/',views.kiamunyiBusiness,name='Kbusiness'),
    url(r'Kauth/',views.kiamunyiAuth,name='Kauth'),
    url(r'Khealth/',views.kiamunyiHealth,name='Khealth'),
    url(r'LPosts/',views.lanetPost,name='LPosts'),
    url(r'KPosts/',views.kiamunyiPost,name='KPosts'),
    url(r'MPosts/',views.milimaniPost,name='MPosts'),
     url(r'post_form/',views.submitPostK,name='post_form'),
      url(r'post_form/',views.submitPostL,name='post_form'),
       url(r'post_form/',views.submitPostM,name='post_form'),

]
