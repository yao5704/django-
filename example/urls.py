from django.urls import path,include
from . import views
from django.conf.urls import url
from django.views.static import serve

app_name = 'example'
urlpatterns = [
    path('',views.index),
    path('example/right/',views.right),
    path('example/error/',views.error),
]
