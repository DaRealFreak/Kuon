#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.api_response import APIResponse
from kuon.bitskins import BitSkins
from kuon.bitskins.common import *


class ICashout(BitSkins):
    """Implementation of the API methods related to the cashout on BitSkins"""

    def __init__(self, *args, **kwargs) -> None:
        """Initializing function

        :type args: list
        :type kwargs: dict
        """
        super().__init__(*args, **kwargs)

    def request_withdrawal(self, amount: float, withdrawal_method: str = Processor.PAYPAL) -> APIResponse:
        """MoneyWithdrawal v1 implementation
        https://bitskins.com/api/#request_withdrawal

        :type amount: float
        :type withdrawal_method: str
        :return:
        """
        api_url = "https://bitskins.com/api/v1/request_withdrawal/"

        payload = {
            'amount': str(amount),
            'withdrawal_method': withdrawal_method
        }

        return self.api_request(api_url=api_url, params=payload)
