#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

from opskins import OPSkins
from opskins.api import APIResponse


class IUser(OPSkins):
    """The IUser interface of OPSkins"""

    def __init__(self):
        """Initializing function"""
        super().__init__()

    def get_balance(self):
        """GetBalance v1 implementation
        https://opskins.com/kb/api-iuser#method-getbalance-v1

        :return:
        """
        api_url = "https://api.opskins.com/IUser/GetBalance/v1/"

        link = requests.get(url=api_url, headers=self._headers)
        return APIResponse(link.text)

    def save_trade_url(self, trade_url: str):
        """SaveTradeURL v1 implementation
        https://opskins.com/kb/api-iuser#method-savetradeurl-v1

        :param trade_url:
        :return:
        """
        api_url = "https://api.opskins.com/IUser/SaveTradeURL/v1/"

        payload = {
            'trade_url': trade_url,
        }

        link = requests.post(url=api_url, data=payload, headers=self._headers)
        return APIResponse(link.text)
