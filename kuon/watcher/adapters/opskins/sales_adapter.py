#!/usr/bin/python
# -*- coding: utf-8 -*-

from kuon.opskins.api.interfaces import ISales
from kuon.watcher.adapters import SalesAdapterBase
from kuon.watcher.adapters.opskins.parser import SearchResponseParser, SoldHistoryParser


class OPSkinsSalesAdapter(SalesAdapterBase):
    """Adapter for the Sales Interface of OPSkins"""

    def __init__(self, *args, **kwargs):
        """Initializing function

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.sales_interface = ISales(*args, **kwargs)

    def search(self, market_name, no_delay=False):
        """Implementation of the search function

        :param market_name:
        :param no_delay:
        :return:
        """
        # put market name in double quotation marks to search for the exact market name.
        # else we won't be able to search f.e. for Desert Eagle | Blaze (Factory New) since it will find
        # Desert Eagle | Oxid Blaze (Factory New) too
        market_name = '"{market_name}"'.format(market_name=market_name)

        if no_delay:
            results = self.sales_interface.search_no_delay(search_item=market_name)
        else:
            results = self.sales_interface.search(search_item=market_name)

        return SearchResponseParser.parse(results=results)

    def get_sold_history(self, market_name, no_delay=False):
        """Implementation of get sold history function

        :param market_name:
        :param no_delay:
        :return:
        """
        search_results = self.search(market_name=market_name).data.market_items
        if search_results:
            market_name = search_results[0].market_name

        if no_delay:
            results = self.sales_interface.get_last_sales_no_delay(market_name=market_name)
        else:
            results = self.sales_interface.get_last_sales(market_name=market_name)

        return SoldHistoryParser.parse(results=results)

    @staticmethod
    def get_item_link(item_id: int):
        """Generate the item link from the item id

        :param item_id:
        :return:
        """
        return "https://opskins.com/?loc=shop_view_item&item={0:d}".format(item_id)
