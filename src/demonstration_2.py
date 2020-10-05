"""
Given an integer value `n`, write a function that will return a list of the string representation of numbers from 1 to `n`.

However, there are a few additional rules to follow:

- For multiples of three, it should output "Lambda" instead of the number.
- For multiples of five, it should output "School" instead of the number.
- For numbers which are multiples of three and five, it should output "LambdaSchool" instead of the number.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Lambda",
    "4",
    "School",
    "Lambda",
    "7",
    "8",
    "Lambda",
    "School",
    "11",
    "Lambda",
    "13",
    "14",
    "LambdaSchool"
]
"""

# My Sol
def lambda_school(n):
    # Your code here
    # Understand
    # Want to return a list consisting of numbers 1, n
    # At the same time we have some conditions, multiples of 3,5, and 3 and 5 correpond to certain  strings
    # That is lambda, school, lambdaschool
    # Plan
    # use enumerate and range to perform a a for loop that keeps track of index and elements created from range(n+!)

    # create list of numbers 1 through n
    list1 = list(range(1, n + 1))

    for index, x in enumerate(list1):
        if x % 3 == 0 and x % 5 == 0:
            list1[index] = "LambdaSchool"
        elif x % 3 == 0:
            list1[index] = "Lambda"
        elif x % 5 == 0:
            list1[index] = "School"
    return list1


# solution #2
def lambda_school(n):
    return [str(i) if i % 3 and i % 5 else "LambdaSchool" if not i % 15 else "School" if not i % 5 else "Lambda" for i
            in range(1, n + 1)]

#instructors sol
def lambda_school(n):
    # Your code here
    answer = []
    # loop up to n, using `range`
    # keep in mind we want 1-indexed numbers, instead of 0-indexing
    for num in range(1, n+1):
        # we need to check if num is divisible by 3
        divisible_by_3 = (num % 3 == 0)
        # we need to check if num is divisible by 5
        divisible_by_5 = (num % 5 == 0)
        # we need to check if num is divisible by 3 and 5
        # ordering of how we check divisibility of num is important
        if divisible_by_3 and divisible_by_5:
            answer.append("LambdaSchool")
        elif divisible_by_3:
            answer.append("Lambda")
        elif divisible_by_5:
            answer.append("School")
        # for every other number, we need to push it to our answer
        # list, but as a string, instead of as a number
        else:
            answer.append(str(num))
    return answer
print(lambda_school(30))