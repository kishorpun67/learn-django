from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import random
from django.core.paginator import Paginator
from django.db.models import *

# Create your views here.

@login_required(login_url="login")
def receipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        user = request.user
        Receipe.objects.create(
            user = user,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )
        return redirect('/receipe')
    receipes = Receipe.objects.all()
    # for receipe in receipes:
    #     receipe.receipe_view_counter = random.randint(0,100)
    #     receipe.save()
    if request.GET.get('search'):
        receipes = receipes.filter(receipe_name__icontains = request.GET.get('search'))
        # return HttpResponse(receipes)
    return render(request, 'receipe.html', context={'receipes':receipes})

@login_required(login_url="login")
def delete_receipe(request, id):
    Receipe.objects.filter(id=id).delete()
    return redirect('/receipe')

@login_required(login_url="login")
def upate_receipe(request, id):
    receipe = Receipe.objects.get(id=id)
    if request.method == 'POST':
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')

        receipe.receipe_name = receipe_name
        receipe.receipe_description = receipe_description
        if receipe_image:
            receipe.receipe_image = receipe_image
        receipe.save()
        return redirect('/receipe')
    
    # return HttpResponse(receipe)
    return render(request, 'edit_receipe.html', {'receipe':receipe})

@login_required(login_url="login")
def logout_page(request):
    auth.logout(request)
    return redirect('/login')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        # return HttpResponse(user)
        if user is None:
            messages.error(request, "Invalid Creditials.")
            return redirect('/login')
        else:
            auth.login(request, user)
            return redirect('/receipe')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        userCheck = User.objects.filter(username = name)
        if userCheck.exists():
            messages.error(request, "User already exists.")
            return redirect('/register')

        user = User.objects.create(
            username=name,
            email=email,
            password=password
        )
        user.set_password(password)
        user.save()
        return redirect('/login')
    return render(request,'register.html')

from django.db.models import Q
def get_students(request):
    students = Student.objects.all()
    if request.GET.get('search'):
        search = request.GET.GET('search')
        students = students.filter(Q(student_name__icontains=search) | 
                                   Q(department__deparment__icontains = search )|
                                   Q(student_id__student_id__icontains = search )
                                     )
    students = Paginator(students, 25)
    page_number = request.GET.get('page',1)
    students = students.get_page(page_number)
    # return HttpResponse(students)
    return render(request,'report/student.html', context={'students':students})

def see_marks(request, student_id):
    marks = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    totalMarkas = marks.aggregate(marks = Sum('marks'))
    return render(request, 'report/see_marks.html', context={'marks': marks, 'totalMarkas': totalMarkas})