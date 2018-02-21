# !/usr/bin/python
# -*- coding: utf-8 -*-

import json
import unittest

from kuon.watcher.adapters.models.item import Item
from kuon.watcher.adapters.models.sticker import Sticker


class TestItem(unittest.TestCase):
    """
    Test cases for the item model for the properties
    """

    def setUp(self):
        """Set up the sticker to add

        :return:
        """
        self._sticker = Sticker(
            name="Howling Dawn",
            image="some_sticker_image_link",
            wear_value=0.43092
        )

    def test_item(self):
        """Test the conversion to the APIResponse object and the json.dumps

        :return:
        """
        item_1 = Item(
            market_name='some_market_name',
            item_id=12345,
            app_id=730,
            class_id=12345,
            context_id=2,
            instance_id=54321,
            price=109999,
            wear_value=0.14305446,
            image="some_item_image_link",
            inspect_link="some_steam_inspect_link"
        )

        item_1.add_sticker(self._sticker)

        item_2 = Item(
            market_name='some_market_name',
            item_id=12345,
            app_id=730,
            class_id=12345,
            context_id=2,
            instance_id=54321,
            price=109999,
            wear_value=0.14305446,
            image="some_item_image_link",
            inspect_link="some_steam_inspect_link",
            stickers=[self._sticker]
        )

        # check if stickers added at a later moment are added properly
        self.assertEqual(json.dumps(item_1.__dict__), json.dumps(item_2.__dict__))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestItem)
    unittest.TextTestRunner(verbosity=2).run(suite)
