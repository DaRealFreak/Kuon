#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from kuon.api_response import APIResponse
from kuon.watcher.adapters.models.sold_history import SoldHistory
from kuon.watcher.adapters.models.sold_item import SoldItem


class SoldHistoryParser:
    """Parser class to parse the response of the sold history to the unified format"""

    @staticmethod
    def parse(results):
        """Parse the sold history model

        :param results:
        :return:
        """
        response = SoldHistory(success=results['status'] == 'success')
        for item in results['data']['sales']:
            sold_item = SoldItem(
                market_name=item['market_hash_name'],
                price=int(float(item['price']) * 100),
                wear_value=float(item['sold_at']),
                sold_at=int(item['sold_at'])
            )
            response.add_sale(sold_item)
        return APIResponse(json.dumps(response.__dict__))
