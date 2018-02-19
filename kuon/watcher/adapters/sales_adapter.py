#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class SalesAdapterBase:
    __metaclass__ = ABCMeta

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
