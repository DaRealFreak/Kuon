#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.common import CommonSteamGames
from kuon.steam.common import SteamUrls
from kuon.steam.steam_login import SteamLogin


class Steam(SteamLogin):

    def __init__(self, *args, **kwargs):
        """Initializing function

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)

    def get_my_inventory(self):
        url = '{base:s}/my/inventory/json/{app_id:d}/{app_context:d}'.format(base=SteamUrls.COMMUNITY,
                                                                             app_id=CommonSteamGames.APP_ID_CSGO,
                                                                             app_context=2)
        print(self._session.get(url).json())
