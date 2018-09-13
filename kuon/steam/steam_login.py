#!/usr/bin/python
# -*- coding: utf-8 -*-
from base64 import b64encode
from time import time

import requests
import rsa

from kuon.steam.common import SteamUrls
from kuon.steam.steam_guard import SteamGuard


class SteamLogin(SteamGuard):
    """Class providing the login functionality of the steam mobile client"""

    def __init__(self, *args, **kwargs) -> None:
        """Initializing function

        :type args: list
        :type kwargs: dict
        """
        super().__init__(*args, **kwargs)

        self._session = requests.Session()
        self._rsa_data = {}

        self.login()
        self.set_sessionid_cookies()

    def login(self) -> None:
        """Login into the set account

        :return:
        """
        response = self._session.post(SteamUrls.STORE + '/login/dologin', data=self.login_data).json()
        self.visit_transfer_urls(response)
        return response['success']

    @property
    def rsa_key(self) -> dict:
        """Retrieve the public key modulus and exponent and generate an RSA public key from it

        :return:
        """
        if not self._rsa_data:
            response = self._session.post(SteamUrls.STORE + '/login/getrsakey/', data={'username': self._user}).json()
            rsa_mod = int(response['publickey_mod'], 16)
            rsa_exp = int(response['publickey_exp'], 16)
            rsa_timestamp = response['timestamp']
            self._rsa_data = {
                'rsa_key': rsa.PublicKey(rsa_mod, rsa_exp),
                'rsa_tstamp': rsa_timestamp
            }
        return self._rsa_data

    @property
    def login_data(self) -> dict:
        """Retrieve the form login data

        :return:
        """
        return {
            'username': self._user,
            'password': b64encode(rsa.encrypt(self._password.encode(encoding="utf-8"), self.rsa_key['rsa_key'])),
            'twofactorcode': self.generate_one_time_code,
            'emailauth': '',
            'loginfriendlyname': '',
            'captchagid': '-1',
            'captcha_text': '',
            'emailsteamid': '',
            'rsatimestamp': self.rsa_key['rsa_tstamp'],
            'remember_login': 'false',
            'donotcache': str(int(time() * 1000))
        }

    def visit_transfer_urls(self, response: dict) -> None:
        """Visit the transfer urls to create the session

        :type response: dict
        :return:
        """
        parameters = response.get('transfer_parameters')
        for url in response['transfer_urls']:
            self._session.post(url, parameters)

    def set_sessionid_cookies(self) -> None:
        """Create the newly created session for the community and the store url

        :return:
        """
        session_id = self._session.cookies.get_dict()['sessionid']
        self.set_session_cookie(SteamUrls.COMMUNITY[8:], session_id)
        self.set_session_cookie(SteamUrls.STORE[8:], session_id)

    def set_session_cookie(self, domain: str, session_id: str) -> None:
        """Set the passed cookie for the passed domain

        :param domain:
        :param session_id:
        :return:
        """
        self._session.cookies.set(**{
            "name": "sessionid",
            "value": session_id,
            "domain": domain
        })
