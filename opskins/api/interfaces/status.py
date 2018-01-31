#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

from opskins import OPSkins
from opskins.api import APIResponse


class IStatus(OPSkins):
    """The IStatus interface of OPSkins"""

    def __init__(self, *args, **kwargs):
        """Initializing function"""
        super().__init__(*args, **kwargs)

    def get_bot_list(self):
        """GetBotList v1 implementation
        https://opskins.com/kb/api-istatus#method-getbotlist-v1

        :return:
        """
        api_url = "https://api.opskins.com/IStatus/GetBotList/v1/"

        link = requests.get(url=api_url, headers=self._headers)
        return APIResponse(link.text)
