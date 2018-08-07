#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from kuon.watcher.adapters.models import AbstractEntity
from kuon.watcher.adapters.models.sticker import Sticker


class Item(AbstractEntity):
    """General Item Class"""

    def __init__(self, market_name: str, item_id: str, app_id: int, class_id: int, context_id: int, instance_id: int,
                 price: int, wear_value: float, image: str, inspect_link: str, stickers: List[Sticker] = None):
        """Initializing function

        :param market_name:
        :param item_id:
        :param app_id:
        :param class_id:
        :param context_id:
        :param instance_id:
        :param price:
        :param wear_value:
        :param image:
        :param inspect_link:
        :param stickers:
        """
        self._market_name = market_name
        self._item_id = item_id
        self._app_id = app_id
        self._class_id = class_id
        self._context_id = context_id
        self._instance_id = instance_id
        self._price = price
        self._wear_value = wear_value
        self._image = image
        self._inspect_link = inspect_link

        if stickers:
            self._stickers = stickers
        else:
            self._stickers = []

    @property
    def value(self):
        """Return all important information from the Steam API

        :return:
        """
        return {
            'market_name': self._market_name,
            'item_id': self._item_id,
            'app_id': self._app_id,
            'class_id': self._class_id,
            'context_id': self._context_id,
            'instance_id': self._instance_id,
            'price': self._price,
            'wear_value': self._wear_value,
            'image': self._image,
            'inspect_link': self._inspect_link,
            'stickers': self.stickers
        }

    @property
    def stickers(self):
        """Property for stickers which returns __dict__ of the sticker objects
        to allow JSON dump the item without custom JSONEncoder objects

        :return:
        """
        return [s.__dict__ for s in self._stickers]

    @stickers.setter
    def stickers(self, stickers: List[Sticker]):
        """Setter for sticker

        :param stickers:
        :return:
        """
        self._stickers = stickers

    def add_sticker(self, sticker: Sticker):
        """Adder for sticker

        :param sticker:
        :return:
        """
        if sticker not in self._stickers:
            self._stickers.append(sticker)
