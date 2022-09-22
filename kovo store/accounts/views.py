from django.db.models.expressions import Value
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from .models import Email, Profile
from django.contrib.auth import login,authenticate
from .forms import Emailsform, userchange, userform , profileform
from django.contrib import messages
from django.contrib.auth import logout,authenticate, login
from product.views import allitem
from product.tests import checkCol
from product.models import Orders
# Create your views here.


def signup(request):
    err = False
    if request.method =='POST':
        form = userform(request.POST)
        if form.is_valid() :
            form.save()
            user = form.cleaned_data.get('username')
            err = False
            return redirect('login')
        else: 
            err = True
    else:
        form = userform()
    context = {
        'err':err,
        'form':form
    }
    return render(request, 'registration/signup.html', context)

def loginuser(request):
    err = False
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            err = False
            i = 1
            return redirect('/home/')
        else:
           err = True
        
    print(err)
    context= {'err':err,}
    return render(request, 'login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')


def Profile_detail(request,slug,col):
    profile= get_object_or_404(Profile, slug=slug)
    orders_inordred = Orders.objects.filter(Profile = profile)
    orders = []
    for order in orders_inordred :
        if len(orders) < 6:
            orders.insert(0,order)
        else:
            orders.pop(5)
            orders.insert(0,order)
    user_Edit=userform(instance=profile.user)
    Col_active = checkCol(col)
    try:
        eml = Email.objects.get(costumer = profile)
    except Email.DoesNotExist :
        eml = Email.objects.create(costumer=profile)
    Email_add = Emailsform()
    if request.method == 'POST':
        Email_add = Emailsform(request.POST , instance=eml)
        if Email_add.is_valid():
            Email_add.save()
    if request.method == 'POST':
        user_Edit = userchange(request.POST , instance=profile.user)
        if user_Edit.is_valid():
            user_Edit.save()
            messages.success(request,'sequrity setting edited succesfully')
    profile_Edit = profileform(instance=profile)
    if request.method == 'POST':
        profile_Edit = profileform(request.POST , instance=profile)
        if profile_Edit.is_valid():
            profile_Edit.save()
            messages.success(request,'profile edited succesfully')
    context = {
        'profile':profile,
        'profile_Edit':profile_Edit,
        'user_Edit':user_Edit,
        'Col_active':Col_active,
        'orders':orders,
        'Emailform':Email_add,
        # 'password_Edit':password_Edit,
    }
    allitem(context,request)
    return render(request,'registration/profile.html',context)