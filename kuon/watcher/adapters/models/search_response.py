#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import time
from typing import List

from kuon.watcher.adapters.models import AbstractEntity
from kuon.watcher.adapters.models.item import Item


class SearchResponse(AbstractEntity):
    """General Search Response from the APIs"""

    def __init__(self, success: bool, checked_time: [float, int] = time(), items: List[Item] = None) -> None:
        """Initializing function

        :type success:
        :type checked_time:
        :type items:
        """
        self._success = success
        self._time = int(checked_time)

        if items:
            self._items = items
        else:
            self._items = []

    @property
    def value(self) -> dict:
        """Return all important information regarding the search API call like success, time and items

        :return:
        """
        return {
            'data': {
                'success': self._success,
                'time': self._time,
                # market_items since using "items" will return the built-in function in APIResponse
                'market_items': self.items
            }
        }

    @property
    def items(self) -> list:
        """Property for items which returns __dict__ of the item objects
        to allow JSON dump the search response without custom JSONEncoder objects

        :return:
        """
        return [i.__dict__ for i in self._items]

    @items.setter
    def items(self, items: List[Item]) -> None:
        """Setter for items

        :type items: List[Item]
        :return:
        """
        self._items = items

    def add_item(self, item: Item) -> None:
        """Adder for items

        :type item: Item
        :return:
        """
        if item not in self._items:
            self._items.append(item)
