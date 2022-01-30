#!/usr/bin/env python3
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"[a-z]+(\w)*"

content = """"
            ORIGIN  
                  1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
                  61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
            //
           """

matches = re.finditer(regex, content)
all_matches = []
for match in matches:
    all_matches.append(match)
# print(all_matches)

clean = ''
for m in all_matches:
    m[0].strip()
    clean += m[0]
# print(clean)
# print(len(clean))

# This function take two parameter
# Return all the matched based on the regex


def matchContentWithRegex(content, regex):
    matches = re.finditer(regex, content)
    all_matches = []
    for match in matches:
        all_matches.append(match)
    return all_matches


print(matchContentWithRegex(content, regex))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
