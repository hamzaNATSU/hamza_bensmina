from django.forms.widgets import Widget
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
import stripe
from stripe.api_resources import line_item
from stripe.api_resources.issuing import transaction
from accounts.models import Profile
from product.models import Orders,shippingAdress
from django.conf import settings
from product.views import allitem
from django.forms import BooleanField, CheckboxInput
# Create your views here.
import datetime

def HomePageView(request):
    profile = Profile.objects.get(user=request.user)
    order = Orders.objects.get(Profile=profile, complete=False)
    shippingadres = shippingAdress.objects.get(costumer=profile, order=order)
    items = order.orderitem_set.all()
    context={'shippingadres':shippingadres,
            'items':items,
    }
    allitem(context,request)
    return render(request,'checkout/checkout_2.html',context)


@csrf_exempt
def stripe_config(request):
    pass


# payments/views.py

@csrf_exempt
def create_checkout_session(request):
    domain_url = 'http://127.0.0.1:8000/'
    stripe.api_key = settings.STRIPE_SECRET_KEY
    profile = Profile.objects.get(user=request.user)
    order = Orders.objects.get(Profile=profile, complete=False)
    transaction_id= str(profile.id)+'8246729'+str(order.id)
    order.transaction_id = str(transaction_id)
    order.paiment_type = 'stripe'
    order.save()
    # print(order.transaction_id)
        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
    checkout_session = stripe.checkout.Session.create(
    success_url=domain_url + 'home/order_process_'+str(transaction_id),
    cancel_url=domain_url + 'cancelled/',
    payment_method_types=['card'],
    mode='payment',
    line_items=[
            {
                'name': 'order :'+str(order.id),
                'quantity': 1,
                'currency': 'USD',
                'amount': round(order.get_total)*100,                    }                ]
            )
    return JsonResponse({
            'publicKey':settings.STRIPE_PUBLIC_KEY,
            'sessionId': checkout_session['id']})
#! /usr/bin/env python3.6
"""
Python 3.6 or newer required.
"""
import json
import os
import stripe
# This is your real test secret API key.
stripe.api_key = "sk_test_51J7rnpCoVF7w6k3XG0StHaNYtOKFHBRuKCTFsDfEUmrSzy8mMMMo4Z89FrWukKdDcTuSuOIFKPkhSw83sgs3O2nt00ptIq97iP"

from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_folder=".",
            static_url_path="", template_folder=".")


def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 1400


@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        data = json.loads(request.data)
        intent = stripe.PaymentIntent.create(
            amount=calculate_order_amount(data['items']),
            currency='usd'
        )

        return jsonify({
          'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run()



def paypalpay(request):
    profile = Profile.objects.get(user=request.user)
    order = Orders.objects.get(Profile=profile, complete=False)
    transaction_id= str(profile.id)+'8246729'+str(order.id)
    order.transaction_id = str(transaction_id)
    order.paiment_type = 'paypal'
    order.save()
    return redirect ('/home/order_process_'+str(transaction_id))


def on_cash(request):
    profile = Profile.objects.get(user=request.user)
    order = Orders.objects.get(Profile=profile, complete=False)
    transaction_id= str(profile.id)+'8246729'+str(order.id)
    order.transaction_id = str(transaction_id)
    order.paiment_type = 'On Cash'
    order.save()
    return redirect ('/home/order_process_'+str(transaction_id))


def download(request):
    context = {}
    return render(request,'download.html',context)