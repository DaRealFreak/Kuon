#!/usr/bin/python
# -*- coding: utf-8 -*-


class NoAPIKeyProvidedException(Exception):
    pass


class NoSecretProvidedException(Exception):
    pass


class InvalidOrWrongApiKeyException(Exception):
    pass
