from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

# USED FOR LOGICAL CODE => IF , IF ELSE ETC....

# ALL COMMANDS FROM STARTING =>
# 1. py -m venv env 
# 2. cd env/scripts/
# 3. ./activate
# 4. cd ../../
# 5. pip install django 
# 6. django-admin startproject project
# 7. cd project
# 8. py manage.py startapp app
# 9. py manage.py makemigrations
# 10. py manage.py migrate
# 11. py manage.py runserver


# def home(request):
#     return HttpResponse ("<h1 style = color:red > Hello... </h1>")
    # return HttpResponse("hello....")

# def home(request):
#     data=[{
#         'name':True,
#         'age':False,
#         'city':None
#     },{
#         'name':'mayank',
#         'age':22
#     },{
#         'city':'bhopal'
#     }]
#     return JsonResponse(data,safe=False)

# def home(request):
#     return render(request , 'home.html')


def landingpage(req):
    return render(req,'landing.html')

def home(req):
    return render(req,'home.html')


def trending(req):
    return render(req,'trending.html')

def history(req):
    return render(req,'history.html')

def subscription(req):
    return render(req,'subscription.html')

def library(req):
    return render(req,'library.html')