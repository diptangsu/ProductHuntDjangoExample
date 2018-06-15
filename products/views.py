from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product


def home(request):
    allproducts = Product.objects.all()
    return render(request, 'products/home.html', {'allproducts': allproducts})


@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'products/create.html')
    else:
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] \
                and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            url = request.POST['url']
            product.url = url if url.startswith('http://') or url.startswith('https://') else 'http://' + url
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()

            return redirect(f'/products/{product.id}')
        else:
            return render(request, 'products/create.html', {'error': 'All fields are required.'})


def details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/detail.html', {'product': product})
