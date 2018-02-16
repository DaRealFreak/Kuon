#!/usr/bin/python
# -*- coding: utf-8 -*-


class Sticker:
    def __init__(self, name: str, image: str, wear_value: float):
        self._name = name
        self._image = image
        self._wear_value = wear_value

    def __dict__(self):
        return self.value

    @property
    def value(self):
        return {
            'name': self._name,
            'image': self._image,
            'wear_value': self._wear_value
        }

    def __repr__(self):
        return str(self.value)
