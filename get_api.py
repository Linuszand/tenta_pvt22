from pprint import pprint

import requests


def get_api(parameter):
    """
    Fetches data from URL and converts it to JSON
    :param parameter: A dictionary tuple
    :return: Returns the data from the URL
    """
    res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=parameter).json()
    return res
