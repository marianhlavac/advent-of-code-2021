"""
Day 2 of Advent of Code 2021
https://adventofcode.com/2021/day/2

More-or-less a FP solution to the submarine position
problem using lambda functions.
"""

from sys import argv
from operator import add
from functools import reduce

commands_to_coords_map = lambda x, aim: {
    'forward': (x * aim, x, 0),
    'down': (0, 0, x),
    'up': (0, 0, -x),
}

add_tuples_elwise = lambda a, b: tuple(map(add, a, b))

add_command_to_coord = lambda a, b: \
    add_tuples_elwise(a, commands_to_coords_map(int(b[1]), a[2])[b[0]])

calc_final_position = lambda commands: \
    reduce(add_command_to_coord, commands, (0, 0, 0))


def read_commands_from_file(filename):
    with open(filename, 'r') as file:
        return [line.split(' ') for line in file.readlines()]


commands = read_commands_from_file(argv[1])
final_pos = calc_final_position(commands)
result = final_pos[0] * final_pos[1]

print(f'Result: {result} (final coordinate was {final_pos})')
