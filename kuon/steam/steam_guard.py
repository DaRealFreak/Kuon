#!/usr/bin/python
# -*- coding: utf-8 -*-
import hmac
import os
import struct
import time
from base64 import b64decode, b64encode
from hashlib import sha1

import dotenv

from kuon.steam.api.exceptions import *


class SteamGuard(object):
    """Class to provide functionality regarding SteamGuard
    big thanks to bukson/steampy who extracted most of these functions from the mobile app"""

    def __init__(self, user: str = None, password: str = None, id_64: str = None, api_key: str = None,
                 secret: str = None, identity: str = None) -> None:
        """Initializing function

        :type user: str
        :type password: str
        :type id_64: str
        :type api_key: str
        :type secret: str
        :type identity: str
        """

        dotenv_path = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, '.env')
        dotenv.load_dotenv(dotenv_path)

        self._user = user
        self._password = password
        self._id64 = id_64
        self._api_key = api_key
        self._secret = secret
        self._identity = identity

        if not self._user:
            self._user = os.environ.get('STEAM_LOGIN_ID')

        if not self._password:
            self._password = os.environ.get('STEAM_LOGIN_PASSWORD')

        if not self._id64:
            self._id64 = os.environ.get('STEAM_ID64')

        if not api_key:
            self._api_key = os.environ.get('STEAM_API_KEY')

        if not secret:
            self._secret = os.environ.get('STEAM_2FA_SECRET')

        if not self._identity:
            self._identity = os.environ.get('STEAM_IDENTITY_SECRET')

        self.check_required_variables()

    @property
    def generate_one_time_code(self) -> str:
        """Generate the login code like the mobile app does

        :return:
        """
        timestamp = int(time.time())
        time_buffer = struct.pack('>Q', timestamp // 30)  # pack as Big endian, uint64
        time_hmac = hmac.new(b64decode(self._secret), time_buffer, digestmod=sha1).digest()
        begin = ord(time_hmac[19:20]) & 0xf
        full_code = struct.unpack('>I', time_hmac[begin:begin + 4])[0] & 0x7fffffff  # unpack as Big endian uint32
        chars = '23456789BCDFGHJKMNPQRTVWXY'
        code = ''

        for i in range(5):
            full_code, i = divmod(full_code, len(chars))
            code += chars[i]

        return code

    def get_confirmation_key(self, tag: str) -> bytes:
        """Generate the confirmation key of the tag like the mobile app does

        :type tag: str
        :return:
        """
        timestamp = int(time.time())
        buffer = struct.pack('>Q', timestamp) + tag.encode('ascii')
        return b64encode(hmac.new(b64decode(self._identity), buffer, digestmod=sha1).digest())

    @property
    def generate_device_id(self) -> str:
        """Generate a device needed for confirmations (similar to the mobile device app)

        :return:
        """
        hexed_steam_id = sha1(self._id64.encode('ascii')).hexdigest()
        return 'android:' + '-'.join([hexed_steam_id[:8],
                                      hexed_steam_id[8:12],
                                      hexed_steam_id[12:16],
                                      hexed_steam_id[16:20],
                                      hexed_steam_id[20:32]])

    def check_required_variables(self) -> None:
        """check all required variables for the full usage

        :return:
        """
        if not self._user:
            raise NoLoginIdProvidedException('Please provide a username for the login')

        if not self._password:
            raise NoLoginPassProvidedException('Please provide a password for the login')

        if not self._id64:
            raise NoSteamID64ProvidedException('Please provide your SteamID64')

        if not self._api_key:
            raise NoAPIKeyProvidedException('Please provide an API key via .env or as argument')

        if not self._secret:
            raise No2FASecretProvidedException('Please provide a secret to generate One Time Passwords')

        if not self._identity:
            raise NoIdentitySecretKeyProvidedException('Please provide the identity secret via .env or as argument')
