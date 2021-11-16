from typing import Optional

from rest_framework.decorators import api_view

from orderly_tracking.tracking import Tracker

@api_view(['GET', 'POST'])
def record_view_event(request, version: str, url: str, title: str, target: str,
        language: str = 'zh-tw', cid: Optional[str] = None, decode_format: str = '',
        sd: str = '', sr: str = '', did: str = '', view_port_size: str = ''):
    tracker = Tracker()
    tracker.view_event(
        version=version, url=url, title=title, target=target,
        language=language, cid=cid, decode_format=decode_format, sd=sd,
        sr=sr, did=did, view_port_size=view_port_size
    )

@api_view(['GET', 'POST'])
def record_click_event(request, version: str, url: str, title: str, target: str,
        language: str = 'zh-tw', cid: Optional[str] = None, decode_format: str = '',
        sd: str = '', sr: str = '', did: str = '', view_port_size: str = ''):
    tracker = Tracker()
    tracker.click_event(
        version=version, url=url, title=title, target=target,
        language=language, cid=cid, decode_format=decode_format, sd=sd,
        sr=sr, did=did, view_port_size=view_port_size
    )
