#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.api_response import APIResponse
from kuon.bitskins import BitSkins
from kuon.common import *


class IHistory(BitSkins):
    """Implementation of the API methods related to the history of the user on BitSkins

    common not self explanatory keys:
        app id:
            The Steam AppID of the game which owns this item (e.g. 730 for CS:GO, 440 for TF2, 570 for Dota 2)
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initializing function

        :type args: list
        :type kwargs: dict
        """
        super().__init__(*args, **kwargs)

    def get_money_events(self, page: int = None) -> APIResponse:
        """GetMoneyEvents v1 implementation
        https://bitskins.com/api/#get_money_events

        :type page: int
        :return:
        """
        api_url = "https://bitskins.com/api/v1/get_money_events/"

        payload = {}

        if page:
            payload['page'] = page

        return self.api_request(api_url=api_url, params=payload)

    def get_buy_history(self, app_id: int = CommonSteamGames.APP_ID_CSGO, page: int = None) -> APIResponse:
        """GetBuyHistory v1 implementation
        https://bitskins.com/api/#get_buy_history

        :type app_id: int
        :type page: int
        :return:
        """
        api_url = "https://bitskins.com/api/v1/get_buy_history/"

        payload = {
            'app_id': app_id
        }

        if page:
            payload['page'] = int(page)

        return self.api_request(api_url=api_url, params=payload)

    def get_sell_history(self, app_id: int = CommonSteamGames.APP_ID_CSGO, page: int = None) -> APIResponse:
        """GetSellHistory v1 implementation
        https://bitskins.com/api/#get_sell_history

        :type app_id:
        :type page:
        :return:
        """
        api_url = "https://bitskins.com/api/v1/get_sell_history/"

        payload = {
            'app_id': app_id
        }

        if page:
            payload['page'] = int(page)

        return self.api_request(api_url=api_url, params=payload)

    def get_item_history(self, app_id: int = CommonSteamGames.APP_ID_CSGO, page: int = None, names: str = "",
                         delimiter: str = "", per_page: int = None) -> APIResponse:
        """GetItemHistory v1 implementation
        https://bitskins.com/api/#get_item_history

        :type app_id: int
        :type page: int
        :type names: str
        :type delimiter: str
        :type per_page: int
        :return:
        """
        api_url = "https://bitskins.com/api/v1/get_item_history/"

        payload = {
            'app_id': app_id
        }

        if page:
            payload['page'] = page
        if names:
            payload['names'] = names
        if delimiter:
            payload['delimiter'] = delimiter
        if per_page:
            payload['per_page'] = per_page

        return self.api_request(api_url=api_url, params=payload)

    def get_trade_details(self, trade_id: str, trade_token: str) -> APIResponse:
        """GetTradeDetails v1 implementation
        https://bitskins.com/api/#get_trade_details

        :type trade_id: str
        :type trade_token: str
        :return:
        """
        api_url = "https://bitskins.com/api/v1/get_trade_details/"

        payload = {
            "trade_id": trade_id,
            "trade_token": trade_token
        }

        return self.api_request(api_url=api_url, params=payload)

    def get_recent_trade_offers(self, active_only: bool = False) -> APIResponse:
        """GetRecentTradeOffers v1 implementation
        https://bitskins.com/api/#get_recent_trade_offers

        :type active_only: bool
        :return:
        """
        api_url = "https://bitskins.com/api/v1/get_recent_trade_offers/"

        payload = {}

        if active_only:
            payload['active_only'] = 'true'

        return self.api_request(api_url=api_url, params=payload)
