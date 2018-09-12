#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
from json import JSONDecodeError
from typing import Union


class JsonManager(object):
    """Class used for the file handling and parsing of the tracker.json"""

    json_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir, "tracker.json"))

    @staticmethod
    def save_tracked_items(items: list) -> None:
        """Dump the tracked items into the json file

        :type items: Union[list, tuple]
        :return:
        """
        json.dump(items, open(JsonManager.json_path, "w", encoding="utf-8"))

    @staticmethod
    def get_tracked_items(required_keys: Union[list, tuple] = None) -> list:
        """Load the tracked items from the json file

        :type required_keys: Union[list, tuple]
        :return:
        """
        if required_keys is None:
            required_keys = []

        # return an empty list if file doesn't exist
        if not os.path.exists(JsonManager.json_path) or not os.path.isfile(JsonManager.json_path):
            return []

        # if file is not a valid json file return an empty list, else the parsed list
        try:
            items = json.load(open(JsonManager.json_path, "r", encoding="utf-8"))  # type: list
            # don't include items which don't have all required keys
            return [item for item in items if all([key in item for key in required_keys])]
        except JSONDecodeError:
            return []
