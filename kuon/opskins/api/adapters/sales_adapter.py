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