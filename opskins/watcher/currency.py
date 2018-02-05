#!/usr/bin/python
# -*- coding: utf-8 -*-


class Currency:
    """Class to parse currency amount in a readable format"""

    def __init__(self, cents, currency_sign="$", currency_sign_start=True):
        """Initializing function

        :param cents:
        :param currency_sign:
        :param currency_sign_start:
        """
        self._amount = cents
        self._currency_sign = currency_sign
        self._currency_sign_start = currency_sign_start

    @property
    def human_readable(self):
        """Return the amount in a readable format like $15.00 instead of 1500

        :return:
        """
        if self._currency_sign_start:
            return "{0:s}{1:.2f}".format(self._currency_sign, self._amount / 100)
        else:
            return "{1:.2f}{0:s}".format(self._currency_sign, self._amount / 100)

    @property
    def amount(self):
        """Get the raw amount

        :return:
        """
        return self._amount
