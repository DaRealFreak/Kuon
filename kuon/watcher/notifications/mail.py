#!/usr/bin/python
# -*- coding: utf-8 -*-
from smtplib import SMTP, SMTPAuthenticationError

from kuon.watcher import Settings


class InvalidSMTPSettingsException(Exception):
    pass


class InvalidMailSettingsException(Exception):
    pass


class Mail(object):
    """
    Class to notify the user via mail.
    """

    def __init__(self) -> None:
        """Initializing action. Validate SMTP connection and user settings"""
        self._smtp = SMTP(host=Settings.Notification.Mail.smtp_server, port=Settings.Notification.Mail.smtp_port)
        self._smtp.ehlo()
        self._smtp.starttls()

        # status code 250 is OK
        response = self._smtp.noop()
        if not response[0] == 250:
            raise InvalidSMTPSettingsException('Invalid SMTP Server settings')

        try:
            self._smtp.login(Settings.Notification.Mail.sender_mail, Settings.Notification.Mail.sender_pass)
        except SMTPAuthenticationError:
            raise InvalidMailSettingsException('Invalid user credentials for the SMTP server')

    def __del__(self) -> None:
        """Destructor"""
        self._smtp.close()

    def send_message(self, subject: str, text: str) -> None:
        """Send a mail to the configured mail

        :type subject:
        :type text:
        :return:
        """
        text = '\r\n'.join(['To: %s' % Settings.Notification.Mail.recipient_mail,
                            'From: %s' % Settings.Notification.Mail.sender_mail,
                            'Subject: %s' % subject,
                            '', text])

        self._smtp.sendmail(Settings.Notification.Mail.sender_mail, Settings.Notification.Mail.recipient_mail, text)
