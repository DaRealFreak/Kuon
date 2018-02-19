#!/usr/bin/python
# -*- coding: utf-8 -*-

from kuon.opskins.api.interfaces import ISales
from kuon.watcher.adapters import SalesAdapterBase


class SalesAdapter(SalesAdapterBase):
    """Adapter for the Sales Interface of OPSkins"""

    def __init__(self, *args, **kwargs):
        """Initializing function

        :param args:
        :param kwargs:
        """
        self.sales_interface = ISales(*args, **kwargs)

    def search(self, market_name, no_delay=False):
        """Implementation of the search function

        :param market_name:
        :param no_delay:
        :return:
        """
        # ToDo: unify the units(BitSkins float like 5.50, OPSkins int like 550)
        if no_delay:
            return self.sales_interface.search_no_delay(search_item=market_name)
        else:
            return self.sales_interface.search(search_item=market_name)

    def get_sold_history(self, market_name, no_delay=False):
        """Implementation of get sold history function

        :param market_name:
        :param no_delay:
        :return:
        """
        if no_delay:
            return self.sales_interface.get_last_sales_no_delay(market_name=market_name)
        else:
            return self.sales_interface.get_last_sales(market_name=market_name)
