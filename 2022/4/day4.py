#!/usr/bin/env python

def part1():
	count = 0
	with open('input.txt') as file:
		for line in file:
			elf1, elf2 = line.strip().split(',')
			elf1 = [int(elf) for elf in elf1.split('-')]
			elf2 = [int(elf) for elf in elf2.split('-')]
			# figure out if elf 1 is contained in elf 2
			if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
				count += 1
			# figure out if elf 2 is contained in elf 1
			elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
				count += 1
	print("Count", count)

def part2():
	count = 0
	with open('input.txt') as file:
		for line in file:
			elf1, elf2 = line.strip().split(',')
			elf1 = [int(elf) for elf in elf1.split('-')]
			elf2 = [int(elf) for elf in elf2.split('-')]
			# check first value in elf 1 for overlap
			if elf1[0] >= elf2[0] and elf1[0] <= elf2[1]:
				count += 1
			# check second value in elf 1 for overlap
			elif elf1[1] >= elf2[0] and elf1[1] <= elf2[1]:
				count += 1
			# check first value in elf 2 for overlap
			elif elf2[0] >= elf1[0] and elf2[0] <= elf1[1]:
				count += 1
			# check second value in elf 2 for overlap
			elif elf2[1] >= elf1[0] and elf2[1] <= elf1[1]:
				count += 1
	print("Count", count)


part1()
part2()
