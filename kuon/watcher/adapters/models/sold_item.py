#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import time

from kuon.watcher.adapters.models import AbstractEntity


class SoldItem(AbstractEntity):

    def __init__(self, price: int, wear_value: float, sold_at: [float, int] = time()) -> None:
        """Initializing function

        :type price:
        :type wear_value:
        :type sold_at:
        """
        self._price = price
        self._wear_value = wear_value
        self._sold_at = int(sold_at)

    @property
    def value(self) -> dict:
        """Return all important information from the API response like price, wear value and the time it was sold

        :return:
        """
        return {
            'price': self._price,
            'wear_value': self._wear_value,
            'sold_at': self._sold_at
        }
