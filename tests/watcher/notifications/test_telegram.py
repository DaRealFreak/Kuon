#!/usr/bin/python
# -*- coding: utf-8 -*-
from opskins.watcher import Settings
from opskins.watcher.notifications import Telegram

if __name__ == "__main__":
    telegram = Telegram()
    text, chat = telegram.get_last_chat_id_and_text()
    res = telegram.send_message('<a href="https://imgur.com/a/Cdvt5">2B Nier Automata imgur album</a>',
                                Settings.Notification.Telegram.chat_id,
                                parse_mode="HTML", disable_web_page_preview=True)
