#!/usr/bin/env python

import re

def part1():
	output = ''
	stacks = [[],[],[],[],[],[],[],[],[]]
	with open('input.txt') as file:
		for line in file:
			line = line.strip()
			if line.startswith('['):
				# create stacks
				counter = 1
				for i in range(len(stacks)):
					if line[counter] != ' ':
						stacks[i].append(line[counter])
					counter += 4
			elif line.strip().startswith('1'):
				# reverse stacks
				for stack in stacks:
					stack.reverse()
			elif line.strip().startswith('move'):
				# do the moves
				count, start, end = [int(num) for num in re.findall('\d+', line.strip())]
				for i in range(count):
					item = stacks[start-1].pop()
					stacks[end-1].append(item)
	for stack in stacks:
		output += stack.pop()
	print("Output:", output)


def part2():
	output = ''
	stacks = [[],[],[],[],[],[],[],[],[]]
	with open('input.txt') as file:
		for line in file:
			line = line.strip()
			if line.startswith('['):
				# create stacks
				counter = 1
				for i in range(len(stacks)):
					if line[counter] != ' ':
						stacks[i].append(line[counter])
					counter += 4
			elif line.strip().startswith('1'):
				# reverse stacks
				for stack in stacks:
					stack.reverse()
			elif line.strip().startswith('move'):
				# do the moves
				count, start, end = [int(num) for num in re.findall('\d+', line.strip())]
				tmp = []
				for i in range(count):
					item = stacks[start-1].pop()
					tmp.append(item)
				tmp.reverse()
				stacks[end-1].extend(tmp)
	for stack in stacks:
		output += stack.pop()
	print("Output:", output)

part1()
part2()