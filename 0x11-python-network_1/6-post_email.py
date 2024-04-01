#!/usr/bin/python3
"""A script that fetches data"""
from sys import argv
from requests import post


if __name__ == '__main__':
    res = post(argv[1], {'email': argv[2]})
    print(res.text)
