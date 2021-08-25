# Local Imports
from modules.logger import logger


class Shipping:
    """
    This class is responsible to fill out shipping address details by identify
    shipping page type and other flows.
    """
    def __init__(self, context):
        self.context = context

    def identify_shipping_page_type(self):
        logger.info("Identifying shipping address page type")
        print(self.context)
        pass

    @staticmethod
    def fill_address_details():
        logger.info("Entering shipping address details.")
        pass
