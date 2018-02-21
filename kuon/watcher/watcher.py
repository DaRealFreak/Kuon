#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import threading
from time import time, sleep
from typing import Type

from kuon.api_response import LockedDict
from kuon.watcher import Settings
from kuon.watcher.adapters import SalesAdapterBase
from kuon.watcher.condition_checker import ConditionChecker
from kuon.watcher.currency import Currency
from kuon.watcher.notifications import Telegram
from kuon.watcher.notifications.mail import Mail
from kuon.watcher.settings import NotificationType
from kuon.watcher.tracker import Tracker


class Watcher(threading.Thread):
    """
    Watcher class to watch tracked items and notify the user on reached conditions
    """

    _mail = None
    _telegram = None

    def __init__(self, adapter: Type[SalesAdapterBase], log_level=logging.ERROR, *args, **kwargs):
        """Initializing function

        :param log_level:
        """
        super().__init__()

        # initialize logger
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger(adapter.__name__)

        self.sales_interface = adapter(*args, **kwargs)
        self._item_tracker = Tracker()
        self.condition_checker = ConditionChecker(adapter, *args, **kwargs)
        self.checked_ids = []

        self.validate_settings()
        self.run()

    def run(self):
        """The main function, checking the tracked items in a while True loop

        :return:
        """
        while True:
            start_time = time()

            for tracked_item in self._item_tracker.tracked_items:
                track_index = self._item_tracker.tracked_items.index(tracked_item)
                results = self.sales_interface.search(market_name=tracked_item.search_item, no_delay=True)

                for search_item in results.data.market_items:

                    if (track_index, search_item.item_id) in self.checked_ids:
                        # if we reach the part where we already notified the user
                        # we can break the loop
                        self.logger.debug("already notified user about item: {item}".format(item=search_item.item_id))
                        break

                    if self.condition_checker.check_condition(item=search_item, settings=tracked_item):
                        # condition matches and user didn't get notified yet
                        self.logger.info("conditions ({cond}) met for item: {item}(${price:.2f})({id})".format(
                            cond=tracked_item, item=search_item.market_name, price=search_item.price / 100,
                            id=search_item.item_id))
                        self.notify_user(item=search_item)
                        self.checked_ids.append((track_index, search_item.item_id))

                    else:
                        # Currently only price conditions are implemented so we can break if the condition is not met
                        # since the default sorting is ascending by price
                        self.logger.info("conditions ({cond}) not met for item: {item}(${price:.2f})({id})".format(
                            cond=tracked_item, item=search_item.market_name, price=search_item.price / 100,
                            id=search_item.item_id))
                        self.checked_ids.append((track_index, search_item.item_id))
                        break

            duration = time() - start_time
            if duration < Settings.check_frequency:
                self.logger.info("sleeping '{:.2f}' seconds".format(Settings.check_frequency - duration))
                sleep(Settings.check_frequency - duration)

    def notify_user(self, item: LockedDict):
        """Notifying the user with the selected option

        :param item:
        :return:
        """
        if item.item_id in self.checked_ids:
            return False

        item_link = self.sales_interface.get_item_link(item.item_id)

        if Settings.notification_type == NotificationType.Nothing:
            self.logger.info('Search conditions met on item:\n<a href="{item_link}">{name}({price})</a>'.format(
                item_link=item_link, name=item.market_name, price=Currency(item.price)))

        if Settings.notification_type == NotificationType.Telegram:
            self.telegram.send_message(
                'Search conditions met on item:\n<a href="{item_link}">{name}({price})</a>'.format(
                    item_link=item_link, name=item.market_name, price=Currency(item.price)),
                Settings.Notification.Telegram.chat_id, parse_mode="HTML")

        if Settings.notification_type == NotificationType.Mail:
            self.mail.send_message("Search conditions met on item", '<a href="{item_link}">{name}({price})</a>'.format(
                item_link=item_link, name=item.market_name, price=Currency(item.price)))

            raise NotImplementedError("Mail notification is not implemented yet")

    def validate_settings(self):
        """Validate the settings and overwrite the invalid settings

        :return:
        """
        if Settings.check_frequency < (60 / Settings.LIMIT_60_SECONDS):
            self.logger.info("check frequency was too high, set to {0:d}s".format(60 / Settings.LIMIT_60_SECONDS))
            Settings.check_frequency = 60 / Settings.LIMIT_60_SECONDS

    @property
    def mail(self):
        """Property for Mail class to only initialize it on usage"""
        if not self._mail:
            self._mail = Mail()
        return self._mail

    @property
    def telegram(self):
        """Property for Telegram class to only initialize it on usage"""
        if not self._telegram:
            self._telegram = Telegram()
        return self._telegram
