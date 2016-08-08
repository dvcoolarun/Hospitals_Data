from django.shortcuts import render
from django.http import HttpResponse

import requests
import json
# Create your views here.


def index(request):
    json_response = []
    for i in range(30):
        response = requests.get(
            'https://data.gov.in/api/datastore/resource.json?resource_id=e16c75b6-7ee6-4ade-8e1f-2cd3043ff4c9&api-key=698a0e2b2e576da34fde0d6533d8fdf9' + '&offset=' + str(i))

        json_response.append(response.json()['records'])
    # return HttpResponse(json_response)

    nec_info = {}
    parseData = []
    for each_dict in json_response:
        for each_item in each_dict:
            nec_info['District'] = each_item['district']
            nec_info['Address'] = each_item['address']
            nec_info['Hospital'] = each_item['h_name']
            nec_info['State'] = each_item['state']
            nec_info['Contact'] = each_item['contact']
            nec_info['id'] = each_item['f_id']
        parseData.append(nec_info)
        return render(request, 'app/index.html', {'data': parseData})
