from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserView
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

user_list = UserView.as_view({
    'post' : 'create',
    'get' : 'list'
})

user_detail = UserView.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})


urlpatterns = [
    path('', views.index),
    path('admin', admin.site.urls),
    path('user', user_list, name = 'user_list'),
    path('user/<int:pk>/', user_detail, name ='user_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)