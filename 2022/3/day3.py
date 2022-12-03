#!/usr/bin/env python

def part1():
	priority = 0
	with open('input.txt') as file:
		for line in file:
			full_list = list(line.strip())
			first_half = set(full_list[:int(len(full_list)/2)])
			second_half = set(full_list[int(len(full_list)/2):])
			for item in first_half:
				if item in second_half:
					# Use ord math to get priority
					if item.isupper():
						priority += (ord(item) - 38)
					else:
						priority += (ord(item) - 96)

	print('priority:', priority)


def part2():
	priority = 0
	with open('input.txt') as file:
		i = 0
		first_elf = {}
		second_elf = {}
		first_second_common = []
		third_elf = {}

		for line in file:
			mod_i = i%3
			# 1. Create sets of items for each elf. 
			# 2. Find common items between the 1st and 2nd. 
			# 3. Find the single common item between the list created in step 2 and the 3rd elf
			if mod_i == 0:
				first_elf = set(list(line.strip()))
			elif mod_i == 1:
				second_elf = set(list(line.strip()))
				# Find common items between the first and second elf
				for item in first_elf:
					if item in second_elf:
						first_second_common.append(item)
			else:
				third_elf = set(list(line.strip()))
				for item in first_second_common:
					if item in third_elf:
						# Use ord math to get priority
						if item.isupper():
							priority += (ord(item) - 38)
						else:
							priority += (ord(item) - 96)
						break
				else:
					# run when inner loop is not broken
					continue
				first_second_common = []
			i += 1
	print('priority:', priority)

part1()
part2()