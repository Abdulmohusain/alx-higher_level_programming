#!/usr/bin/python3
"""A script that fetches data"""
import requests


if __name__ == "__main__":
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    content = resp.text
    print(
        'Body response:\n\t- type: {}\n\t- content: {}'.format(
            type(content),
            content
            ))
