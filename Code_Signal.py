"""PROBLEM #3"""
# Given a list of phone numbers, determine if it is consistent in the sense that no
# number in the list is the prefix of another number in the list.
#
# Example
#
# For numbers = ["911", "9876543", "9112345"], the output should be
# prefixFreePhones(numbers) = false.
# In this case, it isn't possible to call the third person in a list, because the system would direct
# your call to the first number as soon as you dialed the first three digits of third phone number.
# So this list is not consistent.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.string numbers
#
# All numbers are unique.
#
# Guaranteed constraints:
# 1 ≤ numbers.length ≤ 105,
# 1 ≤ numbers[i].length ≤ 10.
#
# [output] boolean
#
# Return true if no number in the given list of phone numbers is the prefix of another number in the list,
# otherwise return false.


# Checking Time
import time

t0 = time.time()
code_block
t1 = time.time()

total = t1 - t0


# My Solution
def prefixFreePhones(numbers):
    # Understand
    # We want to check if any given number in the inputed list (numbers)
    # If is not the prefix for other numbers return False, otherwise return True
    # Plan
    # Make some type of for loop and check for the element x in loop is the prefix(starts)
    # in other number using startswith

    string = " ".join(numbers)
    if len(numbers) == 1:
        return True
    for index, x in enumerate(numbers):
        if string.count(x) >= 2:
            return False
        else:
            continue
    return True


Time = 34.40


# Roberts Solution
def prefixFreePhones(numbers):
    set_nums = set(numbers)
    for num in numbers:
        for idx in range(1, len(num)):
            if num[:idx] in set_nums:
                return False
    return True


Time = 13.47


# PROBLEM #4
# Given a number n, return an array composed of the string representations of the numbers from
# 1 to n. But there's a twist! For multiples of 3, return the string "Fizz" instead of the number;' \
#                  ' for multiples of 5, return the string "Buzz"; and for multiples of both 3 and 5,' \
#                  ' return the string "FizzBuzz".
#
# Example
#
# For n = 15, the output should be
# fizzBuzz(n) = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"].

# My Sol
def fizzBuzz(n):
    # want to return an a list with elements have string representation of numbers 1 to n
    list1 = list(range(1, n + 1))

    for index, x in enumerate(list1):
        if x % 3 == 0 and x % 5 == 0:
            list1[index] = "FizzBuzz"
        elif x % 3 == 0:
            list1[index] = "Fizz"
        elif x % 5 == 0:
            list1[index] = "Buzz"
        else:
            list1[index] = str(x)
    return list1


# TEST#1
# Input:
# n: 15
# Output:
# ["1",
#  "2",
#  "Fizz",
#  "4",
#  "Buzz",
#  "Fizz",
#  "7",
#  "8",
#  "Fizz",
#  "Buzz",
#  "11",
#  "Fizz",
#  "13",
#  "14",
#  "FizzBuzz"]
# Expected Output:
# ["1",
#  "2",
#  "Fizz",
#  "4",
#  "Buzz",
#  "Fizz",
#  "7",
#  "8",
#  "Fizz",
#  "Buzz",
#  "11",
#  "Fizz",
#  "13",
#  "14",
#  "FizzBuzz"]
# Console Output:
# Empty

# PROBLEM #5
# Check if the given string is a correct time representation of the 24-hour clock.
#
# Example
#
# For time = "13:58", the output should be
# validTime(time) = true;
# For time = "25:51", the output should be
# validTime(time) = false;
# For time = "02:76", the output should be
# validTime(time) = false.
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] string time
#
# A string representing time in HH:MM format. It is guaranteed that the first two characters,
# as well as the last two characters, are digits.
#
# [output] boolean
#
# true if the given representation is correct, false otherwise.

def validTime(time):
    # Understand
    # Want to verify the string (time) has a correct 24 hr representation
    # Plan
    # Split string into individal character
    # Check first char can only be 0,1,2,->
    # second char can be 0 through 9 when first char is 0 or 1, second char can be 0-4 when first char is 2
    # thirds char is :
    # fourth can be 0 -> 5
    # fight char can be 0->9
    # Method #2 split by coloon, verify first 2 char are between 0-23, and verify last two char are between 0-59

    # split time into two string integers
    time = time.split(":")
    # Map time to a list of integers (could also do a for loop to convert list strings to ints
    time = list(map(int, time))

    # verify first integer in time is between 0-23 and second one is btw 0-59
    # consider the edge case when we have negative numbers

    if 0 <= time[0] <= 23 and 0 <= time[1] <= 59:
        return True
    else:
        return False
