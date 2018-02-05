#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is an example usage
import logging
from pprint import pprint

from opskins.api.common import *
from opskins.api.interfaces import *
from opskins.common import *
from opskins.watcher import Watcher


def usage_watcher():
    """Example watcher usage

    :return:
    """
    Watcher(log_level=logging.INFO)


def usage_inventory_interface():
    """Example inventory interface usage

    :return:
    """
    inventory_interface = IInventory()
    pprint(inventory_interface.withdraw(['123', '456']))


def usage_cashout_interface():
    """Example cashout interface usage

    :return:
    """
    cashout_interface = ICashout()
    pprint(cashout_interface.get_address(Processor.PAYPAL))


def usage_pricing_interface():
    """Example pricing interface usage

    :return:
    """
    pricing_interface = IPricing()
    pprint(pricing_interface.get_all_lowest_list_prices())


def usage_status_interface():
    """Example status interface usage

    :return:
    """
    status_interface = IStatus()
    pprint(status_interface.get_bot_list().response.bots)


def usage_user_interface():
    """Example user interface usage

    :return:
    """
    user_interface = IUser()
    pprint(user_interface.get_balance())


def usage_sales_interface():
    """Example sales interface usage

    :return:
    """
    sales_interface = ISales()
    pprint(sales_interface.get_sales(status_type=ItemStatus.SOLD_AND_DELIVERED, app_id=CommonSteamGames.APP_ID_CSGO))
    pprint(sales_interface.get_last_sales(app_id=CommonSteamGames.APP_ID_CSGO, context_id=ContextIds.VALVE_GAMES,
                                          market_name='AK-47 | Aquamarine Revenge (Field-Tested)'))
    pprint(sales_interface.search(search_item="howl min", app_id=CommonSteamGames.APP_ID_CSGO))

    # uses selenium chrome driver so initial call takes a few seconds to initialise the driver
    # on second use and later it will take way less time
    pprint(sales_interface.search_no_delay(search_item="howl min", app_id=CommonSteamGames.APP_ID_CSGO))


if __name__ == '__main__':
    usage_watcher()
