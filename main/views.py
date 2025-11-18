import datetime
import json
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.utils.html import strip_tags
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        new_product = Product(
            name=name, 
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper description type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg'),
            status=response.status_code,
            reason=response.reason
        )

    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    # Get data from POST
    name = strip_tags(request.POST.get("name"))  # strip HTML tags
    description = strip_tags(request.POST.get("description"))  # strip HTML tags
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    price = request.POST.get("price")  
    user = request.user
    is_featured = request.POST.get("is_featured") == "true"

    # Validate required fields
    if not name or not description or not category:
        return JsonResponse({'error': 'Name, description, and category are required'}, status=400)

    # Create new product
    new_product = Product(
        name=name, 
        description=description,
        category=category,
        thumbnail=thumbnail if thumbnail else None,
        price=int(price) if price else 0,  
        user=user,
        is_featured=is_featured,
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Check if user owns this product
    if product.user != request.user:
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    
    product.delete()
    return HttpResponse(b"DELETED", status=200)

@csrf_exempt
@require_POST
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Check if user owns this product
    if product.user != request.user:
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    
    # Get data from POST
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    price = request.POST.get("price")
    is_featured= request.POST.get("is_featured") == "true",
    
    # Update product
    product.name = name
    product.description = description
    product.category = category
    product.thumbnail = thumbnail if thumbnail else None
    product.price = int(price) if price else 0
    product.is_featured = is_featured
    product.save()
    
    return HttpResponse(b"UPDATED", status=200)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        # Check if it's AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'status': True,
                    'message': 'Login successful!',
                    'redirect': reverse('main:show_main')
                }, status=200)
            else:
                return JsonResponse({
                    'status': False,
                    'message': 'Invalid username or password.'
                }, status=401)
        else:
            # Regular form submission
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)

@csrf_exempt
def register(request):
    if request.method == "POST":
        # Check if it's AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            # Validation
            if password1 != password2:
                return JsonResponse({
                    'status': False,
                    'message': 'Password tidak sama.'
                }, status=400)
            
            if len(password1) < 8:
                return JsonResponse({
                    'status': False,
                    'message': 'Password harus minimal 8 karakter.'
                }, status=400)
            
            # Check if username exists
            from django.contrib.auth.models import User
            if User.objects.filter(username=username).exists():
                return JsonResponse({
                    'status': False,
                    'message': 'Username sudah digunakan.'
                }, status=400)
            
            # Create user
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password1
                )
                user.save()
                return JsonResponse({
                    'status': True,
                    'message': 'Akun berhasil dibuat!',
                    'redirect': reverse('main:login')
                }, status=200)
            except Exception as e:
                return JsonResponse({
                    'status': False,
                    'message': f'Terjadi kesalahan: {str(e)}'
                }, status=400)
        else:
            # Regular form submission (fallback)
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)

def show_xml_by_id(request, product_id):
   try:
        Product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", Product_item)
        return HttpResponse(xml_data, description_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'views': product.views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_product_hot': product.is_product_hot,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def show_json(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "my":
        if request.user.is_authenticated:
            product_list = Product.objects.filter(user=request.user)
        else:
            return JsonResponse([], safe=False)
    else:
        product_list = Product.objects.all()

    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'views': product.views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'price': product.price,
            'is_product_hot': product.is_product_hot,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else None
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)


def show_xml(request):
     Product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", Product_list)
     return HttpResponse(xml_data, description_type="application/xml")

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        Product_list = Product.objects.all()
    else:
        Product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406423282',
        'name': 'Keira Nuzahra Anjani',
        'class': 'PBP D',
        'product_list': Product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        Product_entry = form.save(commit = False)
        Product_entry.user = request.user
        Product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)