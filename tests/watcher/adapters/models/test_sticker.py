# !/usr/bin/python
# -*- coding: utf-8 -*-
import json
import unittest

from kuon.api_response import APIResponse
from kuon.watcher.adapters.models.sticker import Sticker


class TestSticker(unittest.TestCase):
    """Test cases for the sticker model"""

    def test_sticker(self) -> None:
        """Test the conversion to the APIResponse object and the json.dumps

        :return:
        """
        sticker = Sticker(
            name="Howling Dawn",
            image="some_sticker_image_link",
            wear_value=0.43092
        )

        # assert that all values can get loaded properly and parsed to APIResponse objects
        self.assertEqual(str(sticker), str(APIResponse(json.dumps(sticker.__dict__))))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSticker)
    unittest.TextTestRunner(verbosity=2).run(suite)
