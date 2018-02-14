#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is an example usage

import logging
from pprint import pprint

import kuon.bitskins.api.interfaces as bitskins_interfaces
import kuon.opskins.api.interfaces as opskins_interfaces
import kuon.opskins.common as opskins_common
from kuon.common import *
from kuon.watcher import Watcher


class UsageWatcher:
    """Example usage for the watcher class of Kuon"""

    @staticmethod
    def watcher():
        """Example watcher usage

        :return:
        """
        Watcher(log_level=logging.INFO)


class UsageBitSkins:
    """Example usages for the implementation of the BitSkins API"""

    @staticmethod
    def sales_interface():
        """Example sales interface usage

        :return:
        """
        sales_interface = bitskins_interfaces.ISales()

        pprint(sales_interface.get_sales_info(market_hash_name="M4A4 | Howl (Factory New)"))

    @staticmethod
    def pricing_interface():
        """Example pricing interface usage

        :return:
        """
        pricing_interface = bitskins_interfaces.IPricing()
        pprint(pricing_interface.get_all_item_prices())
        pprint(pricing_interface.get_price_data_for_items_on_sale())


class UsageOPSkins:
    """Example usages for the implementation of the OPSkins API"""

    @staticmethod
    def inventory_interface():
        """Example inventory interface usage

        :return:
        """
        inventory_interface = opskins_interfaces.IInventory()
        pprint(inventory_interface.withdraw(['123', '456']))

    @staticmethod
    def cashout_interface():
        """Example cashout interface usage

        :return:
        """
        cashout_interface = opskins_interfaces.ICashout()
        pprint(cashout_interface.get_address(opskins_common.Processor.PAYPAL))

    @staticmethod
    def pricing_interface():
        """Example pricing interface usage

        :return:
        """
        pricing_interface = opskins_interfaces.IPricing()
        pprint(pricing_interface.get_all_lowest_list_prices())

    @staticmethod
    def status_interface():
        """Example status interface usage

        :return:
        """
        status_interface = opskins_interfaces.IStatus()
        pprint(status_interface.get_bot_list().response.bots)

    @staticmethod
    def user_interface():
        """Example user interface usage

        :return:
        """
        user_interface = opskins_interfaces.IUser()
        pprint(user_interface.get_balance())

    @staticmethod
    def sales_interface():
        """Example sales interface usage

        :return:
        """
        sales_interface = opskins_interfaces.ISales()

        pprint(sales_interface.get_sales(status_type=opskins_common.ItemStatus.SOLD_AND_DELIVERED,
                                         app_id=CommonSteamGames.APP_ID_CSGO))
        pprint(sales_interface.get_last_sales(app_id=CommonSteamGames.APP_ID_CSGO, context_id=ContextIds.VALVE_GAMES,
                                              market_name='AK-47 | Aquamarine Revenge (Field-Tested)'))
        pprint(sales_interface.get_last_sales_no_delay(market_name='M4A4 | Howl (Factory New)'))
        pprint(sales_interface.search(search_item="howl min", app_id=CommonSteamGames.APP_ID_CSGO))

        # uses selenium chrome driver so initial call takes a few seconds to initialise the driver
        # on second use and later it will take way less time
        pprint(sales_interface.search_no_delay(search_item="howl min", app_id=CommonSteamGames.APP_ID_CSGO))


if __name__ == '__main__':
    UsageWatcher.watcher()
