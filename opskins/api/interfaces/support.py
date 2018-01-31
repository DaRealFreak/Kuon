#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

from opskins import OPSkins
from opskins.api import APIResponse


class ISupport(OPSkins):
    """The ISupport interface of OPSkins"""

    def __init__(self):
        """Initializing function"""
        super().__init__()

    def repair_item(self, saleid):
        """RepairItem v1 implementation
        https://opskins.com/kb/api-isupport#method-repairitem-v1

        :param saleid:
        :return:
        """
        api_url = "https://api.opskins.com/ISupport/RepairItem/v1/"

        payload = {
            'saleid': str(saleid)
        }

        link = requests.post(url=api_url, data=payload, headers=self._headers)
        return APIResponse(link.text)
