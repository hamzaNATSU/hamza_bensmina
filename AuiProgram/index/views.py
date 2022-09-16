from curses.ascii import RS
from datetime import timedelta
from multiprocessing import context
from operator import truediv
from django.forms import DurationField
from django.shortcuts import redirect, render
from .models import *
from .filter import searchfilter
import time
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
# Create your views here.
# define the countdown func.
from_email = "hamzanatsu2020@gmail.com"



import threading
lastreserv = []
def printit():
    threading.Timer(5.3, printit).start()
    lastreserv_p = Reservation.objects.filter(DateExp__lt = datetime.datetime.now(tz=timezone.utc),Ended=False)
    smail = email.objects.all()[email.objects.all().count()-1]
    lastreserv.clear()
    for el in lastreserv_p:
        text_content = "Reservation Ended for student <<"+el.NameStud + ">> check details here :  http://127.0.0.1:8000/Reservation_"+str(el.id)+"_Details_detials"
        msg = EmailMultiAlternatives('AUI Res', text_content, from_email, [smail.Eemail])
        msg.send()
        lastreserv.append(el)
        el.Ended = True
        el.save()

printit()
def countdown(t):
    
    while t:
        hours = divmod(t , 3600)
        mins, secs = divmod(t, 60)
        if (mins > 59):
            mins = mins%60
        timer = '{:02d}:{:02d}:{:02d}'.format(hours[0],mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1
    return(timer)

def checkdevices():
    print('hi')
    for dev in Device.objects.all():
        try :
            res = Reservation.objects.filter(Device_id = dev.id,Ended=False)
            if res.count() == 0:
                dev.Reserved = False
                dev.save()
        except Reservation.DoesNotExist :
            print('yes')
            dev.Reserved = False
            dev.save()



def index(request):
    search_filter = searchfilter(request.GET)
    filtred_Res = []
    if request.method == 'POST':
        is_filter = True
        order_type = request.POST.get('order_type')
        if order_type == 'exp':
            Reservations = Reservation.objects.all().order_by('-DateExp')
            for prod in Reservations:
                if prod in search_filter.qs:
                    filtred_Res.append(prod)
        elif order_type == 'expDes':
            Reservations = Reservation.objects.all().order_by('DateExp')
            for prod in Reservations:
                if prod in search_filter.qs:
                    filtred_Res.append(prod)
        elif order_type == 'Res':
            Reservations = Reservation.objects.all().order_by('-DateRes')
            for prod in Reservations:
                if prod in search_filter.qs:
                    filtred_Res.append(prod)
        elif order_type == 'ResDes':
            Reservations = Reservation.objects.all().order_by('DateRes')
            for prod in Reservations:
                if prod in search_filter.qs:
                    filtred_Res.append(prod)
        elif order_type == 'Name':
            Reservations = Reservation.objects.all().order_by('NameStud')
            for prod in Reservations:
                if prod in search_filter.qs:
                    filtred_Res.append(prod)
        elif order_type == 'NameDes':
            Reservations = Reservation.objects.all().order_by('-NameStud')
            for prod in Reservations:
                if prod in search_filter.qs:
                    filtred_Res.append(prod)
    else:
        order_type = ''
        is_filter = False
        Reservations = Reservation.objects.all().order_by('-DateExp')
        for prod in Reservations:
            if prod in search_filter.qs:
                filtred_Res.append(prod)                              
    devices = Device.objects.all()
    counter_expd = Reservation.objects.filter(DateExp__lt = datetime.datetime.now()).count()
    counter_dev = Device.objects.filter(Reserved = False).count()
    counter_dev2 = Device.objects.filter(Reserved = True).count()
    checkdevices()
    context = {
        'lastreserv' : lastreserv, 
        'order_type':order_type,
        'isfilter':is_filter,
        'search_filter':search_filter,
        'Res':filtred_Res,
        'Dev':devices,
        'counter_expd':counter_expd,
        'counter_dev2':counter_dev2,
        'counter_dev':counter_dev,
    }
    return render(request,'pages/index.html',context)


def Reserve(request):
    devicess = Device.objects.filter(Reserved = False)
    checkdevices()
    context = {
        'devicess':devicess,
    }
    if request.method == 'POST':
        id = request.POST.get('ID')
        name = request.POST.get('this_name')
        Devicee = request.POST.get('select_1')
        duration = request.POST.get('Duration')
        print(duration)
        Res = Reservation.objects.create(IDStud=id,NameStud=name,Device=Device.objects.get(IDDev=Devicee))
        Res.DateExp = datetime.datetime.strptime(duration+' '+str(datetime.datetime.now().hour)+':'+str(datetime.datetime.now().minute)+':'+str(datetime.datetime.now().second) ,"%Y-%m-%d %H:%M:%S")
        print('this is : ')
        print(Res.DateExp)
        Res.save()
        return redirect('aui:index')
    return render(request,'pages/form1.html',context)


def AddDevice(request):
    checkdevices()
    if request.method == 'POST':
        id = request.POST.get('id')
        Brand = request.POST.get('Brand')
        SerNum = request.POST.get('SerNum')
        type = request.POST.get('type')
        Dev = Device.objects.create()
        Dev.IDDev=id
        Dev.brand=Brand
        Dev.SerialDev=SerNum
        Dev.typeDev=type
        Dev.save()
        return redirect('aui:index')
    return render(request,'pages/form2.html')

import humanize

def ResDetails(request,id,type):
    Reser = Reservation.objects.get(id=id)
    timeleft =  datetime.datetime.now(datetime.timezone.utc) - Reser.DateRes + timedelta(minutes=59)
    timeleft = humanize.naturaltime(timeleft)
    if request.method == 'POST':
        Reser.Ended = True
        print('ended')
        Reser.Device.Reserved = False
        Reser.Device.save()
        Reser.save()
        return redirect('aui:index')
        
    context={
        'type':type,
        'Reser':Reser,
        'timeleft':timeleft}
    return render(request,'pages/Details.html',context)

def updatealerts(request):
    context={
         'lastreserv' : lastreserv,
    }
    return render(request,'pages/script.html',context)



def changeemail(request):
    alert = False
    confirmation_sent = False
    smail = email.objects.all()[email.objects.all().count()-1]
    if request.method == 'POST':
        string = request.POST.get("email")
        password = request.POST.get("password")
        print(string)
        print(password)
        if password == "Passw0rd":
            confirmation_sent = True
            alert = False
            text_content = "confirm your email :  http://127.0.0.1:8000/confirmation_"+string
            msg = EmailMultiAlternatives('AUI Res', text_content, from_email, [string])
            msg.send()
        else:
            
            alert = True
            confirmation_sent = False
    context = {
        'email':smail.Eemail,
        'sent':confirmation_sent,
        'alert':alert,
    }
    return render(request,'pages/email_change.html',context)
    

def confirmmail(request,mail):
    smail = email.objects.create(Eemail=mail)

    return render(request,'pages/email_confirmed.html')