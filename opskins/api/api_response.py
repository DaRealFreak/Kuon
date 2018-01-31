#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from opskins.api.exceptions import *

from collections import MutableSequence


class LockedList(MutableSequence):
    """Custom list where customizing values isn't possible by default
    Return LockedList on list or tuple types
    and LockedDict on dict types"""

    def __init__(self, data=None):
        """Initialize the class"""
        super(LockedList, self).__init__()
        if data is not None:
            self._list = list(data)
        else:
            self._list = list()

    def __repr__(self):
        return str(self._list)

    def __len__(self):
        return len(self._list)

    def __getitem__(self, ii):
        val = self._list[ii]
        if isinstance(val, list) or isinstance(val, tuple):
            val = LockedList(val)
        if isinstance(val, dict):
            val = LockedDict(val)
        return val

    def __delitem__(self, ii):
        del self._list[ii]

    def __setitem__(self, ii, val):
        pass

    def __str__(self):
        return str(self._list)

    def insert(self, ii, val):
        pass

    def append(self, val):
        pass


class LockedDict(dict):
    """Custom dict where customizing values isn't possible by default
    Return LockedList on list or tuple types
    and LockedDict on dict types"""

    def __init__(self, *args, **kwargs):
        super(LockedDict, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        val = self.get(attr)
        if isinstance(val, list) or isinstance(val, tuple):
            val = LockedList(val)
        if isinstance(val, dict):
            val = LockedDict(val)
        return val

    def __setattr__(self, key, value):
        pass

    def __setitem__(self, key, value):
        pass

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(LockedDict, self).__delitem__(key)
        del self.__dict__[key]


class APIResponse(LockedDict):
    """Wrapper for the json response returned from the OPSkins API
    Uses LockedDict and LockedList classes to prevent modifications to the retrieved values"""

    def __init__(self, data):
        try:
            data = json.loads(data)
        except ValueError:
            raise InvalidApiResponseType("The API didn't return a valid json format")

        super().__init__(data)
