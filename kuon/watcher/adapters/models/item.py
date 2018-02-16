#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from kuon.watcher.adapters.models.sticker import Sticker


class Item:

    def __init__(self, app_id: int, class_id: int, context_id: int, instance_id: int, price: int, wear_value: float,
                 image: str, inspect_link: str, stickers: List[Sticker] = None):
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
        return {
            'app_id': self._app_id,
            'class_id': self._class_id,
            'context_id': self._context_id,
            'instance_id': self._instance_id,
            'price': self._price,
            'wear_value': self._wear_value,
            'image': self._image,
            'inspect_link': self._inspect_link,
            'stickers': self._stickers
        }

    def __repr__(self):
        return str(self.value)
