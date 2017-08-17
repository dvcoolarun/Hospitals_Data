from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from app.models import bloodbankdata

import requests
import json


def index(request):
    parseData = bloodbankdata.objects.all().order_by('id')
    return render(request, 'app/index.html', {'data': parseData})
