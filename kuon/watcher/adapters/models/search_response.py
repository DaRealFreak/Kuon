#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import time
from typing import List

from kuon.watcher.adapters.models.item import Item
from kuon.watcher.adapters.models.sticker import Sticker


class SearchResponse:

    def __init__(self, success: bool, checked_time: int, items: List[Item] = None):
        self._success = success
        self._time = checked_time

        if items:
            self._items = items
        else:
            self._items = []

    @property
    def value(self):
        return {
            'data': {
                'status': self._success,
                'time': self._time,
                'items': self._items
            }
        }

    def __repr__(self):
        return str(self.value)

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, checked_time):
        self._time = checked_time

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, success: bool):
        self._success = success

    @property
    def items(self):
        return self._items

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


if __name__ == '__main__':
    response = SearchResponse(success=True, checked_time=time())
    example_sticker = Sticker(name="G2 Esports (Holo) | Atlanta 2017",
                              image="https://steamcdn-a.akamaihd.net/apps/730/icons/econ/stickers/atlanta2017/"
                                    "g2_holo.63b73331c6091060936726688b344c47703e5438.png",
                              wear_value=0.43092891573905945)
    example_item = Item(app_id=730, class_id=2720277405, context_id=2, instance_id=188530139, price=109999,
                        wear_value=0.14305446,
                        image="https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZL"
                              "QHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpou-6kejhjxszFJTwT09S5g4yC"
                              "mfDLP7LWnn8f65Mli7DH9tXziQTgqUY4YmmnINSUJwQ-YVnT_wS7yOzngMW07ZrOmmwj5HeObpQQtA/"
                              "256fx256f",
                        inspect_link="steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561198445403"
                                     "072A%item_id%D2351618156038130176",
                        stickers=[example_sticker])
    response.add_item(example_item)
    print(response)
