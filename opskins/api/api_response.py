#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections
import json

from opskins.api.exceptions import InvalidApiResponseType


class APIResponse(collections.Mapping):

    def __init__(self, data):
        try:
            self._data = json.loads(data)
        except ValueError:
            raise InvalidApiResponseType("The API didn't return a valid json format")
        self._data = data

    def __repr__(self):
        return self._data

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)
