#!/usr/bin/python
# -*- coding: utf-8 -*-

from json.decoder import JSONDecodeError
from typing import Type

from kuon.api_response import LockedDict
from kuon.opskins.api.exceptions import InvalidApiResponseType
from kuon.watcher.adapters import SalesAdapterBase
from kuon.watcher.tracker import TrackConditions


class ConditionChecker:
    """
    Class for checking if the given conditions match the item
    Extra file since there will be more code to come
    """

    def __init__(self, adapter: Type[SalesAdapterBase], *args, **kwargs):
        """Initializing function

        :param adapter:
        """
        self.sales_interface = adapter(*args, **kwargs)
        self.condition_mapping = {
            TrackConditions.BELOW_VALUE: self._check_below_value,
            TrackConditions.BELOW_AVERAGE_LAST_SOLD: self._check_below_average_last_sold,
            TrackConditions.BELOW_CHEAPEST_LAST_SOLD: self._check_below_cheapest_last_sold,
        }

    @staticmethod
    def _check_below_value(item: LockedDict, settings: LockedDict):
        """Check if the value of the item is below the specified search value

        :param item:
        :param settings:
        :return:
        """
        return item.price < settings.value

    def _check_below_average_last_sold(self, item: LockedDict, settings: LockedDict):
        """Check if the value of the item is below the average of the last 20 sold items

        :param item:
        :param settings:
        :return:
        """
        last_sold = self.sales_interface.get_sold_history(
            market_name=item.market_name,
            no_delay=True
        )
        average_price = sum([sold_item.price for sold_item in last_sold.data.sales]) / len(last_sold.data.sales)

        if settings.unit == "%":
            return item.price < average_price * (1 + settings.value)
        else:
            return item.price < average_price + settings.value

    def _check_below_cheapest_last_sold(self, item: LockedDict, settings: LockedDict):
        """Check if the value of the item is below the average of the cheapest sold items
        of the last 20 purchases

        :param item:
        :param settings:
        :return:
        """
        last_sold = self.sales_interface.get_sold_history(
            market_name=item.market_name
        )
        lowest_price = min([sold_item.price for sold_item in last_sold.data.sales])

        if settings.unit == "%":
            return item.price < lowest_price * (1 + settings.value)
        else:
            return item.price < lowest_price + settings.value

    def check_condition(self, item: LockedDict, settings: LockedDict):
        """Check if the set condition matches on the passed item

        :param item:
        :param settings:
        :return:
        """
        if settings.condition in self.condition_mapping:
            try:
                return self.condition_mapping[settings.condition](item, settings)
            except (InvalidApiResponseType, JSONDecodeError, ValueError, AttributeError):
                return False
        else:
            return False
