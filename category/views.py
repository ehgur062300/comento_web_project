from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def postview(request):
    def get(self, request):
        id = request.GET.get('id', '')

    return render(request, 'pages/product/laptop_A.html', {
        'post': get_object_or_404(postview, pk = id)
    })

def product_detail(request, product_id):
    content_list = Product.objects.get(id=product_id)
    context = {'content_list': content_list}
    return render(request, 'pages/product/product_detail.html', context)


def laptop(request):
    content_list = Product.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'pages/category/laptop.html', context)


def tv(request):
    return render(request, 'pages/category/tv.html');


def kitchen(request):
    return render(request, 'pages/category/kitchen.html');


def beauty(request):
    return render(request, 'pages/category/beauty.html');


def robot(request):
    return render(request, 'pages/category/robot.html');