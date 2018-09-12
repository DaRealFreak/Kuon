#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.watcher.notifications.mail import Mail
from kuon.watcher.notifications.telegram import Telegram

__all__ = [
    Telegram.__name__,
    Mail.__name__
]
