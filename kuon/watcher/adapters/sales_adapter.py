#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class SalesAdapterBase:
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        """Initializing function to just not display the warning of unexpected arguments

        :param args:
        :param kwargs:
        """
        pass

    @abstractmethod
    def search(self, market_name, no_delay=False):
        """Search for a specific item

        :param market_name:
        :param no_delay:
        :return:
        """
        pass

    @abstractmethod
    def get_sold_history(self, market_name, no_delay=False):
        """Get the last available sell history

        :param market_name:
        :param no_delay:
        :return:
        """
        pass

    @staticmethod
    @abstractmethod
    def get_item_link(item_id: int):
        """Generate the item link from the item id

        :return:
        """
        pass
