from email.policy import SMTP
from functools import cmp_to_key
import stripe
from django.contrib import messages
from django.db.models.lookups import IsNull
from django.shortcuts import redirect, render
from django_filters.filters import RangeFilter
from .models import OrderItem, Orders, PRD_Cat, PRD_Img, PrdFvt, PrdRvd, product ,Deal, shippingAdress
from settings.models import Collection, Variant , brand
from datetime import datetime,timedelta
from django.shortcuts import get_object_or_404
from .filters import productFilter,searchfilter,brandfilter
from django.core.paginator import Paginator
from django.http import JsonResponse, request
import json
from accounts.models import Email,Profile
from accounts.forms import Emailsform
from django.contrib.auth.models import User
from .forms import orderAdressForm,VariantForm,cantactForm
from django.core.mail import send_mail
from email.message import EmailMessage
from .tests import checkCat , items_to_html


# Create your views here.


def allitem(context,request):
    Cat_list=PRD_Cat.objects.all()
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        rvds = []
        rvds2 = PrdRvd.objects.filter(costumer=profile)
        for rvd in rvds2 :
            if len(rvds) < 3:
                rvds.append(rvd)
            else:
                rvds.pop(0)
                rvds.append(rvd)
        try:
            FVRT2 = PrdFvt.objects.filter(costumer= profile)
            FVRT = []
            for product in FVRT2:
                FVRT.append(product.Product)
        except PrdFvt.DoesNotExist:
            FVRT = []
        try:
            eml = Email.objects.get(costumer= profile)
        except Email.DoesNotExist :
            eml = Email.objects.create(costumer=profile)
        Email_add = Emailsform()
        if request.method == 'POST':
            Email_add = Emailsform(request.POST , instance=eml)
        if Email_add.is_valid():
            Email_add.save()
        try:
            order = Orders.objects.get(Profile=profile, complete=False)
        except Orders.DoesNotExist :
            order = None
        try:
            wishlist = PrdFvt.objects.filter(costumer=profile)
        except PrdFvt.DoesNotExist:
            wishlist = None
        print(FVRT)
        context['order']=order
        context['wishlist']=wishlist
        context['Email_add']=Email_add
        context['eml']=eml
        context['FVRT']=FVRT
        context['rvds']=rvds
    context['Cat_list']=Cat_list


def product_list(request):
    deal=Deal.objects.order_by('-id')[0]
    product_list=product.objects.all().order_by('-id')
    Cat_list=PRD_Cat.objects.all()
    Parent = PRD_Cat.objects.filter(PRDCat_Parent__isnull = True)
    Cat_Sec=[]
    Product_new=product.objects.all()[:8]
    for Cat2 in Parent: 
        for Cat in Cat_list:
            if Cat.PRDCat_Parent == Cat2:
                Cat_Sec.append(Cat)
    newest_collections= Collection.objects.all()[3:]
    all_collections= Collection.objects.all()[4:]
    context={
        'product_list' : product_list,
         'all_collections': all_collections,
        'newest_collections': newest_collections,
        'Parent': Parent,
        'Cat_Sec': Cat_Sec,
        'deal':deal,
        'Product_new':Product_new,
    }
    allitem(context, request)
    return render(request,'product/index.html' ,context)

def productfilter(request, Cat):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
    Cat_active = checkCat(Cat)
    product_filter = productFilter(request.GET)
    search_filter = searchfilter(request.GET)
    brand_filter = brandfilter(request.GET)
    brand_filtred = brand_filter.qs
    brands=brand.objects.all()
    Parent = PRD_Cat.objects.filter(PRDCat_Parent__isnull = True)
    Cat_list=PRD_Cat.objects.all()
    Cat_Sec=[]
    product_list=[]
    product_list_all=[]
    for Cat2 in Parent: 
        for Cat in Cat_list:
            if Cat.PRDCat_Parent == Cat2:
                Cat_Sec.append(Cat)
    for prd in product.objects.all():
        if prd in product_filter.qs :   
            if prd in brand_filter.qs:
                if prd in search_filter.qs:
                    product_list_all.append(prd)
    for prd in product.objects.all():
        if prd in product_filter.qs :     
            if prd in brand_filter.qs:
                if prd in brand_filter.qs:
                    if prd.PRDCat.PRDCat_Parent == Cat:
                        product_list.append(prd)
    product_count = len(product.objects.all())
    product_count2 = 0
    paginator = Paginator(product_list, 9)
    paginator_all = Paginator(product_list_all, 9)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    product_list_all = paginator_all.get_page(page_number)
    context={
    'product_filter':product_filter,
    'product_list':product_list,
    'Parent': Parent,
    'Cat_Sec':Cat_Sec,
    'Cat_active':Cat_active,
    'search_filter':search_filter, 
    'brand_filter':brand_filter,
    'brand_filtred':brand_filtred,
    'product_list_all':product_list_all,
    'product_count':product_count,
    'product_count2':product_count2,
   }
    allitem(context,request)
    return render(request,'product/shop.html', context )


def product_detail(request , id):
    Product_detail= get_object_or_404(product, id=id)
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        try:
            order = Orders.objects.get(Profile=profile, complete=False)
            try:
                items= OrderItem.objects.get(product=Product_detail, Order= order)    
            except OrderItem.DoesNotExist:
                items = None
        except Orders.DoesNotExist:
            order = None
            items = None
        variants = Variant.objects.all()
        try:
            rvd = PrdRvd.objects.get(costumer=profile,Product=Product_detail)
            rvd.delete()
            rvd , created = PrdRvd.objects.get_or_create(costumer= profile , Product = Product_detail)
        except:
            rvd , created = PrdRvd.objects.get_or_create(costumer= profile , Product = Product_detail)
    else :
        order = None
        items = None
        rvd = []
        variants = Variant.objects.all()

    try:
        PRDImgs = PRD_Img.objects.get(PRDSelected_id=id)
    except PRD_Img.DoesNotExist:
        PRDImgs = None
    pass
    Cat_list=PRD_Cat.objects.all()
    Product_new=product.objects.all()[:8]

    
    context= {
        'Product_detail': Product_detail,
        'PRDImgs':PRDImgs,
        'Product_new':Product_new,
        'items':items,
        'rvd':rvd,
        'variants':variants,
    }
    allitem(context,request)
    return render(request, 'product/product_detail.html', context)


from django.views.decorators.csrf import csrf_protect

@csrf_protect
def updateItem(request):
    data = json.loads(request.body)
    productID = data['productId']
    action = data['action']
    try:
        variant = data['variant']
        vrt = Variant.objects.get(id = variant)
    except :
        variant=None
        vrt = None
    print('variant: ', variant)
    print('action :',action)
    print('id : ', productID)
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        Product = product.objects.get(id=productID)
        order , created = Orders.objects.get_or_create(Profile=profile, complete=False)
        orderitem , created = OrderItem.objects.get_or_create(Order=order,product=Product)
        if vrt != None:
            orderitem.Variant = vrt
    if action=='add':
        orderitem.quantity = (orderitem.quantity + 1 )
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1 )
    elif action == 'removeAT':
        orderitem.quantity = 0
    elif action == 'removeATFAV':
        FVRT = PrdFvt.objects.filter(costumer = profile)
        for fvrt in FVRT:
            fvrt.delete()
    elif action == 'favorite':
        FVRT, created = PrdFvt.objects.get_or_create(costumer = profile , Product = Product)
    elif action == 'defavorite':
        FVRT = PrdFvt.objects.get(costumer = profile , Product = Product)
        FVRT.delete()
    orderitem.save()
    if orderitem.quantity <= 0 :
        orderitem.delete() 

    return JsonResponse('Item was added', safe=False)

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def Cart(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        try:
            order = Orders.objects.get(Profile=profile, complete=False)
            items = order.orderitem_set.all()
        except Orders.DoesNotExist:
            order = {
            'getCart_total': 0,
            'getdelivery':0,
            'get_total':0,
        
        }
            items=[]
    else:
        items = []
        order = {
            'getCart_total': 0,
            'getdelivery':0,
            'get_total':0,
        
        }
    context={
        'items':items,
    }
    allitem(context,request)
    return render(request,'product/Cart.html', context)



@csrf_protect
def checkout(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        order , created = Orders.objects.get_or_create(Profile=profile, complete=False)
        shippingadres , created = shippingAdress.objects.get_or_create(costumer=profile, order=order)
        items = order.orderitem_set.all()
        addressForm = orderAdressForm(instance=shippingadres)
        warn = False
        if request.method == 'POST':
            addressForm = orderAdressForm(request.POST , instance=shippingadres)
            if addressForm.is_valid():
                addressForm.save()
                return redirect('pay:payment')
            else:
                warn = True
                # if addressForm.IsDefault == True:
                #     profile.country = addressForm.country
                #     profile.phone = addressForm.phone
                #     profile.fullname = addressForm.Fullname

    else:
        items = []
        order = {
            'getCart_total': 0,
            'getdelivery':0,
            'get_total':0,
        }
    context={
       'items':items,
       'addressForm':addressForm,
       'profile':profile,
       'warning':warn,
    }
    allitem(context,request)
    return render(request,'product/checkout.html',context)


stripe.api_key = 'sk_test_51J6aEFJ3i0GkFvuykbqbvMTpf3rd09N3fakHXtZGTj8xD7XtpCaiVduO1WblC3JrHJYMEhrkAnZC68frxLIaPJEg004R6FJijE'

def checkout_2(request):
    if request.user.is_authenticated: 
        return redirect('order_proccess')
    else:
        return redirect('home:index')

from django.core.mail import EmailMultiAlternatives
def orderprocess(request,transaction_id):
    profile = Profile.objects.get(user=request.user)
    order =  get_object_or_404(Orders , transaction_id=transaction_id)
    items = order.orderitem_set.all()
    shippingadres= shippingAdress.objects.get(costumer=profile, order=order)
    order.complete = True
    subject, from_email, to = 'there is an order!', 'hamzatestsmtp@gmail.com', 'hamzabensmina2002@gmail.com'
    text_content = 'This is an important message.'
    html_file1,html_file1_user= open('product/msg_text/_txt1.txt', "r"),open('product/msg_text/_txt1.txt', "r")
    html_file1_5,html_file1_5_user= open('product/msg_text/_txt1_5.txt', "r"),open('product/msg_text/_txt1_5.txt', "r")
    html_file2,html_file2_user= open('product/msg_text/_txt2.txt', "r"),open('product/msg_text/_txt2.txt', "r")
    html_file3, html_file3_user= open('product/msg_text/_txt3.txt', "r"),open('product/msg_text/_txt3.txt', "r")
    html_file4,html_file4_user = open('product/msg_text/_txt4.txt', "r"),open('product/msg_text/_txt4.txt', "r")
    html_file5 ,html_file5_user = open('product/msg_text/_txt5.txt', "r"),open('product/msg_text/_txt5.txt', "r")
    html_file6,html_file6_user = open('product/msg_text/_txt6.txt', "r"),open('product/msg_text/_txt6.txt', "r")
    html_content_user = html_file1.read()+'kovo store'+'</h2>Thanks for your order N° : #'+str(order.transaction_id) +'</h2>' + html_file1_5.read() + items_to_html(order) + html_file2.read() +'$'+ str(order.get_total) + html_file3.read() + shippingadres.address + str(shippingadres.city) +'|'+ str(shippingadres.country) +'|'+ str(shippingadres.ZipCode) + '<br> <bold> phone number : </bold>' + str(shippingadres.phone) + html_file4.read() + str(order.dateOrdered) + html_file5.read() + str(order.paiment_type) + html_file6.read()
    html_content = html_file1_user.read()+str(profile.user)+'</h2> <br> <h3> order N° : #'+str(order.transaction_id) +'</h2>' + html_file1_5_user.read() + items_to_html(order) + html_file2_user.read() +'$'+ str(order.get_total) + html_file3_user.read() + shippingadres.address + str(shippingadres.city) +'|'+ str(shippingadres.country) +'|'+ str(shippingadres.ZipCode) + '<br> <bold> phone number : </bold>' + str(shippingadres.phone) + html_file4_user.read() + str(order.dateOrdered) + html_file5_user.read() + str(order.paiment_type) + html_file6_user.read() 
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg_user = EmailMultiAlternatives(subject, text_content, from_email, [profile.user.email])
    msg.attach_alternative(html_content, "text/html")
    msg_user.attach_alternative(html_content_user, "text/html")
    msg.send()
    msg_user.send()
    order.save()
    redirect('home:index')
    return redirect('home:index')

def msginfos(request):
    profile = Profile.objects.get(user=request.user)
    order , created = Orders.objects.get_or_create(Profile=profile, complete=False)
    context={
        'order':order,
        'profile':profile,

    }
    return render(request,'product/msg.html',context)


def favorites(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        FVRT = PrdFvt.objects.filter(costumer = profile)
    else: 
        FVRT = []
    context= {
        'FVRT' :FVRT
    }
    
    allitem(context,request)
    return render(request,'product/wishlist.html',context)


def cantact_us(request):
    cantactform = cantactForm()
    if request.method == 'POST':
        cantactform = cantactForm(request.POST)
        feedback =  request.POST.get('feedback')
        fullname =  request.POST.get('fullname')
        Email =  request.POST.get('Email')
        subject, from_email, to = 'feedback', Email, 'hamzabensmina2002@gmail.com'
        text_content =  'feedback'
        html_content = '<h2> full name : '+ fullname +'</h2><br><p>' + feedback +'</p>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        redirect('/home/')
    return render(request,'product/cantacts.html',context={'cantactform':cantactform})

def about_us(request):
    return render (request,'product/about_us.html')