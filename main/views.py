from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from main.forms import ProductForm
from main.models import Product
import datetime

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def increment(request, id):
    product = Product.objects.get(pk=id)
    product.amount += 1
    product.save()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def decrement(request, id):
    product = Product.objects.get(pk=id)
    if product.amount > 0:
        product.amount -= 1
        product.save()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def delete (request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def input_item(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "input_item.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context) 

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name=name, amount=amount, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()