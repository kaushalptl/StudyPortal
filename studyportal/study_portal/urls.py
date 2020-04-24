from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("video", views.video, name="video"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("signuphandle", views.signuphandle, name="signuphandle"),
    path("loginhandle", views.loginhandle, name="loginhandle"),
    path("tutorial/<int:course_id>/", views.tutorial, name="tutorial"),
    path("course", views.course, name="course"),
    path("question", views.question, name="question"),
    path("answer/<que_id>/", views.answer, name="answer"),
    path("material", views.material, name="material"),
    path("contact", views.contact, name="contact"),
]
