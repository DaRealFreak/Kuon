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
        response = SoldHistory(success=results['status'] == 1)
        for item in results['response']:
            wear = item['wear']
            if item['wear'] is None:
                wear = -1.0

            sold_item = SoldItem(
                price=int(item['amount']),
                wear_value=float(wear),
                sold_at=int(item['timestamp'])
            )
            response.add_sale(sold_item)
        return APIResponse(json.dumps(response.__dict__))
