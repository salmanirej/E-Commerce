from django.shortcuts import render
from .models import Product 
 
from django.core.paginator import Paginator
# Create your views here.

def product_list(request):
    product_list= Product.objects.all()
    paginator = Paginator(product_list, 1)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"product_list":product_list,"page_obj":page_obj}
    return render( request, "product\product_list.html",context )

def product_detail(request,id):
    product_detail=Product.objects.get(id=id)
    context={"product_detail":product_detail}
    return render(request,"product/product_detail.html",context)