from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import requests
import json


def index(request):
    json_response = []
    for i in range(30):
        response = requests.get(
            'https://data.gov.in/api/datastore/resource.json?resource_id=e16c75b6-7ee6-4ade-8e1f-2cd3043ff4c9&api-key=' + settings.API_KEY + '&offset=' + str(i))
        json_response.append(response.json()['records'])

    parseData = []
    spec_info = {}
    for each_dict in json_response:
        for each_item in each_dict:
            spec_info['District'] = each_item['district']
            spec_info['Address'] = each_item['address']
            spec_info['Hospital'] = each_item['h_name']
            spec_info['State'] = each_item['state']
            spec_info['Contact'] = each_item['contact']
            spec_info['id'] = each_item['f_id']
        parseData.append(spec_info)
    return render(request, 'app/index.html', {'data': parseData})
