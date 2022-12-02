#!/usr/bin/env python

#Part 1
count = 0
with open('input.txt') as file:
	temp = 0
	for line in file:
		if temp == 0:
			temp = int(line.rstrip())
		elif int(line.rstrip()) > temp:
			count += 1
		temp = int(line.rstrip())
print("Count:", count)

#Part 2
sum_a = 0
sum_b = 0
sum_c = 0
i = 1

output_count = 0
with open('input.txt') as file:
	for line in file:
		mod_i = i%3
		current_val = int(line.rstrip())
		# First 3 values just get added
		if i <= 3:
			if mod_i == 1:
				sum_a += current_val
			elif mod_i == 2:
				sum_a += current_val
				sum_b += current_val
			else:
				sum_a += current_val
				sum_b += current_val
				sum_c += current_val

		if mod_i == 1:
			# add current value to other 2 sums
			sum_b += current_val
			sum_c += current_val
			# calculate increase
			if sum_b > sum_a:
				output_count += 1
			# assign current val to sum_a
			sum_a = current_val
		elif mod_i == 2:
			# add current value to other 2 sums
			sum_a += current_val
			sum_c += current_val
			# calculate increase
			if sum_c > sum_b:
				output_count += 1
			# assign current val to sum_b
			sum_b = current_val
		else:
			# add current value to other 2 sums
			sum_a += current_val
			sum_b += current_val
			# calculate increase
			if sum_a > sum_c:
				output_count += 1
			# assign current val to sum_c
			sum_c = current_val
		i += 1
print("Count 2:", output_count)
