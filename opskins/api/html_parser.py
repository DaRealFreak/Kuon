#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import re
from time import time
from urllib.parse import unquote

from bs4 import BeautifulSoup as Soup
from bs4 import element


class HtmlToJsonParser:
    """
    Parser to get the same structure of the web request results like the API result
    so written code works with the both SDKs
    """

    @staticmethod
    def _get_context_id(html):
        """Extract the context id from the javascript part of the page

        :param html:
        :return:
        """
        context_id = re.findall('var g_contextId = (\d+);', html)
        if context_id:
            return int(context_id[0])
        else:
            return None

    @staticmethod
    def _get_image(item_tag: element.Tag):
        """Extract the used image from the item tag

        :param item_tag:
        :return:
        """
        image_tag = item_tag.find('img', attrs={'data-async-media': "image"})  # type: element.Tag
        if not image_tag or not image_tag.get('data-mediasrc'):
            return None
        else:
            img_src = image_tag.get('data-mediasrc')
            if "/image/" in img_src:
                img_src = "".join(img_src.split("/image/")[1:])
        return img_src

    @staticmethod
    def _get_inspect_link(item_tag: element.Tag):
        """Extract the inspect link from the item tag

        :param item_tag:
        :return:
        """
        inspect_button = item_tag.find_next('a', text=re.compile('Inspect'))
        if inspect_button:
            return inspect_button.get('href')
        else:
            return None

    @staticmethod
    def _get_stickers(item_tag: element.Tag):
        """Extract the stickers from the item tag

        :param item_tag:
        :return:
        """
        results = []
        sticker_tags = item_tag.find_all('img', attrs={'class': 'sticker'})
        for sticker_tag in sticker_tags:
            sticker_title = sticker_tag.get('title')
            # safe to use index since we assume a wear value too
            name = re.findall('^(.*)\nWear:', sticker_title, flags=re.MULTILINE)[0]
            wear_values = re.findall('Wear: (\d+){1,2}.?(\d+){0,2}% - \w+', sticker_title)[0]
            wear_float = wear_values[1] if wear_values[1] else "0"
            wear = float("{0:s}.{1:s}".format(wear_values[0], wear_float))
            # the OPSkins API returns comma separated so to make the code compatible we do the same
            # why doesn't OPSkins return it as json encoded array though?
            results.append("{0:s},{1:f}".format(name, wear))
            # results.append((name, wear))
        return results

    @staticmethod
    def search_result(html):
        """Parse the html of the search page to a valid json result of the search function
        We don't receive the bot_id or the instance id(not exactly sure what the instance id is used for)
        so set them None on the response

        :param html:
        :return:
        """
        soup = Soup(html, "html5lib")

        context_id = HtmlToJsonParser._get_context_id(html)

        results = {
            'status': 1,
            'time': int(time()),
            'response': {
                'sales': []
            }
        }

        result_div = soup.select_one("div.col-lg-9")
        result_items = result_div.find_all("div", attrs={"class": "featured-item"})
        for item in result_items:  # type: element.Tag
            # img and sticker ids are not in the data tags of the add to cart button
            buy_button_tag = item.find('button', attrs={'data-buttontype': 'addtocart'})

            # we don't get the bot id and instance id in the web result
            res = {
                'img': HtmlToJsonParser._get_image(item),
                'amount': int(buy_button_tag.get('data-amount')),
                'item_id': unquote(buy_button_tag.get('data-item_id')),
                'wear': float(buy_button_tag.get('data-wear')),
                'contextid': context_id,
                'type': unquote(buy_button_tag.get('data-type')),
                'market_name': unquote(buy_button_tag.get('data-market_name')),
                'classid': unquote(buy_button_tag.get('data-classid')),
                'instanceid': None,
                'appid': int(buy_button_tag.get('data-appid')),
                'inspect': HtmlToJsonParser._get_inspect_link(item),
                'stickers': HtmlToJsonParser._get_stickers(item),
                'id': int(buy_button_tag.get('data-id')),
                'bot_id': None,
            }

            results['response']['sales'].append(res)

        return json.dumps(results)
