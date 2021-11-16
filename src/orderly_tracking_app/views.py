from typing import Optional

from rest_framework.decorators import api_view
from django.http.request import QueryDict
from orderly_tracking.tracking import Tracker
from django.conf import settings

def get_tracker():
    try:
        cerem_url = settings.CEREM_API_URL
    except:
        cerem_url = 'localhost'

    try:
        relay_url = settings.RELAY_URL
    except:
        relay_url = 'localhost'

    try:
        team_code = settings.ORDERLY_TEAM_CODE
    except:
        team_code = ''

    return Tracker(team_code, relay_url, cerem_url)

@api_view(['GET', 'POST'])
def record_view_event(request, format=None, *args, **kwargs):
    data = querydict_to_dict(request.data)
    tracker = Tracker()
    tracker.view_event(**data)

@api_view(['GET', 'POST'])
def record_click_event(request, format=None, *args, **kwargs):
    data = querydict_to_dict(request.data)
    tracker = Tracker()
    tracker.click_event(**data)

def querydict_to_dict(data):

    if isinstance(data, QueryDict) is True:
        as_dict = dict(data)
    elif isinstance(data, dict) is True:
        as_dict = data
    else:
        return data

    key_values = {}
    for key in as_dict:

        values = as_dict[key]

        if '[]' in key:
            # this is a list, so keep it's original type
            key = key.replace('[]', '')
            key_values[key] = values
        else:

            if isinstance(values, list) is True:
                if len(values) > 1:
                    key_values[key] = values
                elif len(values) == 1:
                    key_values[key] = values[0]
                else:
                    key_values[key] = values

            else:
                key_values[key] = values

    return key_values
