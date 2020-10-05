"""
Given a `string`, write a function that finds the first non-repeating character in the `string` and return its index.
 If it doesn't exist, return -1.

Examples:

string = "lambdaschool"
return 2.

string = "lovelambdaschool"
return 2.

string = "abcabc"
return -1.
"""


def first_unique_char(string):
    list1 = [char for char in string]
    for index, x in enumerate(list1):
        try:
            if x not in list1[index + 1:]:
                return index
        except:
            continue


def first_unique_char(string):
    # Understand
    # we want the first non repeating character
    # in other words, we want the first character that didn't repeated itself for the first n characters
    # Plan
    # Split string into individual characters
    # run a for loop that keeps track of index and character
    # if character appears in the list created from splitting string into individual chars
    # Then we want to return the index corresponding to this character
    list1 = [char for char in string]
    for index, char in enumerate(list1):
        if char not in list1[index + 1:] and len(list1[index + 1:]) >= 2:
            return index
        else:
            return -1


# Instructor solution
def first_unique_char(string):
    # Your code here
    counts = {}
    # loop through our string to populate dictionary
    # with the counts of each character
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    print(counts)
    # loop over the string again
    # for each char, check how many times it occurs
    # return the index of the first char that occurs once
    for index, char in enumerate(string):
        if counts[char] == 1:
            return index
    # otherwise, no char in the string occurred exactly once
    return -1


string = "lambdaschool"
first_unique_char(string)
