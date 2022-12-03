#!/usr/bin/env python

def part_1():
	rate_dict = {}
	gamma_rate = ''
	epsilon_rate = ''
	with open('input.txt') as file:
		for line in file:
			bits = list(line.rstrip())
			for i in range(len(bits)):
				rate_dict.setdefault(i, {}).setdefault(bits[i], 0)
				rate_dict[i][bits[i]] += 1
	
	for i in range(len(rate_dict)):
		position_dict = rate_dict[i]
		if rate_dict[i]['0'] > rate_dict[i]['1']:
			gamma_rate += '0'
			epsilon_rate += '1'
		else: 
			gamma_rate += '1'
			epsilon_rate += '0'

	print('Power Consumption:', int(gamma_rate, 2) * int(epsilon_rate, 2), 'gamma_rate:', gamma_rate, 'epsilon_rate:', epsilon_rate)


def get_most_common_bit(input, index):
	zeros = 0
	ones = 0
	for value in input:
		if value[index] == '0':
			zeros += 1
		else:
			ones += 1
	return '1' if ones >= zeros else '0'


def get_oxygen_generator_rating(input, index):
	# input = List[str]
	# 0 <= index < len(input[0])
	if len(input) == 1:
		return input[0]
	# find most common bit at index
	most_common_bit = get_most_common_bit(input, index)
	# create list of values containing the most common bit
	new_input = []
	for value in input:
		if value[index] == most_common_bit:
			new_input.append(value)
	# recurse
	return get_oxygen_generator_rating(new_input, index + 1)


def get_co2_scrubbing_rating(input, index):
	# input = List[str]
	# 0 <= index < len(input[0])
	if len(input) == 1:
		return input[0]
	# find most common bit at index
	most_common_bit = get_most_common_bit(input, index)
	# conver most common bit to least common bit
	least_common_bit = str(~ (int(most_common_bit) - 2))
	# create list of values containing the most common bit
	new_input = []
	for value in input:
		if value[index] == least_common_bit:
			new_input.append(value)
	# recurse
	return get_co2_scrubbing_rating(new_input, index + 1)


def part_2():
	input = []
	with open('input.txt') as file:
		for line in file:
			input.append(line.rstrip())
	oxygen_generator_rating = get_oxygen_generator_rating(input, 0)
	co2_scrubbing_rating = get_co2_scrubbing_rating(input, 0)
	print('oxygen_generator_rating:', oxygen_generator_rating, 'co2_scrubbing_rating:', co2_scrubbing_rating)
	print('Life support rating:', int(oxygen_generator_rating, 2) * int(co2_scrubbing_rating, 2))
	


part_1()
part_2()




