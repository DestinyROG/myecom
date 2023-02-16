from django.shortcuts import render,redirect
from NewApp.models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'Store\Layout\home.html')

def Collections(request):
    ourCollections=Category.objects.all()
    context={
        'ourCollections':ourCollections,
    }
    return render(request, 'Store\Layout\collections.html',context)

def Collectionsview(request,name):
    if Category.objects.filter(urlname=name):
        category=Category.objects.all().get(urlname=name)
        products=Product.objects.all().filter(category=name)
        print(type(category))
        context={
            "products":products,
            'category':category,
        }
        # print(Product.objects.filter(category=name))
    return render(request,'Store\Layout\Product\product.html',context)


def Productview(request,cate,prod):
    if Product.objects.filter(category=cate,name=prod) and Category.objects.filter(urlname=cate):
        categoryname=Category.objects.get(urlname=cate)
        itemname=Product.objects.get(category=cate,name=prod)
        context={
            'itemname':itemname,
            'categoryname':categoryname,
        }
        return render(request,'Store\Layout\Product\productview.html', context)
    
def Add_to_cart(request,cate,name,qty):
    prod=Product.objects.all().get(category=cate,name=name)
    cart=Cart.objects.all()
    check=0
    if len(cart)==0:
        add=Cart(category=prod.category,name=prod.name,product_image=prod.product_image,price=prod.selling_price,quantity=qty)
        add.save()
    else:
        for i in cart:
            if i.name==name and i.category==cate:
                check+=1
            else:
                check+=0
        if check==1:
            for i in cart:
                if i.name==prod.name and i.category==prod.category:
                    i.quantity+=qty
                    i.save()
        else:
            add=Cart(category=prod.category,name=prod.name,product_image=prod.product_image,price=prod.selling_price,quantity=qty)
            add.save()
        
    return redirect(f"/collections/{cate}")

def Cartview(request):
    cart=Cart.objects.all()
    context={
        'cart':cart,
    }
    return render(request,'Store\Layout\cart.html',context=context)