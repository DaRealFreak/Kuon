#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Structured similar to the OPSkins interfaces to make it easier to work with both APIs
Split up in:

ICashout:
    Money Withdrawal

IHistory:
    Get Money Events
    Get Buy History
    Get Sell History
    Get Item History
    Get Trade Details
    Get Recent Trade Offers

IInventory:
    Get Account Inventory
    Get Inventory On Sale

IPricing:
    Get All Item Prices
    Get Market Data

ISales:
    Buy Item
    Sell Item
    Modify Sale
    Withdraw Item
    Bump Item
    Get Reset-Price Items
    Get Raw Price Data
    Get Specific Items on Sale
    Get Recent Sale Info

IUser:
    Get Account Balance
"""

from kuon.bitskins.api.interfaces.cashout import ICashout
from kuon.bitskins.api.interfaces.history import IHistory
from kuon.bitskins.api.interfaces.inventory import IInventory
from kuon.bitskins.api.interfaces.pricing import IPricing
from kuon.bitskins.api.interfaces.sales import ISales
from kuon.bitskins.api.interfaces.user import IUser

__all__ = [
    ICashout.__name__,
    IHistory.__name__,
    IInventory.__name__,
    IPricing.__name__,
    ISales.__name__,
    IUser.__name__
]
