#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

from kuon.watcher.adapters.models import AbstractEntity
from kuon.watcher.adapters.models.sticker import Sticker


class Item(AbstractEntity):
    """General Item Class"""

    def __init__(self, market_name: str, item_id: str, app_id: int, class_id: int, context_id: int, instance_id: int,
                 price: int, wear_value: float, image: str, inspect_link: str, stickers: List[Sticker] = None) -> None:
        """Initializing function

        :type market_name: str
        :type item_id: str
        :type app_id: int
        :type class_id: int
        :type context_id: int
        :type instance_id: int
        :type price: int
        :type wear_value: float
        :type image: str
        :type inspect_link: str
        :type stickers: List[Sticker]
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
    def value(self) -> dict:
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
    def stickers(self) -> list:
        """Property for stickers which returns __dict__ of the sticker objects
        to allow JSON dump the item without custom JSONEncoder objects

        :return:
        """
        return [s.__dict__ for s in self._stickers]

    @stickers.setter
    def stickers(self, stickers: List[Sticker]) -> None:
        """Setter for sticker

        :type stickers: List[Sticker]
        :return:
        """
        self._stickers = stickers

    def add_sticker(self, sticker: Sticker) -> None:
        """Adder for sticker

        :type sticker: Sticker
        :return:
        """
        if sticker not in self._stickers:
            self._stickers.append(sticker)
