import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def part1(file: str) -> int:
	diagram = [[0 for __ in range(1000)] for _ in range(1000)]
	# Fill diagram with lines
	for line in file.split("\n"):
		# Split line to coordinates		
		c1, c2 = line.split(" -> ")
		x1, y1 = c1.split(",")
		x2, y2 = c2.split(",")
		# Turn to integers
		x1, x2, y1, y2 = map(int, (x1, x2, y1, y2))
		# Ignore diagonal lines
		if not (x1 == x2 or y1 == y2):
			continue
		# Sort indexes, otherwise indexing doesnt work
		x, y = [x1, x2], [y1, y2]
		x.sort(); y.sort()
		x1, x2 = x
		y1, y2 = y
		# Loop through every point the line touches
		for x in range(x1, x2 + 1):
			for y in range(y1, y2 + 1):
				diagram[y][x] += 1
	# Count cells with number higher than 1
	return sum([sum([c >= 2 for c in line]) for line in diagram])

# This is the exact same thing as part1, but without the continue statement
def part2(file: str) -> int:
	diagram = [[0 for __ in range(1000)] for _ in range(1000)]
	# Fill diagram with lines
	for line in file.split("\n"):
		# Split line to coordinates		
		c1, c2 = line.split(" -> ")
		x1, y1 = c1.split(",")
		x2, y2 = c2.split(",")
		# Turn to integers
		x1, x2, y1, y2 = map(int, (x1, x2, y1, y2))
		# Loop through every point the line touches
		# If line is straight this works
		if x1 == x2 or y1 == y2:
			# Sort indexes, otherwise indexing doesnt work
			x, y = [x1, x2], [y1, y2]
			x.sort(); y.sort()
			x1, x2 = x
			y1, y2 = y  
			for x in range(x1, x2 + 1):
				for y in range(y1, y2 + 1):
					diagram[y][x] += 1
		# Diagonal case
		else:
			xPoints = list(range(x1, x2 + (1 if x2 > x1 else -1), -1 if x1 > x2 else 1))
			yPoints = list(range(y1, y2 + (1 if y2 > y1 else -1), -1 if y1 > y2 else 1))
			for i in range(len(xPoints)):
				diagram[yPoints[i]][xPoints[i]] += 1
	# Count cells with number higher than 1
	return sum([sum([c >= 2 for c in line]) for line in diagram])
