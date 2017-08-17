from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from app.models import bloodbankdata

import requests
import json


class Command(BaseCommand):
    args = ''
    help = 'Export data to remote server'

    def handle(self, *args, **options):
        response = requests.get(
            'https://data.gov.in/api/datastore/resource.json?resource_id=e16c75b6-7ee6-4ade-8e1f-2cd3043ff4c9&api-key=' + settings.API_KEY)
        offset = int(response.json()['total_records']
                     ) / response.json()['count']

        hospitals_list = []

        for i in range(int(offset)):
            response = requests.get(
                'https://data.gov.in/api/datastore/resource.json?resource_id=e16c75b6-7ee6-4ade-8e1f-2cd3043ff4c9&api-key=' + settings.API_KEY + '&offset=' + str(i))
            hospitals_list.append(response.json()['records'])

        parse_list = []

        for each_list in hospitals_list:
            for each_dict in each_list:
                parse_list.append(each_dict)


        for each_dict in parse_list:
            bloodbankdata.objects.update_or_create(State=each_dict['state'], District=each_dict['district'], Hospital_name=each_dict['h_name'], Contact=each_dict['contact'], Address=each_dict['address'])
