import os

def read() -> str:
	path = "\\".join(os.path.realpath(__file__).split("\\")[:-1])
	with open(f"{path}\\input.txt", "r") as file:
		return file.read().strip("\n")

def part1(file: str) -> int:
	lanterns = list(map(int, file.split(",")))
	# Iterate for 80 days
	for _ in range(80):
		# Decrement each timer by 1
		lanterns = [l - 1 for l in lanterns]
		for i in range(len(lanterns)):
			if lanterns[i] == -1:
				lanterns[i] = 6
				lanterns.append(8)

	return len(lanterns)

def part2(file: str) -> int:
	lanterns = [int(i) for i in file.split(",")]	
	# Dont store fishes, store how many in each state (my ram isnt crying anymore)
	states = {i: lanterns.count(i) for i in range(9)}
	# Iterate for 256 days
	for _ in range(256):
		# Shift (this effectively adds 1 to all)
		states = {i: states[(i + 1) % 9] for i in range(9)}
		# Reset fish from 0 to 6 (key 8 is used because we just shifted)
		if states[8] > 0:
			states[6] += states[8]

	return sum(states.values())		
