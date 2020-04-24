from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Video
from .models import Course, User, Tutorial, Question, Answer, Material
from django.http import HttpResponseRedirect
import os
from lxml import html
from django.contrib import messages


def tutorial(request, course_id):
    request.session['course_id'] = course_id
    if request.method == "POST":
         name= request.POST['name']
         print("Name ...",name)
         tut = Tutorial.objects.filter(course_name=name).values().order_by('sq_no')

    else:
        tut = Tutorial.objects.filter(course_id=course_id).values().order_by('sq_no')
    return render(request, 'tutorial.html', {'tut': tut,'c_id':course_id})


def index(request):
    c_id=request.session.get('course_id')
    cor = Course.objects.all()
    cor1 = {'cor': cor,'c_id':c_id}
    return render(request, 'index.html',cor1)


def video(request):
    c_id=request.session.get('course_id')
    video = Video.objects.filter(course_id=c_id).values().order_by('order')
    print("video",video)
    param = {'video':video,'c_id':c_id}
    return render(request, 'video.html', param)


def login(request):
    return render(request,'login.html')




def loginhandle(request):
    if request.method=="POST":
        email=request.POST['email']
        pwd=request.POST['password']
        users = User.objects.get(email=email)
    
        user={"name" : users.name, "email" : users.email}

        if pwd == users.password:
            request.session['name']=users.name
            return render(request, 'index.html', user)
        else :
             return(request, 'login.html', {'error' : 'Email or Password Incorrect'})

    else:
        return HttpResponse("Invalid Method")


def signup(request):
    return render(request,'signup.html')




def signuphandle(request):
    if request.method=="POST":
        name1 = request.POST['name']
        email1 = request.POST['email']
        contact1 = request.POST['contact']
        password1 = request.POST['password']
        # cpassword = request.POST['cpassword']
        myuser = User(name=name1, email=email1, contact_no=contact1, password=password1)
        myuser.save()
        return HttpResponseRedirect('/study_portal/login')

    else:
        return HttpResponse("Invalid Method",)    





def material(request):
    c_id=request.session.get('course_id')
    material = Material.objects.filter(course_id=c_id).values()
    print(material)
    return render(request,'material.html', {'material':material,'c_id':c_id})



def question(request):
    c_id=request.session.get('course_id')
    if request.method == 'POST':
        ques = request.POST.get('question')
        print("Questions",ques)
        que = Question(question=ques,course_id=Course.objects.get(pk=c_id))
        que.save()
    que = Question.objects.filter(course_id=c_id)
    ans = Answer.objects.filter(course_id=c_id)
    #ans = Answer.objects.filter(que_id=que_id)
    print(ans)
    q1 = {'que': que,'ans':ans,'c_id':c_id}
    return render(request, 'query.html', q1)


def answer(request, que_id):
    c_id=request.session.get('course_id')
    if request.method == 'POST':
        ans = request.POST.get('answer')
        print("Ans",ans)
        a = Answer(que_id=Question.objects.get(pk=que_id),answer=ans,course_id=Course.objects.get(pk=c_id))
        a.save()
        return HttpResponseRedirect('/study_portal/question')
    que=Question.objects.filter(que_id=que_id)
    ans = Answer.objects.filter(que_id=que_id)
    return render(request, 'answer.html', {'ans': ans,'que':que,'c_id':c_id})


def course(request):
    c_id=request.session.get('course_id')
    cor = Course.objects.all()
    cor1 = {"cor": cor,'c_id':c_id}
    return render(request, 'courses.html', cor1)


def contact(request):
    return render(request,'contact.html')    


