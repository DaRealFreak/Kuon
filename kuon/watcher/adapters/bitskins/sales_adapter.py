#!/usr/bin/python
# -*- coding: utf-8 -*-

from kuon.bitskins.api.interfaces import ISales
from kuon.watcher.adapters import SalesAdapterBase
from kuon.watcher.adapters.bitskins.parser import SearchResponseParser
from kuon.watcher.adapters.bitskins.parser.sold_history import SoldHistoryParser


class SalesAdapter(SalesAdapterBase):
    """Adapter for the Sales Interface of BitSkins"""

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
        return SearchResponseParser.parse(self.sales_interface.get_inventory_on_sale(market_hash_name=market_name))

    def get_sold_history(self, market_name, no_delay=False):
        """Implementation of get sold history function

        :param market_name:
        :param no_delay:
        :return:
        """
        search_results = self.search(market_name=market_name).data.market_items
        if search_results:
            market_name = search_results[0].name

        return SoldHistoryParser.parse(self.sales_interface.get_sales_info(market_hash_name=market_name))
