from django.conf.urls import url
from django.shortcuts import redirect, render
import json
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse, request
from .models import book
import requests
from urllib import request as req
import urllib.request, urllib.error, urllib.parse
# Create your views here.

def showbooks(request):
    books = book.objects.all()
    for art in books : 
        art.description = art.description.split('Rating',1)[0]
        art.save()
    context = {
        'books':books,
    }
    return render(request,'index.html',context)

def extractdatafix(request):
    url = 'https://yofreesamples.com/courses/free-discounted-udemy-courses-list/'
    req = urllib.request.Request(url, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
    response = urllib.request.urlopen(req).read()
    webContent = response
    f = open('books/data/datatxt.html', 'wb')
    f.write(webContent)
    f.close()
    d = open('books/data/datatxt.html', 'r',encoding='utf-8')
    webContent = d.read().split('<ul')[2].split('</ul>')[0]
    d.close()
    context= {'html' : webContent}
    return render(request,'data.html',context)

@csrf_protect
def convertdata(request):
    book.objects.all().delete()
    data = json.loads(request.POST.get('data'))   
    for article in data : 
        book_art , created = book.objects.get_or_create(title = article['title'] , description=article['description'], image_url = article['img'], url=article['url'])
        book_art.get_image_from_url()
        book_art.image_url = book_art.image.url
        book_art.save()
    return redirect('home:index')
    return JsonResponse('home',safe=False)