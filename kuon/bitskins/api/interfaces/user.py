#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.api_response import APIResponse
from kuon.bitskins import BitSkins


class IUser(BitSkins):
    """Implementation of the API methods related to the user on BitSkins"""

    def __init__(self, *args, **kwargs) -> None:
        """Initializing function

        :type args: list
        :type kwargs: dict
        """
        super().__init__(*args, **kwargs)

    def get_account_balance(self) -> APIResponse:
        """GetAccountBalance v1 implementation
        https://bitskins.com/api/#get_account_balance

        :return:
        """
        api_url = "https://bitskins.com/api/v1/get_account_balance/"

        return self.api_request(api_url=api_url)
