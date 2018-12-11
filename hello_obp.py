#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script says hello to the OpenBankProject API

Configure settings.py to suit your needs.
"""

from pprint import pprint

from oauth_dance import get_api
from settings import API_USER_URL
import logging

def say_hello():
    """Says hello to the API"""
    api = get_api()
    
    """Get the current authenticated User """
    response = api.get(API_USER_URL)
    status_code = response.status_code
    print('Status code: {}'.format(status_code))
    if status_code == 200:
        print('Success JSON:')
        pprint(response.json())
    else:
        print(response.text)    


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,)
    say_hello()
