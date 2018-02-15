#!/usr/bin/python
# -*- coding: utf-8 -*-
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

    def __init__(self, *args, **kwargs):
        """Initializing function"""
        super().__init__(*args, **kwargs)

    def get_inventory_on_sale(self, app_id=CommonSteamGames.APP_ID_CSGO, page=None, sort_by=Sorting.PRICE,
                              order=SortingDirection.ASCENDING, market_hash_name=None, min_price=None, max_price=None,
                              has_stickers=False, is_stattrak=False, is_souvenir=False, per_page=None) -> APIResponse:
        """GetInventoryOnSale v1 implementation
        https://bitskins.com/api/#get_inventory_on_sale

        :param app_id:
        :param page:
        :param sort_by:
        :param order:
        :param market_hash_name:
        :param min_price:
        :param max_price:
        :param has_stickers:
        :param is_stattrak:
        :param is_souvenir:
        :param per_page:
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

    def get_sales_info(self, market_hash_name: str, app_id=CommonSteamGames.APP_ID_CSGO, page=None) -> APIResponse:
        """GetRecentSaleInfo v1 implementation
        https://bitskins.com/api#get_sales_info

        :param market_hash_name:
        :param page:
        :param app_id:
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

    def buy_item(self, item_ids: list, prices: list, app_id=CommonSteamGames.APP_ID_CSGO,
                 auto_trade=True) -> APIResponse:
        """BuyItem v1 implementation
        https://bitskins.com/api#buy_item

        :param item_ids:
        :param prices:
        :param app_id:
        :param auto_trade:
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

    def list_item_for_sale(self, item_ids: list, prices: list, app_id=CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """SellItem v1 implementation
        https://bitskins.com/api#list_item_for_sale

        :param item_ids:
        :param prices:
        :param app_id:
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/list_item_for_sale/'

        payload = {
            'app_id': app_id,
            'item_ids': ",".join(item_ids),
            'prices': ",".join(prices)
        }

        return self.api_request(api_url=api_url, params=payload)

    def modify_sale_item(self, item_ids: list, prices: list, app_id=CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """ModifySale v1 implementation
        https://bitskins.com/api#modify_sale_item

        :param item_ids:
        :param prices:
        :param app_id:
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/modify_sale_item/'

        payload = {
            'app_id': app_id,
            'item_ids': ",".join(item_ids),
            'prices': ",".join(prices)
        }

        return self.api_request(api_url=api_url, params=payload)

    def withdraw_item(self, item_ids: list, app_id=CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """WithdrawItem v1 implementation
        https://bitskins.com/api#withdraw_item

        :param item_ids:
        :param app_id:
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/withdraw_item/'

        payload = {
            'app_id': app_id,
            'item_ids': ",".join(item_ids)
        }

        return self.api_request(api_url=api_url, params=payload)

    def bump_item(self, item_ids: list, app_id=CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """BumpItem v1 implementation
        https://bitskins.com/api#bump_item

        :param item_ids:
        :param app_id:
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/bump_item/'

        payload = {
            'app_id': app_id,
            'item_ids': ",".join(item_ids)
        }

        return self.api_request(api_url=api_url, params=payload)

    def get_reset_price_items(self, app_id=CommonSteamGames.APP_ID_CSGO, page=None) -> APIResponse:
        """GetResetPriceItems v1 implementation
        https://bitskins.com/api#get_reset_price_items

        :param app_id:
        :param page:
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/get_reset_price_items/'

        payload = {
            'app_id': app_id,
        }

        if page:
            payload['page'] = int(page)

        return self.api_request(api_url=api_url, params=payload)

    def get_steam_price_data(self, market_hash_name: str, app_id=CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """GetRawPriceData v1 implementation
        https://bitskins.com/api#get_steam_price_data

        Returns the cheapest steam market price

        :param market_hash_name:
        :param app_id:
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/get_steam_price_data/'

        payload = {
            'app_id': app_id,
            'market_hash_name': market_hash_name
        }

        return self.api_request(api_url=api_url, params=payload)

    def get_specific_items_on_sale(self, item_ids: list, app_id=CommonSteamGames.APP_ID_CSGO) -> APIResponse:
        """GetSpecificItemsOnSale v1 implementation
        https://bitskins.com/api#get_specific_items_on_sale

        Returns detailed information of requested items currently on sale on BitSkins

        :param item_ids:
        :param app_id:
        :return:
        """
        api_url = 'https://bitskins.com/api/v1/get_specific_items_on_sale/'

        payload = {
            'app_id': app_id,
            'item_ids': ",".join(item_ids)
        }

        return self.api_request(api_url=api_url, params=payload)
