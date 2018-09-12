#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from collections import MutableSequence

from kuon.exceptions import InvalidApiResponseType


class LockedList(MutableSequence):
    """Custom list where customizing values isn't possible by default
    Return LockedList on list or tuple types
    and LockedDict on dict types"""

    def __init__(self, data=None) -> None:
        """Initialize the class"""
        super(LockedList, self).__init__()
        if data is not None:
            self._list = list(data)
        else:
            self._list = list()

    def __repr__(self) -> str:
        return str(self._list)

    def __len__(self) -> int:
        return len(self._list)

    def __getitem__(self, ii):
        val = self._list[ii]
        if isinstance(val, list) or isinstance(val, tuple):
            val = LockedList(val)
        if isinstance(val, dict):
            val = LockedDict(val)
        return val

    def __delitem__(self, ii) -> None:
        del self._list[ii]

    def __setitem__(self, ii, val) -> None:
        pass

    def __str__(self) -> str:
        return str(self._list)

    def insert(self, ii, val) -> None:
        pass

    def append(self, val) -> None:
        pass


class LockedDict(dict):
    """Custom dict where customizing values isn't possible by default
    Return LockedList on list or tuple types
    and LockedDict on dict types"""

    def __init__(self, *args, **kwargs) -> None:
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

    def __setattr__(self, key, value) -> None:
        pass

    def __setitem__(self, key, value) -> None:
        pass

    def __delattr__(self, item) -> None:
        self.__delitem__(item)

    def __delitem__(self, key) -> None:
        super(LockedDict, self).__delitem__(key)
        del self.__dict__[key]


class APIResponse(LockedDict):
    """Wrapper for the json response returned from the APIs of OPSkins and Bitskins
    Uses LockedDict and LockedList classes to prevent modifications to the retrieved values"""

    def __init__(self, data) -> None:
        try:
            data = json.loads(data)
        except ValueError:
            raise InvalidApiResponseType("The API didn't return a valid json format", data)

        super().__init__(data)
