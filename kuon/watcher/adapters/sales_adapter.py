#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class SalesAdapterBase:
    __metaclass__ = ABCMeta

    @abstractmethod
    def search(self, market_name):
        """Search for a specific item

        :param market_name:
        :return:
        """
        pass
