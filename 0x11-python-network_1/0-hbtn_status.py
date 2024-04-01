#!/usr/bin/python3
"""A script that fetches data"""
from urllib import request

if __name__ == "__main__":
    """Main function"""
    req = request.Request("https://alx-intranet.hbtn.io/status")
    with request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
