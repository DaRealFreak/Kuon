#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

import requests

from kuon.opskins import APIResponse, OPSkins
from kuon.opskins.api.exceptions import *
from kuon.decorators import deprecated


class IInventory(OPSkins):
    """The IInventory interface of OPSkins"""

    def __init__(self, *args, **kwargs):
        """Initializing function"""
        super().__init__(*args, **kwargs)

    def get_inventory(self, page=None, per_page=None) -> APIResponse:
        """GetInventory v2 implementation
        https://opskins.com/kb/api-iinventory#method-getinventory-v2

        :param page:
        :param per_page:
        :return:
        """
        api_url = "https://api.opskins.com/IInventory/GetInventory/v2/"

        payload = {}

        if page:
            payload['page'] = str(page)
        if per_page:
            payload['per_page'] = str(per_page)

        link = requests.get(url=api_url, params=payload, headers=self._headers)
        return APIResponse(link.text)

    @deprecated
    def get_inventory_v1(self) -> APIResponse:
        """GetInventory v1 implementation
        https://opskins.com/kb/api-iinventory#method-getinventory-v1

        :return:
        """
        api_url = "https://api.opskins.com/IInventory/GetInventory/v1/"

        link = requests.get(url=api_url, headers=self._headers)
        return APIResponse(link.text)

    def withdraw(self, items: list) -> APIResponse:
        """Withdraw v1 implementation
        https://opskins.com/kb/api-iinventory#method-withdraw-v1

        :param items:
        :return:
        """
        api_url = "https://api.opskins.com/IInventory/Withdraw/v1/"

        payload = {
            'items': ",".join([str(item) for item in items])
        }

        link = requests.post(url=api_url, data=payload, headers=self._headers)
        return APIResponse(link.text)

    def deposit(self, items: list) -> APIResponse:
        """Deposit v1 implementation
        https://opskins.com/kb/api-iinventory#method-deposit-v1

        :param items:
        :return:
        """
        api_url = "https://api.opskins.com/IInventory/Deposit/v1/"
        required_keys = ['appid', 'contextid', 'assetid']

        for item in items:
            if any([key not in item for key in required_keys]):
                raise ArgumentIncompleteError("Your passed item doesn't have all required keys({0:s}).".format(
                    ",".join(required_keys)
                ))

        payload = {
            'items': json.dumps(items)
        }

        link = requests.post(url=api_url, data=payload, headers=self._headers)
        return APIResponse(link.text)
