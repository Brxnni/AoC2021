import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def part1(file: str) -> int:
	# Split to lines
	file = file.split("\n")
	# Find gamma
	gamma = ""
	length = len(file[0])
	# Iterate column-wise
	for i in range(length):
		bits = [line[i] for line in file]
		# Find most common bit with count
		# This is O(n^2) but that doesn't matter because length is tiny
		commonBit = max(set(bits), key = bits.count)
		gamma += commonBit

	gamma = int(gamma, 2)
	# Epsilon is just the reverse of gamma
	epsilon = (2 ** length) - 1 - gamma
	
	# Multiply for final int
	return gamma * epsilon

def part2(file: str) -> int:
	# Split to lines
	file = file.split("\n")
	# Calculate oxygen generator rating
	oxygenNums = file
	i = 0	
	# Stop when there's only 1 number left
	while len(oxygenNums) > 1:
		# Find bits of all numbers in index i
		bits = [num[i] for num in oxygenNums]
		# Oxygen generator uses most common bit, use 1 if equal
		if bits.count("0") > bits.count("1"):
			commonBit = "0"
		else:
			commonBit = "1"
		# Filter for all numbers that have this bit in index i
		oxygenNums = [num for num in oxygenNums if num[i] == commonBit]
		# Go to next index
		i += 1 
 
	oxygenRating = int(oxygenNums[0], 2)

	# Same thing, but with CO2 scrubber rating
	co2Nums = file
	i = 0	
	# Stop when there's only 1 number left
	while len(co2Nums) > 1:
		# Find bits of all numbers in index i
		bits = [num[i] for num in co2Nums]
		# CO2 scrubber uses least common bit, use 0 if equal
		if bits.count("1") < bits.count("0"):
			commonBit = "1"
		else:
			commonBit = "0"
		# Filter for all numbers that have this bit in index i
		co2Nums = [num for num in co2Nums if num[i] == commonBit]
		# Go to next index
		i += 1

	co2Rating = int(co2Nums[0], 2)
 
	# Multiply for final int
	return oxygenRating * co2Rating

print(part2(read()))