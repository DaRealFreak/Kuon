#!/usr/bin/python
# -*- coding: utf-8 -*-

from kuon.bitskins.api.interfaces import ISales
from kuon.watcher.adapters import SalesAdapterBase
from tests.watcher.adapters.models.parser.search_response import SearchResponseParser


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
        return SearchResponseParser.parse(self.sales_interface.get_inventory_on_sale(market_hash_name=market_name))

    def get_sold_history(self, market_name):
        """Implementation of get sold history function

        :param market_name:
        :return:
        """
        # ToDo: use search function to get the full market hash name(partial not allowed here)
        return self.sales_interface.get_sales_info(market_hash_name=market_name)

    def get_sold_history_no_delay(self, market_name):
        """Implementation of get sold history no delay function

        :param market_name:
        :return:
        """
        # ToDo: use search function to get the full market hash name(partial not allowed here)
        return self.sales_interface.get_sales_info(market_hash_name=market_name)


if __name__ == '__main__':
    from pprint import pprint
    pprint(SalesAdapter().search("m4 howl min"))
