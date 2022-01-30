#!/usr/bin/env python3
# Python 3.9.6

import re

""""
This funtion read a file and return the content
"""


def readFile(file_name):
    try:
        # Read file and close it
        file = open(file_name)
        content = file.readlines()
        file.close()
        return content
# print(lines)
    except FileNotFoundError:
        print("File {} is not exist to ride".format(file_name))
        exit()


def writeFile(file_name, mod, content):
    try:
        with open(file_name, mod) as file:
            lines = content
            for line in lines:
                file.write(line)
    except IOError:
        print("Sorry can\'t write file")


