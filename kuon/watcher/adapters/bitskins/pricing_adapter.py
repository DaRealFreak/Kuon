#!/usr/bin/python
# -*- coding: utf-8 -*-

from kuon.watcher.adapters import PricingAdapterBase
from kuon.bitskins.api.interfaces import IPricing


class PricingAdapter(PricingAdapterBase):
    """Adapter for the Pricing Interface of BitSkins"""

    def __init__(self, *args, **kwargs):
        """Initializing function

        :param args:
        :param kwargs:
        """
        self.pricing_interface = IPricing(*args, **kwargs)
