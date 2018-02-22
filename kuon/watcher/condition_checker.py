#!/usr/bin/python
# -*- coding: utf-8 -*-

from json.decoder import JSONDecodeError
from typing import Type

from kuon.api_response import LockedDict
from kuon.opskins.api.exceptions import InvalidApiResponseType
from kuon.watcher.adapters import SalesAdapterBase
from kuon.watcher.tracker import TrackConditions


class ConditionChecker:
    """Class for checking if the given conditions match the item"""

    _cache = {}

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
    def _check_below_value(item: LockedDict, condition: LockedDict):
        """Check if the value of the item is below the specified search value

        :param item:
        :param condition:
        :return:
        """
        return item[condition.key] < condition.value

    def _check_below_average_last_sold(self, item: LockedDict, condition: LockedDict):
        """Check if the value of the item is below the average of the last 20 sold items

        :param item:
        :param condition:
        :return:
        """
        last_sold = self.get_sold_history(market_name=item.market_name, no_delay=True)
        avg_value = sum([sold_item[condition.key] for sold_item in last_sold.data.sales]) / len(last_sold.data.sales)

        if condition.unit == "%":
            return item[condition.key] < avg_value * (1 + condition.value)
        else:
            return item[condition.key] < avg_value + condition.value

    def _check_below_cheapest_last_sold(self, item: LockedDict, condition: LockedDict):
        """Check if the value of the item is below the average of the cheapest sold items
        of the last 20 purchases

        :param item:
        :param condition:
        :return:
        """
        last_sold = self.get_sold_history(market_name=item.market_name, no_delay=True)
        lowest_value = min([sold_item[condition.key] for sold_item in last_sold.data.sales])

        if condition.unit == "%":
            return item[condition.key] < lowest_value * (1 + condition.value)
        else:
            return item[condition.key] < lowest_value + condition.value

    def check_condition(self, item: LockedDict, settings: LockedDict):
        """Check if the set condition matches on the passed item

        :param item:
        :param settings:
        :return:
        """
        try:
            return all([self.condition_mapping[cond.condition](item, cond) for cond in settings.conditions])
        except (InvalidApiResponseType, JSONDecodeError, ValueError, AttributeError):
            return False

    def get_sold_history(self, market_name, no_delay=False):
        """Cache the sold history entries to execute less queries

        :param market_name:
        :param no_delay:
        :return:
        """
        if market_name not in self._cache:
            self._cache[market_name] = {}

        if no_delay not in self._cache[market_name]:
            last_sold = self.sales_interface.get_sold_history(
                market_name=market_name,
                no_delay=True
            )
            self._cache[market_name][no_delay] = last_sold
        return self._cache[market_name][no_delay]

    def clear_sold_history_cache(self):
        """Clear the sold history cache

        :return:
        """
        self._cache = {}
