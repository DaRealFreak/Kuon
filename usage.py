#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is an example usage

from pprint import pprint

from opskins.api.common import *
from opskins.api.interfaces import ISales, IUser
from opskins.common import *

if __name__ == '__main__':
    user_interface = IUser()
    pprint(user_interface.get_balance())

    sales_interface = ISales()
    pprint(sales_interface.get_sales(status_type=ItemStatus.SOLD_AND_DELIVERED, app_id=CommonSteamGames.APP_ID_CSGO))
    pprint(sales_interface.get_last_sales(app_id=CommonSteamGames.APP_ID_CSGO, context_id=ContextIds.VALVE_GAMES,
                                          market_name='AK-47 | Aquamarine Revenge (Field-Tested)'))
    pprint(sales_interface.search(search_word="howl min", app_id=CommonSteamGames.APP_ID_CSGO))
