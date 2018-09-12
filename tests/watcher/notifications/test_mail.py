#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.watcher.notifications.mail import Mail

if __name__ == "__main__":
    mail = Mail()
    mail.send_message('Mail Test', '<a href="https://imgur.com/a/Cdvt5">2B Nier Automata imgur album</a>')
