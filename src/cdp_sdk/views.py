from typing import Optional

from rest_framework.decorators import api_view, permission_classes
# https://www.django-rest-framework.org/api-guide/permissions/#allowany
from rest_framework.permissions import AllowAny

from django.http.request import QueryDict
from django.http import JsonResponse
from django.conf import settings

from .tracking import Tracker


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
        team_code = settings.CDP_TEAM_CODE
    except:
        team_code = ''

    try:
        ds_id = settings.CDP_DS_ID
    except:
        ds_id = ''

    return Tracker(team_code, ds_id, relay_url, cerem_url)


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


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def record_view_event(request, format=None, *args, **kwargs):

    if request.method == 'GET':

        data = querydict_to_dict(request.GET)

    elif request.method == 'POST':

        data = querydict_to_dict(request.data)

    tracker = get_tracker()

    if tracker.team_code == '':
        return JsonResponse({'result': False, 'cid': ''})

    if 'tc' not in data:
        return JsonResponse({'result': False, 'cid': ''})

    if tracker.team_code != data['tc']:
        return JsonResponse({'result': False, 'cid': ''})

    result, cid = tracker.view_event(**data)

    return JsonResponse({'result': result, 'cid': cid})


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def record_click_event(request, format=None, *args, **kwargs):

    if request.method == 'GET':

        data = querydict_to_dict(request.GET)

    elif request.method == 'POST':

        data = querydict_to_dict(request.data)

    tracker = get_tracker()

    if tracker.team_code == '':
        return JsonResponse({'result': False, 'cid': ''})

    if 'tc' not in data:
        return JsonResponse({'result': False, 'cid': ''})

    if tracker.team_code != data['tc']:
        return JsonResponse({'result': False, 'cid': ''})

    result, cid = tracker.click_event(**data)

    return JsonResponse({'result': result, 'cid': cid})
