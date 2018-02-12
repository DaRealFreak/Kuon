#!/usr/bin/python
# -*- coding: utf-8 -*-


class MissingArgumentException(Exception):
    pass


class ArgumentIncompleteError(Exception):
    pass


class InvalidApiResponseType(Exception):
    pass


class NoAPIKeyProvidedException(Exception):
    pass


class NoSecretProvidedException(Exception):
    pass


class InvalidOrWrongApiKeyException(Exception):
    pass
