#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

# covered by python-dotenv
# noinspection PyPackageRequirements
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, '.env')
dotenv.load_dotenv(dotenv_path)


class NotificationType:
    Nothing = 0
    Telegram = 1
    Mail = 2


class Settings:
    """Settings for Watcher"""

    class Notification:
        """Settings for Notifications"""

        class Telegram:
            """Settings for Telegram"""
            token = os.environ.get('TELEGRAM_API_KEY')

            if os.environ.get('TELEGRAM_USER_ID') and os.environ.get('TELEGRAM_USER_ID').isnumeric():
                chat_id = int(os.environ.get('TELEGRAM_USER_ID'))
            else:
                chat_id = 0

        class Mail:
            """Settings for Mail"""
            sender_mail = os.environ.get('MAIL_SENDER_USER')
            sender_pass = os.environ.get('MAIL_SENDER_PASS')
            recipient_mail = os.environ.get('MAIL_RECIPIENT')
            smtp_server = os.environ.get('MAIL_SMTP_SERVER')

            if os.environ.get('MAIL_SMTP_SERVER_PORT') and os.environ.get('MAIL_SMTP_SERVER_PORT').isnumeric():
                smtp_port = int(os.environ.get('MAIL_SMTP_SERVER_PORT'))
            else:
                smtp_port = 587

    LIMIT_60_SECONDS = 20

    if os.environ.get('CHECK_FREQUENCY') and os.environ.get('CHECK_FREQUENCY').isnumeric():
        check_frequency = int(os.environ.get('CHECK_FREQUENCY'))
    else:
        check_frequency = 20

    if os.environ.get('NOTIFICATION_TYPE') and os.environ.get('NOTIFICATION_TYPE').isnumeric():
        notification_type = int(os.environ.get('NOTIFICATION_TYPE'))
    else:
        notification_type = NotificationType.Nothing
