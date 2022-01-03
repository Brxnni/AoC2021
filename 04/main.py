import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def isWinning(marked: list[bool]) -> bool:
	return any([
		# Rows
		all(marked[0:5]),
		all(marked[5:10]),
		all(marked[10:15]),
		all(marked[15:20]),
		all(marked[20:25]),
		# Columns
		all([marked[i*5] for i in range(5)]),
		all([marked[i*5+1] for i in range(5)]),
		all([marked[i*5+2] for i in range(5)]),
		all([marked[i*5+3] for i in range(5)]),
		all([marked[i*5+4] for i in range(5)])
	])

def part1(file: str) -> int:
	# Split to lines
	file = file.split("\n")
	# First line is the drawn numbers	
	drawnNumbers = file[0].split(",")
	# Parse boards
	boards = []
	# Boards are seperated by 2 newlines
	for board in "\n".join(file[2:]).split("\n\n"):
		# Remove extra spaces
		board = board.replace("\n", " ").replace("  ", " ").strip()
		board = board.split(" ")
		# Add board numbers and marked mask
		boards.append([
      		board,
        	[False for __ in range(25)]
		])
	
	for number in drawnNumbers:
		for board in boards:
			# Check if number present on board
			if number in board[0]:
				# Get index of chosen number
				index = board[0].index(number)
				# Set corresponding boolean to true
				board[1][index] = True
				# Check if this board has won now
				if isWinning(board[1]):
					# Calculate score
					sumUnmarked = sum([int(board[0][i]) for i in range(25) if not board[1][i]])
					score = sumUnmarked * int(number)
					return sumUnmarked, number, score

def part2(file: str) -> int:
	# The first part (parsing) is the same
	# Split to lines
	file = file.split("\n")
	# First line is the drawn numbers	
	drawnNumbers = file[0].split(",")
	# Parse boards
	boards = []
	# Boards are seperated by 2 newlines
	for board in "\n".join(file[2:]).split("\n\n"):
		# Remove extra spaces
		board = board.replace("\n", " ").replace("  ", " ").strip()
		board = board.split(" ")
		# Add board numbers and marked mask
		boards.append([
	  		board,
	    	[False for __ in range(25)]
		])

	# Store which board has already won
	won = [False for _ in range(len(boards))]
	for number in drawnNumbers:
		for boardIndex, board in enumerate(boards):
			# No need to do unnecessary work on finished boards
			if won[boardIndex]: continue
			# Check if number present on board
			if number in board[0]:
				# Get index of chosen number
				index = board[0].index(number)
				# Set corresponding boolean to true
				board[1][index] = True
				# Check if this board has won now
				if isWinning(board[1]):
					# Calculate score
					sumUnmarked = sum([int(board[0][i]) for i in range(25) if not board[1][i]])
					score = sumUnmarked * int(number)
					# Check if this is the last board to win	
					if won.count(False) == 1:
						return score
					else:
						won[boardIndex] = True
