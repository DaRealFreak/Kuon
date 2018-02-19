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

    def search(self, market_name):
        """Implementation of the search function

        :param market_name:
        :return:
        """
        return SearchResponseParser.parse(self.sales_interface.get_inventory_on_sale(market_hash_name=market_name))

    def search_no_delay(self, market_name):
        """Implementation of the search no delay function

        :param market_name:
        :return:
        """
        return self.search(market_name=market_name)

    def get_sold_history(self, market_name):
        """Implementation of get sold history function

        :param market_name:
        :return:
=        """
        search_results = self.search(market_name=market_name).data.market_items
        if search_results:
            market_name = search_results[0].name

        return SoldHistoryParser.parse(self.sales_interface.get_sales_info(market_hash_name=market_name))

    def get_sold_history_no_delay(self, market_name):
        """Implementation of get sold history no delay function

        :param market_name:
        :return:
        """
        return self.get_sold_history(market_name=market_name)
