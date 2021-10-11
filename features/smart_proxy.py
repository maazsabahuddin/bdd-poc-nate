# Python imports
import os

# Framework Imports
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Local imports
from modules.logger import logger


HOSTNAME = ''
PORT = ''
RUN_PROXY = False


def smart_proxy_impl():
    """
    This piece of code is going to handle the residential proxies.
    Make sure to not edit settings beyond this point unless you know what you are doing!
    :return:
    """

    if not RUN_PROXY:
        logger.info("SMART PROXY FLAG IS OFF")

    if RUN_PROXY and not (HOSTNAME and PORT):
        logger.info("SMART PROXY FLAG IS ON, but some parameters are missing")
        os.abort()
        return

    prox = Proxy()

    prox.proxy_type = ProxyType.MANUAL

    prox.http_proxy = '{hostname}:{port}'.format(hostname=HOSTNAME, port=PORT)
    prox.ssl_proxy = '{hostname}:{port}'.format(hostname=HOSTNAME, port=PORT)

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    return capabilities
