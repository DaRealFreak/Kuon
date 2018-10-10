#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.common import CommonSteamGames
from kuon.steam.common import SteamUrls
from kuon.steam.steam import Steam


class IInventory(Steam):
    """Implementation of the API methods related to the inventory of the user on Steam

    common not self explanatory keys:
        app id:
            The Steam AppID of the game which owns this item (e.g. 730 for CS:GO, 440 for TF2, 570 for Dota 2)
        app context:
            The context of the game. Nearly all games usually have the context id 2, while Steam items usually have the
            context id 6
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_my_inventory(self, app_id: int = CommonSteamGames.APP_ID_CSGO, app_context: int = 2):
        """Retrieve the steam inventory

        :type app_id: int
        :type app_context: int
        :return:
        """
        url = '{base:s}/my/inventory/json/{app_id:d}/{app_context:d}'.format(base=SteamUrls.COMMUNITY,
                                                                             app_id=app_id,
                                                                             app_context=app_context)
        return self.api_request(url)
