#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from kuon.api_response import APIResponse


class SalesAdapterBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs) -> None:
        """Initializing function to just not display the warning of unexpected arguments

        :type args: list
        :type kwargs: dict
        """
        pass

    @abstractmethod
    def search(self, market_name, no_delay=False) -> APIResponse:
        """Search for a specific item

        :type market_name: str
        :type no_delay: bool
        :return:
        """
        pass

    @abstractmethod
    def get_sold_history(self, market_name, no_delay=False) -> APIResponse:
        """Get the last available sell history

        :type market_name: str
        :type no_delay: bool
        :return:
        """
        pass

    @staticmethod
    @abstractmethod
    def get_item_link(item_id: int) -> str:
        """Generate the item link from the item id

        :return:
        """
        pass
