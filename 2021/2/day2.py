#!/usr/bin/env python

def part_1():
	horizontal = 0
	depth = 0

	with open('input.txt') as file:
		for line in file:
			direction, distance = line.split(' ')
			if direction == 'forward':
				horizontal += int(distance)
			elif direction == 'down':
				depth += int(distance)
			elif direction == 'up':
				depth -= int(distance)
	print("Horizontal: {} Depth: {} Answer: {}".format(horizontal, depth, horizontal*depth))

def part_2():
	horizontal = 0
	depth = 0
	aim = 0

	with open('input.txt') as file:
		for line in file:
			direction, distance = line.split(' ')
			if direction == 'forward':
				horizontal += int(distance)
				depth += aim * int(distance)
			elif direction == 'down':
				aim += int(distance)
			elif direction == 'up':
				aim -= int(distance)
	print("Horizontal: {} Depth: {} Answer: {}".format(horizontal, depth, horizontal*depth))

part_1()
part_2()
