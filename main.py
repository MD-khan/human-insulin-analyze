#!/usr/bin/env python3
# Python 3.9.6

import re

""""
This script analizes the following content:

ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//

This content can be found here : https://www.ncbi.nlm.nih.gov/protein/AAA59172.1

Note: This script automate the 99% of the work including read, write and slicing data.
      To make this script fully atumate you need to scrabe content from the above link.

Start Here:
    To run this script, you need to create preproinsulin-seq.txt and copy and paste the content 
    that start with ORIGIN and end wiht //

What to expect from this script:
    It will clean the content with removing ORIGIN, // and all the digits.
    Next it will save the clean data in preproinsulin-seq-clean.txt
    Next it will count the total characters of the content that is 110
    After that, it will slice the date from the preproinsulin-seq-clean.txt 
        based on the amino acids characters such as amino acide 1 to 24
    Up next, it will save all the slices data in different files
    Also it will count the amino acids total characters characters 
"""

# This funtion read a file and return the content


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


# Get the content data for cleaning
"""
programmatically delete ORIGIN, 1, 61, //, and the spaces and return carriages.
from the file preproinsulin-seq.txt
"""


# This function create new file

def writeFile(file_name, mod, content):
    try:
        with open(file_name, mod) as file:
            lines = content
            for line in lines:
                file.write(line)
    except IOError:
        print("Sorry can\'t write file")


# This function take two parameter
# Return all the matched based on the regex
def matchContentWithRegex(content, regex):
    matches = re.finditer(regex, content)
    all_matches = []
    for match in matches:
        all_matches.append(match)
    return all_matches


content = readFile("preproinsulin-seq.txt")
# this content is a list type
# so we need to convert it to string
# Otherwise matchContentWithRegex(content, regex) will not work
content = ' '.join(content)
regex = r"[a-z]+(\w)*"

pattern_matched_group = matchContentWithRegex(content, regex)

# Writnig file with the matched content


def cleanContent(match_group):
    clean_text = ''
    for match in match_group:
        match[0].strip()
        clean_text += match[0]
    return clean_text


# print(cleanContent(pattern_matched_group))
clean_text = cleanContent(pattern_matched_group)  # call the function
# create a new file with the clean text
writeFile("preproinsulin-seq-clean.txt", "w", clean_text)

# Makeing sure the clean text has 110 character

# print(len(clean_text))


def count_characters(text):
    # readFile("preproinsulin-seq-clean.txt")
    return len(text)


print(count_characters(clean_text))

# Anaylioze the content - human insulin
# We have now the raw data
# We need to slice them based on the aminos acids
#


def sliceInsulinData(data, start, end):
    string_slice = data[start:end]
    return string_slice

# Now we will slice amino acids
# And save these slice data on a file
# Create file wiht the indi


def saveAminoAcids(file_name, mod, amino_acids_characters):
    writeFile(file_name, mod, amino_acids_characters)


""""
The below section will slice the clean text 
"""
# call sliceInsulinData to slice amino acids 1-24
amino_acids_1_24 = sliceInsulinData(clean_text, 0, 24)
# print(amino_acids_1_24)
# Save amino acids 1 to 24 in lsinsulin-seq-clean.txt
writeFile("lsinsulin-seq-clean.txt", "w", amino_acids_1_24)
# Veryfiy that file has 30 characters
print("Aminos Acids 1 to 24 has total {} characters".format(
    count_characters(amino_acids_1_24)))

# call sliceInsulinData to slice amino acids 25-54
amino_acids_25_54 = sliceInsulinData(clean_text, 24, 54)
# print(amino_acids_25_54)
# Save amino acids 25 to 54 in lsinsulin-seq-clean.txt
writeFile("lbinsulin-seq-clean.txt", "w", amino_acids_25_54)
# Veryfiy that file has 30 characters
print("Aminos Acids 25 to 54 has total {} characters".format(
    count_characters(amino_acids_25_54)))

# call sliceInsulinData to slice amino acids 55-89
amino_acids_55_89 = sliceInsulinData(clean_text, 54, 89)
# print(amino_acids_55_89)
# Save amino acids 55 to 89 in lsinsulin-seq-clean.txt
writeFile("cinsulin-seq-clean.txt", "w", amino_acids_55_89)
# Veryfiy that file has 30 characters
print("Aminos Acids 25 to 54 has total {} characters".format(
    count_characters(amino_acids_55_89)))

# call sliceInsulinData to slice amino acids 55-89
amino_acids_90_110 = sliceInsulinData(clean_text, 89, 110)
# print(amino_acids_90_110)
# Save amino acids 55 to 89 in lsinsulin-seq-clean.txt
writeFile("cinsulin-seq-clean.txt", "w", amino_acids_90_110)
# Veryfiy that file has 30 characters
print("Aminos Acids 25 to 54 has total {} characters".format(
    count_characters(amino_acids_90_110)))

print("Happy Coding \U0001F642")
