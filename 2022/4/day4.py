#!/usr/bin/env python

def part1():
	count = 0
	with open('input.txt') as file:
		for line in file:
			elf1, elf2 = line.strip().split(',')
			elf1 = [int(elf) for elf in elf1.split('-')]
			elf2 = [int(elf) for elf in elf2.split('-')]
			if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
				print('elf 1 in elf 2')
				print('elf1', elf1, 'elf2', elf2)
				count += 1
			elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
				print('elf 2 in elf 1')
				print('elf1', elf1, 'elf2', elf2)
				count += 1
	print("Count", count)


part1()
# count = 0
# input = '31-74,5-32'
# elf1, elf2 = input.strip().split(',')
# elf1 = [int(elf) for elf in elf1.split('-')]
# elf2 = [int(elf) for elf in elf2.split('-')]
# if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
# 	print('elf 1 in elf 2')
# 	print('elf1', elf1, 'elf2', elf2)
# 	count += 1
# elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
# 	print('elf 2 in elf 1')
# 	print('elf1', elf1, 'elf2', elf2)
# 	count += 1
# print("Count", count)