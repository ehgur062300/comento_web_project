from django.shortcuts import render, get_object_or_404


def mainpage(request):
    return render(request, 'pages/mainpage.html')


def home(request):
    return render(request, 'pages/mainpage.html')


def search(request):
    return render(request, 'pages/search.html')

def company(request):
    return render(request, 'pages/company_info.html')


def laptop_B(request):
    return render(request, 'pages/product/laptop_B.html');


def laptop_C(request):
    return render(request, 'pages/product/laptop_C.html');