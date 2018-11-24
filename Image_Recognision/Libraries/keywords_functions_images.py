# Functions used as keywords in Keywords/eshop/keywords_eshop.txt
from robot.api import logger

def locate_product(xpath, webelements, product_name):
    """Receives initial xpath, a list of webelements and a product name and returns a modified unique xpath locator
       of the product."""
    for webelement in webelements:
        if webelement.get_attribute('title') in product_name:
            return xpath + "[@title='" + webelement.get_attribute('title') + "']"
    return False


def get_neighboring_element_xpath(product_xpath, postfix):
    """To be able to click on a button "Add to cart" that belongs to a specific product (identified by label)."""
    return "(" + product_xpath + postfix


def is_in_cart(webelements, product_name):
    """Receives all product names (webelement objects) from cart and returns True if a given product_name is there."""
    for webelement in webelements:
        if webelement.text in product_name:
            return True
    return False

def get_trash_button_by_label(webelements, label, xpath, postfix):
    """Receives webelements, label of the product to be deleted, its xpath and a postfix to identify its trash icon.
       Return xpath to a trash icon of the product to be deleted."""
    index = 1
    for webelement in webelements:
        if webelement.text in label:
            return '(' + xpath + postfix + ')' + '[' + str(index) + ']'
        index += 1
    return False

def is_sorted(lst, order):
    """Returns true if sorted."""
    logger.info(lst)
    logger.info(order)
    if order == 'ASC':
        return sorted(lst) == lst
    elif order == 'DESC':
        return sorted(lst, reverse=True) == lst
    else:
        logger.error('Wrong sorting criteria - should be either ASC or DESC.')
