#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import time
from typing import List

from kuon.watcher.adapters.models import AbstractEntity
from kuon.watcher.adapters.models.item import Item


class SearchResponse(AbstractEntity):
    """General Search Response from the APIs"""

    def __init__(self, success: bool, checked_time: int = int(time()), items: List[Item] = None):
        """Initializing function

        :param success:
        :param checked_time:
        :param items:
        """
        self._success = success
        self._time = checked_time

        if items:
            self._items = items
        else:
            self._items = []

    @property
    def value(self):
        """Return all important information regarding the search API call like success, time and items

        :return:
        """
        return {
            'data': {
                'status': self._success,
                'time': self._time,
                'items': self.items
            }
        }

    @property
    def items(self):
        """Property for items which returns __dict__ of the item objects
        to allow JSON dump the search response without custom JSONEncoder objects

        :return:
        """
        return [i.__dict__ for i in self._items]

    @items.setter
    def items(self, items: List[Item]):
        """Setter for items

        :param items:
        :return:
        """
        self._items = items

    def add_item(self, item: Item):
        """Adder for items

        :param item:
        :return:
        """
        if item not in self._items:
            self._items.append(item)
