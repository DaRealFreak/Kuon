#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

from opskins import OPSkins
from opskins.api import APIResponse
from opskins.api.common import *
from opskins.api.exceptions import *


class ICashout(OPSkins):
    """The ICashout interface of OPSkins"""

    def __init__(self):
        """Initializing function"""
        super().__init__()

    def get_address(self, processor=Processor.PAYPAL):
        """GetAddress v1 implementation
        https://opskins.com/kb/api-icashout#method-getaddress-v1

        :param processor:
        :return:
        """
        api_url = "https://api.opskins.com/ICashout/GetAddress/v1/"

        if not processor:
            raise MissingArgumentException('The function get_address requires the argument "processor"')

        payload = {
            'processor': str(processor)
        }

        link = requests.get(url=api_url, params=payload, headers=self._headers)
        return APIResponse(link.text)

    def set_address(self, address: str, processor=Processor.PAYPAL, twofactor_code=None):
        """SetAddress v1 implementation
        https://opskins.com/kb/api-icashout#method-setaddress-v1

        Two Factor Authentication Code is optional if no address is set yet

        :param address:
        :param processor:
        :param twofactor_code:
        :return:
        """
        api_url = "https://api.opskins.com/ICashout/SetAddress/v1/"

        if not processor:
            raise MissingArgumentException('The function set_address requires the argument "processor"')

        payload = {
            "address": address,
            "processor": str(processor)
        }

        if twofactor_code:
            payload['twofactor_code'] = str(twofactor_code)

        link = requests.post(url=api_url, data=payload, headers=self._headers)
        return APIResponse(link.text)

    def get_pending_cashouts(self):
        """GetPendingCashouts v1 implementation
        https://opskins.com/kb/api-icashout#method-getpendingcashouts-v1

        :return:
        """
        api_url = "https://api.opskins.com/ICashout/GetPendingCashouts/v1/"

        link = requests.get(url=api_url, headers=self._headers)
        return APIResponse(link.text)

    def cancel_pending_cashout(self, cashout_id):
        """CancelPendingCashout v1 implementation
        https://opskins.com/kb/api-icashout#method-cancelpendingcashout-v1

        :param cashout_id:
        :return:
        """
        api_url = "https://api.opskins.com/ICashout/CancelPendingCashout/v1/"

        payload = {
            "cashoutid": cashout_id
        }

        link = requests.post(url=api_url, data=payload, headers=self._headers)
        return APIResponse(link.text)

    def get_bitcoin_instant_cashout_rate(self):
        """GetBitcoinInstantCashoutRate v1 implementation
        https://opskins.com/kb/api-icashout#method-getbitcoininstantcashoutrate-v1

        Get the current approximate BTC/USD exchange rate which will be used if you request an instant Bitcoin cashout.

        :return:
        """
        api_url = "https://api.opskins.com/ICashout/GetBitcoinInstantCashoutRate/v1/"

        link = requests.get(url=api_url, headers=self._headers)
        return APIResponse(link.text)

    def request_paypal(self, amount: int, priority=Cashout.REGULAR):
        """RequestPayPal v1 implementation
        https://opskins.com/kb/api-icashout#method-requestpaypal-v1

        :param amount:
        :param priority:
        :return:
        """
        api_url = "https://api.opskins.com/ICashout/RequestPayPal/v1/"

        payload = {
            "amount": str(amount),
            "priority": priority
        }

        link = requests.post(url=api_url, data=payload, headers=self._headers)
        return APIResponse(link.text)

    def request_bitcoin(self, amount: int, priority=Cashout.REGULAR):
        """RequestBitcoin v1 implementation
        https://opskins.com/kb/api-icashout#method-requestbitcoin-v1

        :param amount:
        :param priority:
        :return:
        """
        api_url = "https://api.opskins.com/ICashout/RequestBitcoin/v1/"

        payload = {
            "amount": str(amount),
            "priority": priority
        }

        link = requests.post(url=api_url, data=payload, headers=self._headers)
        return APIResponse(link.text)

    def request_skrill(self, amount: int):
        """RequestSkrill v1 implementation
        https://opskins.com/kb/api-icashout#method-requestskrill-v1

        :param amount:
        :return:
        """
        api_url = "https://api.opskins.com/ICashout/RequestSkrill/v1/"

        payload = {
            "amount": str(amount)
        }

        link = requests.post(url=api_url, data=payload, headers=self._headers)
        return APIResponse(link.text)

    def get_cashout_balance(self):
        """GetCashoutableBalance v1 implementation
        https://opskins.com/kb/api-icashout#method-getcashoutablebalance-v1

        :return:
        """
        api_url = "https://api.opskins.com/ICashout/GetCashoutableBalance/v1/"

        link = requests.get(url=api_url, headers=self._headers)
        return APIResponse(link.text)
