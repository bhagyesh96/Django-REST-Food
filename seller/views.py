from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
import json
from .api import serializers
# Create your views here.

def testview(request):
    r = requests.request('GET', 'http://127.0.0.1:8000/seller/api/sellerlist/').json()
    if r:
        return HttpResponse(r.username)
    else:
        return HttpResponse('Not')




