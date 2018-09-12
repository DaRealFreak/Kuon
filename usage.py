#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This is an example usage
import logging
from pprint import pprint

import kuon.bitskins.api.interfaces as bitskins_interfaces
import kuon.watcher.adapters.bitskins as bitskins_adapters
from kuon.watcher import Watcher


class UsageWatcher(object):
    """Example usage for the watcher class of Kuon"""

    @staticmethod
    def watcher() -> None:
        """Example watcher usage

        :return:
        """
        Watcher(adapter=bitskins_adapters.BitSkinsSalesAdapter, log_level=logging.DEBUG).start()


class UsageBitSkins(object):
    """Example usages for the implementation of the BitSkins API"""

    @staticmethod
    def sales_adapter() -> None:
        sales_adapter = bitskins_adapters.BitSkinsSalesAdapter()
        pprint(sales_adapter.search("m4 howl min"))

    @staticmethod
    def sales_interface() -> None:
        """Example sales interface usage

        :return:
        """
        sales_interface = bitskins_interfaces.ISales()

        pprint(sales_interface.get_sales_info(market_hash_name="M4A4 | Howl (Factory New)"))

    @staticmethod
    def pricing_interface() -> None:
        """Example pricing interface usage

        :return:
        """
        pricing_interface = bitskins_interfaces.IPricing()
        pprint(pricing_interface.get_all_item_prices())
        pprint(pricing_interface.get_price_data_for_items_on_sale())

    @staticmethod
    def inventory_interface() -> None:
        """Example pricing interface usage

        :return:
        """
        inventory_interface = bitskins_interfaces.IInventory()
        pprint(inventory_interface.get_my_inventory())


if __name__ == '__main__':
    UsageWatcher().watcher()
