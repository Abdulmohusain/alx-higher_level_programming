#!/usr/bin/python3
"""A script that fetches data"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    """Main function"""
    email = sys.argv[2]
    url = sys.argv[1]
    content = parse.urlencode({"email": email})
    content = content.encode('ascii')

    with request.urlopen(url, content) as response:
        print(response.read().decode('utf-8'))
