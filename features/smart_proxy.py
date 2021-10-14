"""
This file is basically the implementation of smart proxy residential service.
You can get information for HOSTNAME and PORT on your users dashboard panel.
url: https://dashboard.smartproxy.com/welcome
"""

# Python imports

# Framework Imports
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Local imports
from features import config
from modules.logger import logger

HOSTNAME = 'us.smartproxy.com'
PORT = f'10000:user-{config.USERNAME}:{config.PASSWORD}'
RUN_PROXY = True


def smart_proxy_impl():
    """
    This piece of code is going to handle the residential proxies.
    Make sure to not edit settings beyond this point unless you know what you are doing!
    :return:
    """

    if not RUN_PROXY:
        logger.info("SMART PROXY FLAG IS OFF")

    if RUN_PROXY and not (HOSTNAME and PORT):
        logger.info("SMART PROXY FLAG IS ON, but hostname/port is missing. Running normal flow...")
        return

    prox = Proxy()

    prox.proxy_type = ProxyType.MANUAL

    prox.http_proxy = '{hostname}:{port}'.format(hostname=HOSTNAME, port=PORT)
    prox.ssl_proxy = '{hostname}:{port}'.format(hostname=HOSTNAME, port=PORT)

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    return capabilities
