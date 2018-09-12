#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

from kuon.api_response import APIResponse
from kuon.watcher.adapters.models.sold_history import SoldHistory
from kuon.watcher.adapters.models.sold_item import SoldItem


class SoldHistoryParser(object):
    """Parser class to parse the response of the sold history to the unified format"""

    @staticmethod
    def parse(results: dict) -> APIResponse:
        """Parse the sold history model

        :type results: dict
        :return:
        """
        response = SoldHistory(success=results['status'] == 'success')
        for item in results['data']['sales']:
            wear = item['wear_value']
            if wear is None:
                wear = -1.0

            sold_item = SoldItem(
                price=int(float(item['price']) * 100),
                wear_value=float(wear),
                sold_at=int(item['sold_at'])
            )
            response.add_sale(sold_item)
        return APIResponse(json.dumps(response.__dict__))
