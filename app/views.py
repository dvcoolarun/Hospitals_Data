from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import requests
import json


def index(request):
    hospitals_list = []
    for i in range(30):
        response = requests.get(
            'https://data.gov.in/api/datastore/resource.json?resource_id=e16c75b6-7ee6-4ade-8e1f-2cd3043ff4c9&api-key=' + settings.API_KEY + '&offset=' + str(i))
        hospitals_list.append(response.json()['records'])

    parseData = []
    for list_counter in range(len(hospitals_list)):
        for each_list in hospitals_list:
            for each_dict in each_list:
                parseData.append(each_dict)
        return render(request, 'app/index.html', {'data': parseData})
