#!/usr/bin/python
# -*- coding: utf-8 -*-

from opskins.api.api_response import LockedDict
from opskins.api.interfaces import ISales
from opskins.watcher.tracker import TrackConditions


class ConditionChecker:
    """
    Class for checking if the given conditions match the item
    Extra file since there will be more code to come
    """

    def __init__(self, *args, **kwargs):
        """Initializing function

        :param sales_interface:
        """
        self.sales_interface = ISales(*args, **kwargs)

    def check_condition(self, item: LockedDict, settings: LockedDict):
        """Check if the set condition matches on the passed item

        :param item:
        :param settings:
        :return:
        """
        # ToDo: implement
        if settings.condition == TrackConditions.BELOW_VALUE:
            return item.amount < settings.value
        if settings.condition == TrackConditions.BELOW_AVERAGE:
            # ToDo: calculate average of last sold items, differentiate % and # units
            return False
        if settings.condition == TrackConditions.BELOW_CHEAPEST_LAST_SOLD:
            # ToDo: get last sold, sort by price, differentiate % and # units
            return False
        if settings.condition == TrackConditions.ALL_TIME_LOW:
            # ToDo: get lowest price sold, ignore units
            return False
        else:
            return False
