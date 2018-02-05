#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import threading
from time import time, sleep

from opskins.api.api_response import LockedDict
from opskins.api.interfaces import ISales
from opskins.watcher import Settings
from opskins.watcher.currency import Currency
from opskins.watcher.notifications import Telegram
from opskins.watcher.notifications.mail import Mail
from opskins.watcher.settings import NotificationType


class Watcher(threading.Thread):
    """
    Watcher class to watch tracked items and notify the user on reached conditions
    """

    _mail = None
    _telegram = None

    def __init__(self, log_level=logging.INFO):
        """Initializing function

        :param log_level:
        """
        super().__init__()

        # initialize logger
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger("opskins_watcher")

        self.sales_interface = ISales()
        self.notified_ids = []

        self.validate_settings()
        self.check_conditions()

    def check_conditions(self):
        """The main function, checking the tracked items in a while True loop

        :return:
        """
        while True:
            start_time = time()

            results = self.sales_interface.search("m4 howl min")
            for search_item in results.response.sales:
                # self.notify_user(item=search_item)
                continue

            duration = time() - start_time
            if duration < Settings.check_frequency:
                self.logger.info("sleeping '{:.2f}' seconds".format(Settings.check_frequency - duration))
                sleep(Settings.check_frequency - duration)

    def notify_user(self, item: LockedDict):
        """Notifying the user with the selected option

        :param item:
        :return:
        """
        if item.id in self.notified_ids:
            return False

        item_link = "https://opskins.com/?loc=shop_view_item&item={0:d}".format(item.id)

        if Settings.notification_type == NotificationType.Nothing:
            self.logger.info('Search conditions met on item:\n<a href="{item_link}">{name}({price})</a>'.format(
                item_link=item_link, name=item.market_name, price=Currency(item.amount)))

        if Settings.notification_type == NotificationType.Telegram:
            self.telegram.send_message(
                'Search conditions met on item:\n<a href="{item_link}">{name}({price})</a>'.format(
                    item_link=item_link, name=item.market_name, price=Currency(item.amount)),
                Settings.Notification.Telegram.chat_id, parse_mode="HTML")

        if Settings.notification_type == NotificationType.Mail:
            self.mail.send_message("Search conditions met on item", '<a href="{item_link}">{name}({price})</a>'.format(
                item_link=item_link, name=item.market_name, price=Currency(item.amount)))

            raise NotImplementedError("Mail notification is not implemented yet")

        self.notified_ids.append(item.id)

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
