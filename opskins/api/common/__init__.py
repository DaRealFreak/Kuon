#!/usr/bin/python
# -*- coding: utf-8 -*-


class ItemStatus:
    AWAITING_PICKUP = 1
    ON_SALE = 2
    SOLD_AWAITING_DELIVERY = 3
    SOLD_AND_DELIVERED = 4
    REQUESTING_RETURN = 5
    RETURNED = 6


class Sorting:
    NEW = 'new'
    OLDEST_BUMP = 'oldest_bump'
    LAST_SOLD = 'last_sold'
    PRICE_DESC = 'price_desc'
    PRICE_ASC = 'price_asc'
    ALPHA = 'alpha'
    BOT = 'bot'
    ACTIVITY_OLD = 'activity_old'
    ACTIVITY_NEW = 'activity_new'
