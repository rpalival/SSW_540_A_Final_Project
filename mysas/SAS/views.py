from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Welcome")


def user_list(request):
    return render(request, "user_list.html")