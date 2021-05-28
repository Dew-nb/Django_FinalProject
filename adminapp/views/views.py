from django.http import HttpResponse
from django.shortcuts import render, redirect
from adminapp.models import UserInfo


# Create your views here.
def index(request):
    return redirect(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        name = request.POST.get('name1')
        pwd = request.POST.get('password1')
        ret = UserInfo.objects.filter(username=name, password=pwd)
        if ret:
            return redirect('products')
    return render(request, 'login.html', {'username': name})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('password')
        info = UserInfo.objects.create(username=name, password=pwd)
        info.save()
        return redirect('login')


def products(request):
    return render(request, 'products.html')


def introduction(request):
    return render(request, 'introduction.html')
