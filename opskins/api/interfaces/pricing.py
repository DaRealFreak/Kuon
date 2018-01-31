#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

from opskins import OPSkins
from opskins.api import APIResponse
from opskins.api.exceptions import *
from opskins.common import *


class IPricing(OPSkins):
    """The IPricing interface of OPSkins"""

    def __init__(self):
        """Initializing function"""
        super().__init__()

    def get_price_list(self, app_id=CommonSteamGames.APP_ID_CSGO):
        """GetPriceList v2 implementation
        https://opskins.com/kb/api-ipricing#method-getpricelist-v2

        The output of this method is cached by the CDN of OPSkins, refreshes only daily

        :param app_id:
        :return:
        """
        api_url = "https://api.opskins.com/IPricing/GetPriceList/v2/"

        if not app_id:
            raise MissingArgumentException('The function get_price_list requires the argument "app_id"')

        payload = {
            'appid': str(app_id)
        }

        link = requests.get(url=api_url, params=payload, headers=self._headers)
        return APIResponse(link.text)

    def get_all_lowest_list_prices(self, app_id=CommonSteamGames.APP_ID_CSGO):
        """GetAllLowestListPrices v1 implementation
        https://opskins.com/kb/api-ipricing#method-getalllowestlistprices-v1

        :param app_id:
        :return:
        """
        api_url = "https://api.opskins.com/IPricing/GetAllLowestListPrices/v1/"

        if not app_id:
            raise MissingArgumentException('The function get_all_lowest_list_prices requires the argument "app_id"')

        payload = {
            'appid': str(app_id)
        }

        link = requests.get(url=api_url, params=payload, headers=self._headers)
        return APIResponse(link.text)
