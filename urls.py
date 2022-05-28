from django.urls import path
from .import views

urlpatterns = [
    path('', views.first, name='HOME'),
    path('NEWS', views.second, name='NEWS'),
    path('DISCOGRAPHY', views.third, name='DISCOGRAPHY'),
    path('BIOGRAPHY', views.fourth, name='BIOGRAPHY'),
    path('SCHEDULE', views.fifth, name='SCHEDULE'),
    path('MEDIA', views.sixth, name='MEDIA'),
    path('BLOG', views.seventh, name='BLOG'),
    path('GOODS', views.eighth, name='GOODS'),

]