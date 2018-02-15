#!/usr/bin/python
# -*- coding: utf-8 -*-

from kuon.watcher.adapters import SalesAdapterBase
from kuon.opskins.api.interfaces import ISales


class SalesAdapter(SalesAdapterBase):
    """Adapter for the Sales Interface of OPSkins"""

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
        return self.sales_interface.search(search_item=market_name)

    def search_no_delay(self, market_name):
        """Implementation of the search no delay function

        :param market_name:
        :return:
        """
        # ToDo: unify the units(BitSkins float like 5.50, OPSkins int like 550)
        return self.sales_interface.search_no_delay(search_item=market_name)

    def get_sold_history(self, market_name):
        """Implementation of get sold history function

        :param market_name:
        :return:
        """
        return self.sales_interface.get_last_sales(market_name=market_name)

    def get_sold_history_no_delay(self, market_name):
        """Implementation of get sold history no delay function

        :param market_name:
        :return:
        """
        return self.sales_interface.get_last_sales_no_delay(market_name=market_name)