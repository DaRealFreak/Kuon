#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
from json import JSONDecodeError


class JsonManager:
    json_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "tracker.json"))

    @staticmethod
    def save_tracked_items(items: list):
        """Dump the tracked items into the json file

        :return:
        """
        json.dump(items, open(JsonManager.json_path, "w", encoding="utf-8"))

    @staticmethod
    def get_tracked_items() -> list:
        """Load the tracked items from the json file

        :return:
        """
        # return an empty list if file doesn't exist
        if not os.path.exists(JsonManager.json_path) or not os.path.isfile(JsonManager.json_path):
            return []

        # if file is not a valid json file return an empty list, else the parsed list
        try:
            return json.load(open(JsonManager.json_path, "r", encoding="utf-8"))
        except JSONDecodeError:
            return []
