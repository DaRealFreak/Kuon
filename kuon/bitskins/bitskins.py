#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

# covered by python-dotenv
# noinspection PyPackageRequirements
import dotenv
import pyotp
import requests

from kuon.api_response import APIResponse
from kuon.bitskins.api.exceptions import *
from kuon.selenium_helper import SeleniumHelper


class BitSkins(object):
    _selenium_helper = None

    def __init__(self, api_key=None, secret=None):
        """Initializing function
        According to the API documentation (https://bitskins.com/api/python#totp_code) they
        require OTPs and the API key so we verify the API key and the secret and generate the OTPs with a property

        :type api_key: string
        :type secret: string
        """
        dotenv_path = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, '.env')
        dotenv.load_dotenv(dotenv_path)

        self._api_key = api_key
        self._secret = secret

        if not api_key:
            self._api_key = os.environ.get('BITSKINS_API_KEY')

        if not secret:
            self._secret = os.environ.get('BITSKINS_2FA_SECRET')

        if not self._api_key:
            raise NoAPIKeyProvidedException('Please provide an API key via .env or as argument')

        if not self._secret:
            raise NoSecretProvidedException('Please provide a secret to generate One Time Passwords for the API usage')

        self._pyotp = pyotp.TOTP(self._secret)
        self.validate_api_key()

    def api_request(self, api_url, params=None, headers=None):
        """Insert API key and OTP code to the payload and return the parsed response

        :param api_url:
        :param params:
        :param headers:
        :return:
        """
        if headers is None:
            headers = {}
        if params is None:
            params = {}

        params['api_key'] = self._api_key
        params['code'] = self.secret

        link = requests.get(url=api_url, params=params, headers=headers)

        return APIResponse(link.text)

    def validate_api_key(self):
        """Validate the api key and the 2 FA secret

        :return:
        """
        api_url = "https://bitskins.com/api/v1/get_account_balance/"
        response = self.api_request(api_url=api_url)

        if response.status != "success":
            raise InvalidOrWrongApiKeyException('Please provide a valid API key and 2 FA secret')

    @property
    def selenium_helper(self):
        """Use property to make this lazy since it takes 3-4 seconds to load

        :return:
        """
        if not self._selenium_helper:
            self._selenium_helper = SeleniumHelper()
        return self._selenium_helper

    @property
    def secret(self):
        """Getter for One Time Passwords based on the given secret

        :return:
        """
        return self._pyotp.now()
