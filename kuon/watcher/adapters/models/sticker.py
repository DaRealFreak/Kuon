#!/usr/bin/python
# -*- coding: utf-8 -*-

from kuon.watcher.adapters.models import AbstractEntity


class Sticker(AbstractEntity):
    """General Sticker Class"""

    def __init__(self, name: str, image: str, wear_value: float):
        """Initializing function

        :param name:
        :param image:
        :param wear_value:
        """
        self._name = name
        self._image = image
        self._wear_value = wear_value

    @property
    def value(self):
        """Return all important information regarding the Stickers

        :return:
        """
        return {
            'name': self._name,
            'image': self._image,
            'wear_value': self._wear_value
        }
