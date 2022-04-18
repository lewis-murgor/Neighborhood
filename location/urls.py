from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    re_path('^$',views.index,name='index'),
    re_path(r'^accounts/profile', views.profile, name='profile'),
    re_path(r'^update/profile$', views.update_profile, name='update-profile'),
    re_path(r'^create/neighborhood$', views.create_neighborhood, name='create-neighborhood'),
    re_path(r'^create/business/(\d+)', views.neighborhood, name='create-business'),
    re_path(r'^create/post',views.create_post,name='create-post'),
    re_path(r'^post/',views.post,name='post'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^join/',views.join,name ='join'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)