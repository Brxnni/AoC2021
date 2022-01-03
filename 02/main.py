import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def part1(file: str) -> int:
    # Start at (0, 0)
	horizontal = depth = 0
	for line in file.split("\n"):
		# Parse number after space to int
		amount = int(line.split(" ")[1])
		# Check for every command
		if line.startswith("forward"):
			horizontal += amount
		elif line.startswith("up"):
			depth -= amount
		elif line.startswith("down"):
			depth += amount
	
	# Multiply for final int
	return horizontal * depth

def part2(file: str) -> int:
    # Start at (0, 0) while aiming forward
	horizontal = depth = aim = 0 
	for line in file.split("\n"):
		# Parse number after space to int
		amount = int(line.split(" ")[1])
		# Check for every command
		if line.startswith("forward"):
			horizontal += amount
			depth += aim * amount
		elif line.startswith("up"):
			aim -= amount
		elif line.startswith("down"):
			aim += amount
	
	# Multiply for final int
	return horizontal * depth
