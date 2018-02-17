#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class AbstractEntity(ABC):
    """Abstract Entity abstract class"""

    def __repr__(self):
        """Return only the values we set before

        :return:
        """
        return str(self.value)

    @property
    def __dict__(self):
        """Needed for JSON encoding the objects

        :return:
        """
        return self.value

    @property
    @abstractmethod
    def value(self):
        """Returning all values we actually want to have in the model

        :return:
        """
        pass
