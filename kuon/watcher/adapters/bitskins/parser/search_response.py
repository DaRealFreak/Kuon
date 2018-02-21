#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from kuon.api_response import APIResponse
from kuon.watcher.adapters.models.item import Item
from kuon.watcher.adapters.models.search_response import SearchResponse
from kuon.watcher.adapters.models.sticker import Sticker


class SearchResponseParser:
    """Parser class to parse the response of the search to the unified format"""

    @staticmethod
    def parse(results):
        """Parse the item model

        :param results:
        :return:
        """
        response = SearchResponse(success=results['status'] == 'success')
        for item in results['data']['items']:
            wear = item['float_value']
            if wear is None:
                wear = -1.0

            item_model = Item(
                market_name=item['market_hash_name'],
                item_id=int(item['item_id']),
                app_id=int(item['app_id']),
                class_id=int(item['class_id']),
                context_id=int(item['context_id']),
                instance_id=int(item['instance_id']),
                price=int(float(item['price']) * 100),
                wear_value=float(wear),
                image=item['image'],
                inspect_link=item['inspect_link'],
                stickers=SearchResponseParser.get_stickers(item['stickers'])
            )
            response.add_item(item_model)
        return APIResponse(json.dumps(response.__dict__))

    @staticmethod
    def get_stickers(stickers):
        """Parse the sticker value

        :param stickers:
        :return:
        """
        if not stickers:
            return []

        sticker_results = []
        for sticker in stickers:
            wear = sticker['wear_value']
            if wear is None:
                wear = -1.0

            sticker_results.append(Sticker(
                name=sticker['name'],
                image=sticker['url'],
                wear_value=float(wear)
            ))

        return sticker_results
