#!/usr/bin/python
# -*- coding: utf-8 -*-

from kuon.bitskins.api.interfaces import ISales
from kuon.watcher.adapters import SalesAdapterBase


class SalesAdapter(SalesAdapterBase):
    """Adapter for the Sales Interface of BitSkins"""

    def __init__(self, *args, **kwargs):
        """Initializing function

        :param args:
        :param kwargs:
        """
        self.sales_interface = ISales(*args, **kwargs)

    def search(self, market_name):
        """Implementation of the search function

        :param market_name:
        :return:
        """
        # ToDo: unify the units(BitSkins float like 5.50, OPSkins int like 550)
        return self.sales_interface.get_inventory_on_sale(market_hash_name=market_name)

    def search_no_delay(self, market_name):
        """Implementation of the search no delay function

        :param market_name:
        :return:
        """
        # ToDo: unify the units(BitSkins float like 5.50, OPSkins int like 550)
        return self.sales_interface.get_inventory_on_sale(market_hash_name=market_name)
