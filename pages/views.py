from django.shortcuts import render
from .models import Product

def laptop(request):
    content_list = Product.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'pages/category/laptop.html', context)
def mainpage(request):
    return render(request, 'pages/mainpage.html')

def home(request):
    return render(request, 'pages/mainpage.html')

def search(request):
    return render(request, 'pages/search.html')
def company(request):
    return render(request, 'pages/company_info.html')

def laptop_A(request):
    return render(request, 'pages/product/laptop_A.html');

def laptop_B(request):
    return render(request, 'pages/product/laptop_B.html');

def laptop_C(request):
    return render(request, 'pages/product/laptop_C.html');
def tv(request):
    return render(request, 'pages/category/tv.html');

def kitchen(request):
    return render(request, 'pages/category/kitchen.html');

def beauty(request):
    return render(request, 'pages/category/beauty.html');

def robot(request):
    return render(request, 'pages/category/robot.html');