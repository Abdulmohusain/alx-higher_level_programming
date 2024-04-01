#!/usr/bin/python3
"""A script that fetches data"""
import requests
import sys


if __name__ == '__main__':
    resp = requests.get(sys.argv[1])
    print(resp.headers.get('X-Request-Id'))
