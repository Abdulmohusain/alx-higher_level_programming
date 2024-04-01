#!/usr/bin/python3
"""A script that fetches data"""
from urllib import request
import sys

if __name__ == "__main__":
    """Main function"""
    with request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
