#!/usr/bin/python
# -*- coding: utf-8 -*-

from kuon.bitskins import BitSkins
from kuon.bitskins.api.exceptions import *
from kuon.common import *


class IPricing(BitSkins):
    """Implementation of the API methods related to the pricing of items on BitSkins

    common not self explanatory keys:
        app id:
            The Steam AppID of the game which owns this item (e.g. 730 for CS:GO, 440 for TF2, 570 for Dota 2)
    """

    def __init__(self, *args, **kwargs):
        """Initializing function"""
        super().__init__(*args, **kwargs)

    def get_all_item_prices(self, app_id=CommonSteamGames.APP_ID_CSGO):
        """GetAllItemPrices v1 implementation
        https://bitskins.com/api/#get_all_item_prices

        Returns the suggested prices for every item on the market

        :param app_id:
        :return:
        """
        api_url = "https://bitskins.com/api/v1/get_all_item_prices/"

        payload = {
            'app_id': str(app_id)
        }

        return self.api_request(api_url=api_url, params=payload)

    def get_price_data_for_items_on_sale(self, app_id=CommonSteamGames.APP_ID_CSGO):
        """GetMarketData v1 implementation
        https://bitskins.com/api/#get_price_data_for_items_on_sale

        Returns market data regarding how many items are on the market and highest/lowest price for every item

        :param app_id:
        :return:
        """
        api_url = "https://bitskins.com/api/v1/get_price_data_for_items_on_sale/"

        payload = {
            'app_id': str(app_id)
        }

        return self.api_request(api_url=api_url, params=payload)
