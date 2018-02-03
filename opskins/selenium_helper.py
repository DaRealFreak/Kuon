#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import os
import sys
import time
from urllib.parse import urlencode, urlparse, parse_qsl, urlunparse

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'bin\\ChromeHeadless',
                                                 sys.platform, 'chromedriver'))
CHROME_OPTIONS = Options()


class SeleniumHelper(webdriver.Chrome):
    """Headless Chrome implementation with selenium"""

    def __init__(self, log_level=logging.ERROR, *args, **kwargs):
        CHROME_OPTIONS.add_argument("--headless")
        super().__init__(executable_path=CHROMEDRIVER_PATH, chrome_options=CHROME_OPTIONS, *args, **kwargs)
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger("selenium_logger")

    def get(self, url, params=None, headers=None):
        """Rebuild similar behaviour to requests.get function

        :param url:
        :param params:
        :param headers:
        :return:
        """
        if headers:
            desired_capabilities = DesiredCapabilities.CHROME.copy()
            for key in headers:
                desired_capabilities['chrome.page.customHeaders.{0:s}'.format(key.lower())] = headers[key]
            super().__init__(executable_path=CHROMEDRIVER_PATH, chrome_options=CHROME_OPTIONS,
                             desired_capabilities=desired_capabilities)
        if params:
            url_parts = list(urlparse(url))
            query = dict(parse_qsl(url_parts[4]))
            query.update(params)

            url_parts[4] = urlencode(query)
            url = urlunparse(url_parts)

        super().get(url)
        while 'Your browser will redirect to your requested content shortly.' in self.page_source:
            self.logger.debug("sleeping to pass cloudflare")
            time.sleep(1)

        return self
