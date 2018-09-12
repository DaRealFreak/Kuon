#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.api_response import APIResponse
from kuon.bitskins.api.interfaces import ISales
from kuon.watcher.adapters import SalesAdapterBase
from kuon.watcher.adapters.bitskins.parser import SearchResponseParser, SoldHistoryParser


class BitSkinsSalesAdapter(SalesAdapterBase):
    """Adapter for the Sales Interface of BitSkins"""

    def __init__(self, *args, **kwargs) -> None:
        """Initializing function

        :type args: list
        :type kwargs: dict
        """
        super().__init__(*args, **kwargs)
        self.sales_interface = ISales(*args, **kwargs)

    def search(self, market_name, no_delay=False) -> APIResponse:
        """Implementation of the search function

        :type market_name: str
        :type no_delay: bool
        :return:
        """
        return SearchResponseParser.parse(self.sales_interface.get_inventory_on_sale(market_hash_name=market_name))

    def get_sold_history(self, market_name, no_delay=False) -> APIResponse:
        """Implementation of get sold history function

        :type market_name: str
        :type no_delay: bool
        :return:
        """
        search_results = self.search(market_name=market_name).data.market_items
        if search_results:
            market_name = search_results[0].market_name

        return SoldHistoryParser.parse(self.sales_interface.get_sales_info(market_hash_name=market_name))

    @staticmethod
    def get_item_link(item_id: str) -> str:
        """Generate the item link from the item id

        :type item_id: str
        :return:
        """
        return "https://bitskins.com/view_item?item_id={0:s}".format(item_id)
