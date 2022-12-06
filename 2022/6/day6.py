#!/usr/bin/env python

from queue import SimpleQueue

def find_message_with_marker_length(marker_length):
	code = ''
	with open('input.txt') as file:
		code = next(file).strip()

	queue = SimpleQueue()
	keyset = []
	count = 0
	for char in code:
		if len(set(keyset)) == marker_length:
			# found the key, break
			break
		if queue.qsize() >= marker_length:
			char_to_remove = queue.get()
			keyset.remove(char_to_remove)
		queue.put(char)
		keyset.append(char)
		count += 1

	print('Count:', count)

find_message_with_marker_length(4)
find_message_with_marker_length(14)