#!/usr/bin/python
# -*- coding: utf-8 -*-


class Currency:
    """Class to parse currency amount in a readable format"""

    def __init__(self, amount: int, currency_sign: str = "$", currency_sign_start: bool = True) -> None:
        """Initializing function

        :type amount: int
        :type currency_sign: str
        :type currency_sign_start: bool
        """
        self._amount = amount
        self._currency_sign = currency_sign
        self._currency_sign_start = currency_sign_start

    def __repr__(self) -> str:
        """Return the readable format

        :return:
        """
        return self.human_readable

    @property
    def human_readable(self) -> str:
        """Return the amount in a readable format like $15.00 instead of 1500

        :return:
        """
        if self._currency_sign_start:
            return "{0:s}{1:.2f}".format(self._currency_sign, self._amount / 100)
        else:
            return "{1:.2f}{0:s}".format(self._currency_sign, self._amount / 100)

    @property
    def amount(self) -> int:
        """Get the raw amount

        :return:
        """
        return self._amount
