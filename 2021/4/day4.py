#!/usr/bin/env python


class BingoBoard(object):
	number_position = {}
	board = []
	score = 0
	
	def __init__(self, file):
		super(BingoBoard, self).__init__()
		for line in file:
			if line.strip() == '':
				break
			row = line.strip().replace('  ', ' ').split(' ')
			print("row", row)
			int_row = [int(num_str) for num_str in row]
			self.score += sum(int_row)
			self.board.append(int_row)
			# update number position map
			for i in range(len(int_row)):
				# row + column
				self.number_position.update({int_row[i]: str(len(self.board)) + str(i)})

	def play_number(self, number):
		has_won = False
		if number in self.number_position:
			self.score -= number
			row, column = list(self.number_position[number])
			row = int(row)
			column = int(column)
			board[row][column] = 0
			# check if the row won
			if sum(board[row]) == 0:
				has_won = True
			# check if the column won
			column_sum = None
			for row in board:
				if row == 0:
					column_sum = row[column]
				else:
				  	column_sum += row[column]
			if column_sum == 0:
				has_won = True
		return has_won, self.score

def part1():
	bingo_boards = []
	numbers = []
	try:
		with open('input.txt') as file:
			numbers = next(file).strip().split(',')
			# move past empty line
			next(file)
			while True:
				bingo_boards.append(BingoBoard(file))
				# print(len(bingo_boards))
	except Exception as e:
		print(e)
		print("finished reading file")

	# play game
	for number in numbers:
		for board in bingo_boards:
			has_won, score = board.play_number(number)
			if has_won:
				print("Winning score:", number * score)
				break

part1()
