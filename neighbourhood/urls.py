from . import views
from django.conf.urls import url 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
   
    url(r'register/',views.registerPage,name='register'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)