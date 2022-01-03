import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def part1(file: str) -> str:
	# Parse file
	crabs = list(map(int, file.split(",")))
	# Store fuel usages
	usages = []
	# Loop through every possible alignment position
	for i in range(min(crabs), max(crabs) + 1):
		# Calculate total fuel cost to horizontal position i
		fuelUsage = sum([abs(crab - i) for crab in crabs])
		usages.append(fuelUsage)

	return min(usages)

def part2(file: str) -> str:
	# Parse file
	crabs = list(map(int, file.split(",")))
	# Store fuel usages
	usages = []
	# Loop through every possible alignment position
	for i in range(min(crabs), max(crabs) + 1):
		# Calculate total fuel cost to horizontal position i
		fuelUsage = sum([sum(range(1, abs(crab - i) + 1)) for crab in crabs])
		usages.append(fuelUsage)

	return min(usages)
