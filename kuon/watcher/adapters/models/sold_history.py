#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from kuon.watcher.adapters.models import AbstractEntity
from kuon.watcher.adapters.models.sold_item import SoldItem


class SoldHistory(AbstractEntity):
    """General Sold History Response from the APIs"""

    def __init__(self, success: bool, sold_items: List[SoldItem] = None):
        """Initializing function

        :param success:
        :param sold_items:
        """
        self._success = success

        if sold_items:
            self._sold_items = sold_items
        else:
            self._sold_items = []

    @property
    def value(self):
        """Return all important information from the API response like success and sold items

        :return:
        """
        return {
            'data': {
                'success': self._success,
                'sales': self.sold_items
            }
        }

    @property
    def sold_items(self):
        """Property for sold items which returns __dict__ of the sold item objects
        to allow JSON dump the search response without custom JSONEncoder objects

        :return:
        """
        return [i.__dict__ for i in self._sold_items]

    @sold_items.setter
    def sold_items(self, sold_items: List[SoldItem]):
        """Setter for sold items

        :param sold_items:
        :return:
        """
        self._sold_items = sold_items

    def add_sale(self, sold_item: SoldItem):
        """Adder for sold items

        :param sold_item:
        :return:
        """
        if sold_item not in self._sold_items:
            self._sold_items.append(sold_item)
