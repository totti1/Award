from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('^upload_project/',views.upload_project,name = 'upload_project'),
    url('^upload_profile/',views.upload_profile,name = 'upload_profile'),
    url('^profile/',views.my_profile,name = 'profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)