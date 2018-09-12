#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Union

from kuon.api_response import APIResponse
from kuon.bitskins import BitSkins
from kuon.bitskins.common import *
from kuon.common import CommonSteamGames


class ISales(BitSkins):
    """Implementation of the API methods related to market sales of BitSkins

    common not self explanatory keys:
        app id:
            The Steam AppID of the game which owns this item (e.g. 730 for CS:GO, 440 for TF2, 570 for Dota 2)
        market hash name:
            The full market name of the item. For example: "AK-47 | Aquamarine Revenge (Field-Tested)"
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initializing function

        :type args: list
        :type kwargs: dict
        """
        super().__init__(*args, **kwargs)

    def get_inventory_on_sale(self, app_id: int = CommonSteamGames.APP_ID_CSGO, page: int = None,
                              sort_by: str = Sorting.PRICE, order: str = SortingDirection.ASCENDING,
                              market_hash_name: str = None, min_price: int = None, max_price: int = None,
                              has_stickers: bool = None, is_stattrak: bool = None, is_souvenir: bool = None,
                              per_page: int = None) -> APIResponse:
        """GetInventoryOnSale v1 implementation
        https://bitskins.com/api/#get_inventory_on_sale

        :type app_id: int
        :type page: int
        :type sort_by: str
        :type order: str
        :type market_hash_name: str
        :type min_price: int
        :type max_price: int
        :type has_stickers: bool
        :type is_stattrak: bool
        :type is_souvenir: bool
        :type per_page: int
        :return:
        """
        arguments = locals()
        api_url = "https://bitskins.com/api/v1/get_inventory_on_sale/"

        payload = {
            'app_id': str(app_id)
        }

        for argument in arguments:
            if argument == 'self':
                continue

            if arguments[argument] is not None:
                payload[argument] = arguments[argument]

        return self.api_request(api_url=api_url, params=payload)

    def get_sales_info(self, market_hash_name: str, app_id: int = CommonSteamGames.APP_ID_CSGO,
                       page: int = None) -> APIResponse:
        """GetRecentSaleInfo v1 implementation
        https://bitskins.com/api#get_sales_info

        :type market_hash_name: str
        :type page: int
        :type app_id: int
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/get_sales_info/'

        payload = {
            'app_id': app_id,
            'market_hash_name': market_hash_name
        }

        if page:
            payload['page'] = int(page)

        return self.api_request(api_url=api_url, params=payload)

    def buy_item(self, item_ids: Union[list, tuple], prices: Union[list, tuple],
                 app_id: int = CommonSteamGames.APP_ID_CSGO, auto_trade: bool = True) -> APIResponse:
        """BuyItem v1 implementation
        https://bitskins.com/api#buy_item

        :type item_ids: Union[list, tuple]
        :type prices: Union[list, tuple]
        :type app_id: int
        :type auto_trade: bool
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/buy_item/'

        payload = {
            'app_id': app_id,
            'item_ids': ",".join(item_ids),
            'prices': ",".join(prices)
        }

        if not auto_trade:
            payload['auto_trade'] = 'false'

        return self.api_request(api_url=api_url, params=payload)

    def list_item_for_sale(self, item_ids: Union[list, tuple], prices: Union[list, tuple],
                           app_id: int = CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """SellItem v1 implementation
        https://bitskins.com/api#list_item_for_sale

        :type item_ids: Union[list, tuple]
        :type prices: Union[list, tuple]
        :type app_id: int
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/list_item_for_sale/'

        payload = {
            'app_id': app_id,
            'item_ids': ",".join(item_ids),
            'prices': ",".join(prices)
        }

        return self.api_request(api_url=api_url, params=payload)

    def modify_sale_item(self, item_ids: Union[list, tuple], prices: Union[list, tuple],
                         app_id: int = CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """ModifySale v1 implementation
        https://bitskins.com/api#modify_sale_item

        :type item_ids: Union[list, tuple]
        :type prices: Union[list, tuple]
        :type app_id: int
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/modify_sale_item/'

        payload = {
            'app_id': app_id,
            'item_ids': ",".join(item_ids),
            'prices': ",".join(prices)
        }

        return self.api_request(api_url=api_url, params=payload)

    def withdraw_item(self, item_ids: Union[list, tuple], app_id: int = CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """WithdrawItem v1 implementation
        https://bitskins.com/api#withdraw_item

        :type item_ids: Union[list, tuple]
        :type app_id: int
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/withdraw_item/'

        payload = {
            'app_id': app_id,
            'item_ids': ",".join(item_ids)
        }

        return self.api_request(api_url=api_url, params=payload)

    def bump_item(self, item_ids: Union[list, tuple], app_id: int = CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """BumpItem v1 implementation
        https://bitskins.com/api#bump_item

        :type item_ids: Union[list, tuple]
        :type app_id:
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/bump_item/'

        payload = {
            'app_id': app_id,
            'item_ids': ",".join(item_ids)
        }

        return self.api_request(api_url=api_url, params=payload)

    def get_reset_price_items(self, app_id: int = CommonSteamGames.APP_ID_CSGO, page: int = None) -> APIResponse:
        """GetResetPriceItems v1 implementation
        https://bitskins.com/api#get_reset_price_items

        :type app_id: int
        :type page: int
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/get_reset_price_items/'

        payload = {
            'app_id': app_id,
        }

        if page:
            payload['page'] = int(page)

        return self.api_request(api_url=api_url, params=payload)

    def get_steam_price_data(self, market_hash_name: str, app_id: int = CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """GetRawPriceData v1 implementation
        https://bitskins.com/api#get_steam_price_data

        Returns the cheapest steam market price

        :type market_hash_name: str
        :type app_id: int
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/get_steam_price_data/'

        payload = {
            'app_id': app_id,
            'market_hash_name': market_hash_name
        }

        return self.api_request(api_url=api_url, params=payload)

    def get_specific_items_on_sale(self, item_ids: Union[list, tuple],
                                   app_id: int = CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """GetSpecificItemsOnSale v1 implementation
        https://bitskins.com/api#get_specific_items_on_sale

        Returns detailed information of requested items currently on sale on BitSkins

        :type item_ids: Union[list, tuple]
        :type app_id: int
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/get_specific_items_on_sale/'

        payload = {
            'app_id': app_id,
            'item_ids': ",".join(item_ids)
        }

        return self.api_request(api_url=api_url, params=payload)
