#!/usr/bin/python
# -*- coding: utf-8 -*-

from kuon.bitskins import BitSkins
from kuon.bitskins.api.exceptions import *
from kuon.common import CommonSteamGames


class ISales(BitSkins):
    """Implementation of the API methods related to market sales of BitSkins

    common not self explanatory keys:
        app id:
            The Steam AppID of the game which owns this item (e.g. 730 for CS:GO, 440 for TF2, 570 for Dota 2)
        context id:
            (2 for Valve games, 6 for Steam Community items, 1 for H1Z1, etc.).
            When you right-click on an item in your Steam inventory and copy its URL,
            the context ID is the second number after the hash.
        market hash name:
            The full market name of the item. For example: "AK-47 | Aquamarine Revenge (Field-Tested)"
    """

    def __init__(self, *args, **kwargs):
        """Initializing function"""
        super().__init__(*args, **kwargs)

    def get_sales_info(self, market_hash_name: str, page=None, app_id=CommonSteamGames.APP_ID_CSGO):
        """GetRecentSaleInfo v1 implementation
        https://bitskins.com/api#get_sales_info

        :param market_hash_name:
        :param page:
        :param app_id:
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/get_sales_info/'

        if not app_id:
            raise MissingArgumentException('The function get_last_sales requires the argument "app_id"')

        payload = {
            'market_hash_name': market_hash_name,
            'app_id': str(app_id),
        }

        if page:
            payload['page'] = int(page)

        return self.api_request(api_url=api_url, params=payload)
