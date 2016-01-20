from django.shortcuts import render
from django.http import HttpResponse
from .models import Redirect, ClickLog
import datetime

# Create your views here.


def redirect(request, short):
    client_ip = request.META['REMOTE_ADDR']

    try:
        obj = Redirect.objects.get(short=short)
    except:
        obj = None

    ClickLog.objects.create(url=obj, ip=client_ip)

    if obj:
        return render(request, 'redirect.html', {'target': obj.url})
    return render(request, 'redirect.html', {'target': 'http://www.gliacloud.com'})
