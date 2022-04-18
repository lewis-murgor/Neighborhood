from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    re_path('^$',views.index,name='index'),
    re_path(r'^accounts/profile', views.profile, name='profile'),
    re_path(r'^create/neighborhood$', views.create_neighborhood, name='create-neighborhood'),
    re_path(r'^create/business/(\d+)', views.neighborhood, name='create-business'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)