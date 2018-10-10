#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.api_response import APIResponse
from kuon.steam.steam_login import SteamLogin


class Steam(SteamLogin):

    def __init__(self, *args, **kwargs):
        """Initializing function

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)

    def api_request(self, api_url: str, params: dict = None, headers: dict = None) -> APIResponse:
        """Insert API key and OTP code to the payload and return the parsed response

        :type api_url: str
        :type params: dict
        :type headers: dict
        :return:
        """
        if headers is None:
            headers = {}
        if params is None:
            params = {}

        link = self._session.get(url=api_url, params=params, headers=headers)

        return APIResponse(link.text)
