#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

from opskins import OPSkins
from opskins.api import APIResponse


class ITest(OPSkins):
    """The ITest interface of OPSkins"""

    def __init__(self, *args, **kwargs):
        """Initializing function"""
        super().__init__(*args, **kwargs)

    def test(self):
        """Test v1 implementation
        https://api.opskins.com/ITest/Test/v1/

        :return:
        """
        api_url = "https://api.opskins.com/IUser/GetBalance/v1/"

        link = requests.get(url=api_url, headers=self._headers)
        return APIResponse(link.text)

    def test_authenticated(self):
        """TestAuthed v1 implementation
        https://opskins.com/kb/api-itest#method-testauthed-v1

        :return:
        """
        api_url = "https://api.opskins.com/ITest/TestAuthed/v1/"

        link = requests.get(url=api_url, headers=self._headers)
        return APIResponse(link.text)
