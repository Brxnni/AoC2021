import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def part1(file: str) -> int:
	increased = 0
	# Split file to lines
	file = file.split("\n")
	# We dont compare the first number
	height = int(file[0])
	for line in file[1:]:
		line = int(line)
		if line > height:
			increased += 1
		height = line

	return increased

def part2(file: str) -> int:
	increased = 0
	# Split to lines
	file = file.split("\n")
	# Same thing as part 1 essentially
	height = sum(map(int, file[0:3]))
	for i in range(len(file) - 2):
		# Parse ints from 3 selected lines and get sum
		triplet = map(int, (file[i], file[i + 1], file[i + 2]))
		tripletSum = sum(triplet)
		# Count 1 up when bigger than last time
		if tripletSum > height:
			increased += 1
			for t in triplet: print(t)
		height = tripletSum
	
	return increased
