from django.shortcuts import redirect, render
from .models import Variant, product,guestcostumer,OrderItem,Orders
from django.http import JsonResponse, request
from .forms import getemail
import json
import datetime
from django.core.mail import EmailMultiAlternatives
from .filters import searchfilter


# Create your views here.
def index(request):
    list_product = product.objects.all()
    filtred_prod = []
    search_filter = searchfilter(request.GET)
    for prod in list_product:
        if prod in search_filter.qs:
            filtred_prod.append(prod)
    try:
        device_ID= request.COOKIES['device']
    except:
        device_ID=''
    costumer , created = guestcostumer.objects.get_or_create(device_id=device_ID)
    try:
        order = Orders.objects.get(complete=False,costumer=costumer)
        total_price = order.getCart_total
        items = order.orderitem_set.all()
    except:
        total_price = 0
        items = []
    print(device_ID)
    context = {
        'list_product':filtred_prod,
        'items':items,
        'total_price':total_price,
        'search_filter':search_filter,
    }

    return render(request,'product/shop (2).html',context)


from django.views.decorators.csrf import csrf_protect

@csrf_protect
def updateItem(request):
    try:
        device_ID= request.COOKIES['device']
    except:
        device_ID=''
    data = json.loads(request.body)
    productID = data['productId']
    action = data['action']
    print('action :',action)
    print('id : ', productID)
    Product = product.objects.get(id=productID)
    costumer , created = guestcostumer.objects.get_or_create(device_id=device_ID)
    order , created = Orders.objects.get_or_create(costumer=costumer,complete=False)
    item , created = OrderItem.objects.get_or_create(product=Product,Order=order)
    if (action=='add'):
        quantity = data['quantity']
        print('quantity: ',quantity)
        item.quantity += int(quantity)
        item.save()
    else:
        item.delete()
    return JsonResponse('Item was added', safe=False)

def checkout(request):
    try:
        device_ID= request.COOKIES['device']
    except:
        device_ID=''
    costumer , created = guestcostumer.objects.get_or_create(device_id=device_ID)
    try:
        order = Orders.objects.get(complete=False,costumer=costumer)
        total_price = order.getCart_total
        items = order.orderitem_set.all()
    except:
        order = Orders.objects.get(complete=False,costumer=costumer)
        total_price = 0
        items = []
    print(costumer.email_costumer)
    getemailform = getemail(instance=costumer)
    if request.method == 'POST':
        getemailform= getemail(request.POST,instance=costumer)
        if getemailform.is_valid():
            getemailform.save()
            order.transaction_id = str(costumer.id)+'HQOSJX23JSKIQ'+str(order.id)+str(datetime.datetime.now().day)
            order.complete = True
            order.save()
            return redirect('/transaction_ended_'+order.transaction_id)
    context = {
        'items':items,
        'total_price':total_price,
        'getemailform':getemailform,


    }
    return render(request,'product/checkout.html',context)


def sendorder(request,transaction_id):
    id = transaction_id
    print(datetime.datetime.now().strftime("%d. %B %Y"))
    try:
        device_ID= request.COOKIES['device']
    except:
        device_ID=''
    costumer , created = guestcostumer.objects.get_or_create(device_id=device_ID)
    try:
        order = Orders.objects.get(transaction_id=id)
        total_price = order.getCart_total
        items = order.orderitem_set.all()
    except:
        total_price = 0
        items = []
    subject, from_email, to = 'there is an order!', 'hamzatestsmtp@gmail.com', 'hamzabensmina2002@gmail.com'
    text_content = 'This is an important message.'
    html_file1= open('index/msg_text/_txt1.txt', "r")
    html_file1_5_2= open('index/msg_text/_txt1_5_2.txt', "r")
    html_file2= open('index/msg_text/_txt2.txt', "r")
    html_file3= open('index/msg_text/_txt3.txt', "r")
    html_file3_0= open('index/msg_text/_txt3_0.txt', "r")
    html_file4 = open('index/msg_text/_txt4.txt', "r")
    html_file5= open('index/msg_text/_txt5.txt', "r")
    html_file6 = open('index/msg_text/_txt6.txt', "r")
    html_file7 = open('index/msg_text/_txt7.txt', "r")
    html_items = ''
    txt1 =  html_file3_0.read()
    txt2 = html_file3.read()
    txt3 = html_file4.read()

    for item in items:
        html_items += txt1 + item.product.PRDName + txt2 + str(item.quantity) + txt3 + str(item.getTotal) + '</span>		</td></tr>'
    html_content = html_file1.read() + order.transaction_id + html_file1_5_2.read() + order.transaction_id + '] (' + str(datetime.datetime.now().strftime("%d. %B %Y")) + html_file2.read() + html_items + html_file5.read() + str(total_price) + html_file6.read() + costumer.email_costumer + html_file7.read()
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg_user = EmailMultiAlternatives(subject, text_content, from_email, [costumer.email_costumer])
    msg.attach_alternative(html_content, "text/html")
    msg_user.attach_alternative(html_content, "text/html")
    msg.send()
    msg_user.send()
    return redirect('/order_confirmation_'+order.transaction_id)

def thankYou(request,transaction_id):
    total_price = 0
    items = []
    id = transaction_id
    context= {
        'total_price':total_price,
        'items':items,
        'id':id,
    }
    return render(request,'product/thankYou.html',context)