#!/usr/bin/python
# -*- coding: utf-8 -*-


class LimitExceededException(Exception):
    pass


class NoLoginIdProvidedException(Exception):
    pass


class NoLoginPassProvidedException(Exception):
    pass


class NoSteamID64ProvidedException(Exception):
    pass


class No2FASecretProvidedException(Exception):
    pass


class NoIdentitySecretKeyProvidedException(Exception):
    pass


class NoAPIKeyProvidedException(Exception):
    pass
