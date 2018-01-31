#!/usr/bin/python
# -*- coding: utf-8 -*-

from opskins.api.interfaces.cashout import ICashout
from opskins.api.interfaces.inventory import IInventory
from opskins.api.interfaces.pricing import IPricing
from opskins.api.interfaces.sales import ISales
from opskins.api.interfaces.status import IStatus
from opskins.api.interfaces.support import ISupport
from opskins.api.interfaces.test import ITest
from opskins.api.interfaces.user import IUser

__all__ = [
    ICashout.__name__,
    IInventory.__name__,
    IPricing.__name__,
    ISales.__name__,
    IStatus.__name__,
    ISupport.__name__,
    ITest.__name__,
    IUser.__name__
]
