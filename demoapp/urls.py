# from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
# # from django.conf import settings


urlpatterns = [
    path('', views.login_page, name='login'),
    path('login/',views.login_request, name='login_request'),
    path('signup/',views.registers, name='signup'),
    path('signup/register/',views.registerpage, name='registerpage'),

    
]
# urlpatterns = [
#     path('', views.registers, name='registers'),
#     path('register/',views.registerpage, name='registerpage'),
    
# ]