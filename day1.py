"""
Day 1 of Advent of Code 2021
https://adventofcode.com/2021/day/1

A naive and readable solution of the first AoC
problem, to serve as a starting point and reference
for my colleague.
"""

from sys import argv


def read_input(filename):
    with open(filename, 'r') as file:
        return [int(line) for line in file.readlines()]


def count_increases(nums):
    increases = 0

    for idx in range(3, len(nums)):
        left_sum = nums[idx-1] + nums[idx-2] + nums[idx-3]
        right_sum = nums[idx] + nums[idx-1] + nums[idx-2]
        if right_sum > left_sum:
            increases += 1

    return increases


numbers = read_input(argv[1])
result = count_increases(numbers)
print(f'The count of increases is {result}.')
