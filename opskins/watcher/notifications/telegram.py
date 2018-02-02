#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

from opskins.api import APIResponse
from opskins.watcher.settings import Settings


class InvalidApiSettingsException(Exception):
    pass


class Telegram:
    """
    Class to notify the user via telegram bot.
    The telegram API documentation can be found here: https://core.telegram.org/bots/api
    """

    def __init__(self, settings: Settings):
        """Initializing function

        :param settings:
        """
        if not settings.Notification.Telegram.token:
            raise InvalidApiSettingsException('You need an API token to use the Telegram API')

        self._token = settings.Notification.Telegram.token
        self.api_url = "https://api.telegram.org/bot{0:s}".format(self._token)

        bot_profile = self.get_me()
        if not bot_profile.ok:
            raise InvalidApiSettingsException('The provided API key is invalid')

        self._chat_id = settings.Notification.Telegram.chat_id

    def get_me(self):
        """getMe implementation
        https://core.telegram.org/bots/api#getme

        :return:
        """
        api_url = "{0:s}/getMe".format(self.api_url)
        link = requests.get(api_url)
        return APIResponse(link.text)

    def get_updates(self, offset=None, limit=None, timeout=None, allowed_updates=None):
        """getUpdates implementation
        https://core.telegram.org/bots/api#getupdates

        :param offset:
        :param limit:
        :param timeout:
        :param allowed_updates:
        :return:
        """
        api_url = "{0:s}/getUpdates".format(self.api_url)

        payload = {}

        if offset:
            payload['offset'] = offset
        if limit:
            payload['limit'] = limit
        if timeout:
            payload['timeout'] = timeout
        if allowed_updates:
            payload['allowed_updates'] = allowed_updates

        link = requests.get(api_url)
        return APIResponse(link.text)

    def send_message(self, text, chat_id: int, parse_mode=None, disable_web_page_preview=None,
                     disable_notification=False, reply_to_message_id=None, reply_markup=None):
        """sendMessage implementation
        https://core.telegram.org/bots/api#sendmessage

        :param text:
        :param chat_id:
        :param parse_mode:
        :param disable_web_page_preview:
        :param disable_notification:
        :param reply_to_message_id:
        :param reply_markup:
        :return:
        """
        api_url = "{0:s}/sendMessage".format(self.api_url)

        payload = {
            'text': text,
            'chat_id': chat_id
        }

        if parse_mode:
            payload['parse_mode'] = parse_mode
        if disable_web_page_preview:
            payload['disable_web_page_preview'] = disable_web_page_preview
        if disable_notification:
            payload['disable_notification'] = disable_notification
        if reply_to_message_id:
            payload['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            payload['reply_markup'] = reply_markup

        link = requests.get(api_url, params=payload)
        return APIResponse(link.text)

    def get_last_chat_id_and_text(self):
        """Retrieve the last message and chat id

        :return:
        """
        updates = self.get_updates()
        if not updates.result:
            # Bot didn't receive a single message yet
            return None, ""

        last_update = len(updates.result) - 1
        text = updates.result[last_update].message.text
        chat_id = updates.result[last_update].message.chat.id
        return chat_id, text
