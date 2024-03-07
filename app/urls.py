from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('Signin',views.Signin,name='Signin'),
    path('login',views.handlelogin,name='handlelogin'),
    path('form',views.submit_project,name='submit_project'),
    path('submit_project',views.submit_project,name='submit_project'),
    path('welcome',views.projects, name='projects'),
]
