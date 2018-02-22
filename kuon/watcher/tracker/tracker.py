#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging

from kuon.api_response import LockedDict, LockedList
from kuon.watcher.tracker.json_manager import JsonManager


class TrackConditions:
    BELOW_VALUE = 0
    BELOW_AVERAGE_LAST_SOLD = 1
    BELOW_CHEAPEST_LAST_SOLD = 2


class Tracker:
    """Class to track search terms with conditions"""

    ITEM_REQUIRED_KEYWORDS = ('search_item', 'conditions')

    def __init__(self, log_level=logging.ERROR):
        """Initializing function"""
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger("opskins_tracker")

        self._json_manager = JsonManager()
        self._tracked_items = self._json_manager.get_tracked_items(self.ITEM_REQUIRED_KEYWORDS)

    @property
    def tracked_items(self):
        """Get the tracked items as LockedList

        :return:
        """
        return LockedList(self._tracked_items)

    def add_item(self, item: LockedDict):
        """Adds an item to the tracking list

        :param item:
        :return:
        """
        if not all([key in item for key in Tracker.ITEM_REQUIRED_KEYWORDS]):
            self.logger.error('Not all required keywords ({keywords}) are in the added item'.format(
                keywords=",".join(Tracker.ITEM_REQUIRED_KEYWORDS)))
            return

        if item not in self._tracked_items:
            self._tracked_items.append(item)
            self._json_manager.save_tracked_items(self._tracked_items)

    def remove_item(self, item: LockedDict):
        """Removes an item from the tracking list

        :param item:
        :return:
        """
        if item in self._tracked_items:
            self._tracked_items.remove(item)
            self._json_manager.save_tracked_items(self._tracked_items)
