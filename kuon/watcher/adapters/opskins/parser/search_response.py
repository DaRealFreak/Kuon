#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from typing import Generator, Any

from kuon.api_response import APIResponse
from kuon.watcher.adapters.models.item import Item
from kuon.watcher.adapters.models.search_response import SearchResponse
from kuon.watcher.adapters.models.sticker import Sticker


class SearchResponseParser:
    """Parser class to parse the response of the search to the unified format"""

    @staticmethod
    def parse(results: dict):
        """Parse the item model

        :param results:
        :return:
        """
        response = SearchResponse(success=results['status'] == 1, checked_time=results['time'])
        for item in results['response']['sales']:
            wear = item['wear']
            if wear is None:
                wear = -1.0

            item_model = Item(
                market_name=item['market_name'],
                # OPSkins doesn't use the item_id from the Steam API but their own id
                item_id=int(item['id']),
                app_id=int(item['appid']),
                class_id=int(item['classid']),
                context_id=int(item['contextid']),
                instance_id=int(item['instanceid']),
                price=int(item['amount']),
                wear_value=float(wear),
                image=item['img'],
                inspect_link=item['inspect'],
                stickers=SearchResponseParser.get_stickers(item['stickers'])
            )
            response.add_item(item_model)
        return APIResponse(json.dumps(response.__dict__))

    @staticmethod
    def chunks(seq, n: int) -> Generator[Any, Any, None]:
        """Split sequence into chunks

        :param seq:
        :param n:
        :return:
        """
        return (seq[i:i + n] for i in range(0, len(seq), n))

    @staticmethod
    def get_stickers(stickers: str) -> list:
        """Parse the sticker value

        :param stickers:
        :return:
        """
        if not stickers:
            return []

        sticker_results = []
        stickers = SearchResponseParser.chunks(stickers.split(','), 2)
        for sticker in stickers:
            sticker_results.append(Sticker(
                name=sticker[0],
                image='',
                wear_value=float(sticker[1])
            ))

        return sticker_results
