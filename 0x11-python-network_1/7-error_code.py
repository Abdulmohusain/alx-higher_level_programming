#!/usr/bin/python3
"""A script that fetches data"""
import sys
from requests import get


if __name__ == '__main__':
    url = sys.argv[1]
    response = get(url)
    status = response.status_code

    if (status >= 400):
        print('Error code: {}'.format(status))
    else:
        print(response.text)
