#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from kuon.watcher.currency import Currency


class TestCurrency(unittest.TestCase):
    """
    test cases for the currency module of the watcher
    """

    def test_usd(self):
        """Test currency with default settings(sign = $ and sign before the amount)

        :return:
        """
        currency = Currency(1501)
        self.assertEqual(str(currency), currency.human_readable)
        self.assertEqual(currency.human_readable, "$15.01")
        self.assertEqual(currency.amount, 1501)

    def test_eur(self):
        """Test currency with euro settings(sign = € and sign after the amount)

        :return:
        """
        currency = Currency(4201, currency_sign="€", currency_sign_start=False)
        self.assertEqual(str(currency), currency.human_readable)
        self.assertEqual(currency.human_readable, "42.01€")
        self.assertEqual(currency.amount, 4201)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCurrency)
    unittest.TextTestRunner(verbosity=2).run(suite)
