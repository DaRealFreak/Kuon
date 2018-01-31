#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
from base64 import b64encode

# covered by python-dotenv
# noinspection PyPackageRequirements
import dotenv
import re
import requests

from opskins.api.exceptions import *


class OPSkins(object):
    _api_key = None

    def __init__(self, api_key=None):
        """Initializing function
        According to the API documentation (https://opskins.com/kb/api-v2) they
        prefer to receive the key per basic http authentication as username
        so we set the header for the session in the init function already

        :type api_key: string
        """
        if api_key:
            self._api_key = api_key
        else:
            dotenv_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, '.env')
            dotenv.load_dotenv(dotenv_path)
            self._api_key = os.environ.get('OPSKINS_API_KEY')

        if not self._api_key:
            raise NoAPIKeyProvidedException('Please provide an API key via .env or as argument')

        auth = b64encode("{0:s}:".format(self._api_key).encode(encoding="utf-8", errors="strict")).decode("ascii")
        self._headers = {'Authorization': 'Basic %s' % auth}
        self.validate_api_key()

    def validate_api_key(self):
        """Validate the api key

        :return:
        """
        api_url = 'https://api.opskins.com/ITest/TestAuthed/v1/'
        link = requests.get(url=api_url, headers=self._headers)

        response = json.loads(link.text)
        if response['status'] == 401:
            raise InvalidOrWrongApiKeyException('Please provide a valid API key')

    @staticmethod
    def app_id_to_search_id(app_id: int):
        """Converts the app id of the game to the search id used by OPSkins

        :param app_id:
        :return:
        """
        return str(app_id) + "_2"

