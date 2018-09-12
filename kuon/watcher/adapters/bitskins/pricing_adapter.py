#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.bitskins.api.interfaces import IPricing
from kuon.watcher.adapters import PricingAdapterBase


class PricingAdapter(PricingAdapterBase):
    """Adapter for the Pricing Interface of BitSkins"""

    def __init__(self, *args, **kwargs) -> None:
        """Initializing function

        :type args: list
        :type kwargs: dict
        """
        self.pricing_interface = IPricing(*args, **kwargs)
