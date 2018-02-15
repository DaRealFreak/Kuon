#!/usr/bin/python
# -*- coding: utf-8 -*-

from kuon.api_response import LockedDict
from kuon.opskins.api.interfaces import ISales, IPricing
from kuon.common import CommonSteamGames
from kuon.watcher.tracker import TrackConditions


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
        return item.amount < settings.value

    def _check_below_average_last_sold(self, item: LockedDict, settings: LockedDict):
        """Check if the value of the item is below the average of the last 20 sold items

        :param item:
        :param settings:
        :return:
        """
        last_sold = self.sales_interface.get_last_sales_no_delay(
            app_id=CommonSteamGames.APP_ID_CSGO,
            market_name='"{market_name}"'.format(market_name=item.market_name)
        )
        average_price = sum([sold_item.amount for sold_item in last_sold.response]) / len(last_sold.response)

        if settings.unit == "%":
            return item.amount < average_price * (1 + settings.value)
        else:
            return item.amount < average_price + settings.value

    def _check_below_cheapest_last_sold(self, item: LockedDict, settings: LockedDict):
        """Check if the value of the item is below the average of the cheapest sold items
        of the last 20 purchases

        :param item:
        :param settings:
        :return:
        """
        last_sold = self.sales_interface.get_last_sales_no_delay(
            app_id=CommonSteamGames.APP_ID_CSGO,
            market_name='"{market_name}"'.format(market_name=item.market_name)
        )
        lowest_price = min([sold_item.amount for sold_item in last_sold.response])

        if settings.unit == "%":
            return item.amount < lowest_price * (1 + settings.value)
        else:
            return item.amount < lowest_price + settings.value

    def check_condition(self, item: LockedDict, settings: LockedDict):
        """Check if the set condition matches on the passed item

        :param item:
        :param settings:
        :return:
        """
        if settings.condition in self.condition_mapping:
            return self.condition_mapping[settings.condition](item, settings)
        else:
            return False
