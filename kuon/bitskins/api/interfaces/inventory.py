#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.api_response import APIResponse
from kuon.bitskins import BitSkins
from kuon.common import *


class IInventory(BitSkins):
    """Implementation of the API methods related to the inventory of the user on BitSkins

    common not self explanatory keys:
        app id:
            The Steam AppID of the game which owns this item (e.g. 730 for CS:GO, 440 for TF2, 570 for Dota 2)
    """

    def __init__(self, *args, **kwargs):
        """Initializing function"""
        super().__init__(*args, **kwargs)

    def get_my_inventory(self, app_id=CommonSteamGames.APP_ID_CSGO, page=None) -> APIResponse:
        """GetAccountInventory v1 implementation
        https://bitskins.com/api/#get_my_inventory

        Returns the newest 5000 items, use pages to navigate through more

        :param app_id:
        :param page:
        :return:
        """
        api_url = "https://bitskins.com/api/v1/get_my_inventory/"

        payload = {
            'app_id': str(app_id)
        }

        if page:
            payload['page'] = int(page)

        return self.api_request(api_url=api_url, params=payload)
