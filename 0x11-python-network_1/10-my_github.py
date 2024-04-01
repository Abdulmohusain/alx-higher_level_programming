#!/usr/bin/python3
"""A script that fetches data"""
import requests
import sys
if __name__ == '__main__':

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    json = response.json()
    print(json.get('id'))
