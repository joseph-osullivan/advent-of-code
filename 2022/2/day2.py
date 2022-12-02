#!/usr/bin/env python

# Part 1 - Not programatically interesting but it works
point_mapping = {
    'AX': 4,
    'AY': 8,
    'AZ': 3,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 7,
    'CY': 2,
    'CZ': 6,
}
points = 0
with open('./input.txt') as file:
    for line in file:
        points += point_mapping.get(line.rstrip().replace(' ',''))
print("Points:", points)

# Part 2
correct_point_mapping = {
    'AX': 3,
    'AY': 4,
    'AZ': 8,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 2,
    'CY': 6,
    'CZ': 7,
}

correct_points = 0
with open('./input.txt') as file:
    for line in file:
        correct_points += correct_point_mapping.get(line.rstrip().replace(' ', ''))
print("Correct Points:", correct_points)
