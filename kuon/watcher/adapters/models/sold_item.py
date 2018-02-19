#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import time

from kuon.watcher.adapters.models import AbstractEntity


class SoldItem(AbstractEntity):

    def __init__(self, market_name: str, price: int, wear_value: float, sold_at: int = int(time())):
        """Initializing function

        :param market_name:
        :param price:
        :param wear_value:
        :param sold_at:
        """
        self._market_name = market_name
        self._price = price
        self._wear_value = wear_value
        self._sold_at = sold_at

    @property
    def value(self):
        return {
            'market_name': self._market_name,
            'price': self._price,
            'wear_value': self._wear_value,
            'sold_at': self._sold_at
        }
