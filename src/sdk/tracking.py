import requests
from typing import Optional


class Tracker:
    def __init__(self, team_code, ds_id, relay_url, cerem_url) -> None:
        self.team_code = team_code
        self.ds_id = ds_id
        self.relay_url = relay_url
        self.cerem_url = cerem_url

    def click_event(self, version: str, url: str, title: str, target: str,
                    language: str = 'zh-tw', uid: Optional[str] = '', cid: Optional[str] = None, decode_format: str = '',
                    sd: str = '', sr: str = '', did: str = '', view_port_size: str = ''
                    ):
        result, cid = self._record_event(
            version=version, action='click', url=url, title=title, target=target,
            language=language, uid=uid, cid=cid, decode_format=decode_format, sd=sd,
            sr=sr, did=did, view_port_size=view_port_size
        )

    def view_event(self, version: str, url: str, title: str, target: str,
                   language: str = 'zh-tw', uid: Optional[str] = '', cid: Optional[str] = None, decode_format: str = '',
                   sd: str = '', sr: str = '', did: str = '', view_port_size: str = ''
                   ):
        result, cid = self._record_event(
            version=version, action='view', url=url, title=title, target=target,
            language=language, uid=uid, cid=cid, decode_format=decode_format, sd=sd,
            sr=sr, did=did, view_port_size=view_port_size
        )

    def _record_event(self, version: str, action: str, url: str, title: str, target: str,
                      language: str = 'zh-tw', uid: Optional[str] = '', cid: Optional[str] = None, decode_format: str = '',
                      sd: str = '', sr: str = '', did: str = '', view_port_size: str = ''):

        if cid is None:
            try:
                response = requests.get(self.cerem_url + '/tracking/generate-cid/', params={'team_code': self.team_code})
                cid = response.json()['cid']
            except Exception:
                return False, ''

        payload = {
            'tc': self.team_code,
            'did': did,
            'v': version,
            'uid': uid,
            'cid': cid,
            'tg': target,
            'de': decode_format,
            'at': action,
            'ul': language,
            'pt': url,
            'sd': sd,
            'sr': sr,
            'tl': title,
            'vp': view_port_size
        }

        requests.get(self.relay_url + '/api/' + self.ds_id + '/tracking/', params=payload)

        return True, cid
