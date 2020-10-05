"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""


def two_sum(nums, target):
    # Your code here
    # Understand:
    # that we want the indices of the two #rs that return the target
    # Plan:
    # work with enumerate or some for loop and  keep track of index and elemnt in list,
    # loop over the first combos of two elements that add up to 15 starting by the first element
    # proceed to work with the next two elements iteratively
    # Might also want to consider a while loop

    for index1, x in enumerate(nums):
        diff = target - x
        index2 = 0
        if diff in nums:
            index2 = nums.index(diff)
            return [index1, index2]
        else:
            continue
    # resources
    # https: // www.programiz.com / python - programming / methods / list / index
    # https://leetcode.com/problems/two-sum/solution/
