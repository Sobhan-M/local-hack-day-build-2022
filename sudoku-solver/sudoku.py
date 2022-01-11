
def printPuzzle(solution:list):
	print("")
	for i in range(9):
		print(f"{solution[i][0]} {solution[i][1]} {solution[i][2]} | {solution[i][3]} {solution[i][4]} {solution[i][5]} | {solution[i][6]} {solution[i][7]} {solution[i][8]}")
		if i == 2 or i == 5:
			print("------+-------+------")
	print("")

def hasUniqueRow(puzzle:list):
	for row in puzzle:
		for value in range(1, 10):
			if (row.count(value) > 1):
				return False
	return True

def hasUniqueColumn(puzzle:list):
	for i in range(9):
		column = [puzzle[0][i], puzzle[1][i], puzzle[2][i], puzzle[3][i], puzzle[4][i], puzzle[5][i], puzzle[6][i], puzzle[7][i], puzzle[8][i]]
		for value in range(1, 10):
			if (column.count(value) > 1):
				return False
	return True

def hasUniqueBlock(puzzle:list):
	for i in range(3):
		for j in range(3):

			# Create block as a list.
			block = []
			for k in range(3):
				for l in range(3):
					block.append(puzzle[3*i + k][3*j + l])

			for value in range(1, 10):
				if (block.count(value) > 1):
					return False
	return True

def puzzleWithSolution(puzzle:list, solution:list):

	puzzle_with_solution = [[], [], [], [], [], [], [], [], []]

	# Copying 2D array.
	for i in range(9):
		for j in range(9):
			puzzle_with_solution[i].append(puzzle[i][j])

	# Replacing each 0 in order with the solutions found.
	row = 0
	for value in solution:
		has_inserted = False

		for i in range(9):
			for j in range(9):
				if puzzle_with_solution[i][j] == 0:
					puzzle_with_solution[i][j] = value
					has_inserted = True
					break
			if has_inserted:
				break
	
	return puzzle_with_solution

def isValid(puzzle:list, solution:list):
	formatted_puzzle = puzzleWithSolution(puzzle, solution)
	return hasUniqueBlock(formatted_puzzle) and hasUniqueColumn(formatted_puzzle) and hasUniqueRow(formatted_puzzle)
	

def isSolved(puzzle:list, solution:list):
	formatted_puzzle = puzzleWithSolution(puzzle, solution)

	for i in range(9):
		if formatted_puzzle[i].count(0) > 0:
			return False
	return isValid(puzzle, solution)

def stringListToIntList(strings:list):
	for i in range(len(strings)):
		strings[i] = int(strings[i])
	return strings


def importPuzzle(file_name:str):
	puzzle = []

	with open(file_name) as f:
		for line in f:
			puzzle.append(stringListToIntList(line.split()))
	
	return puzzle


def main():
	
	file_name = input("\nPlease enter the file name of the puzzle: ")
	puzzle = importPuzzle(file_name)
	
	print("\nOriginal Puzzle:")
	printPuzzle(puzzle)

	solution = [0]

	while not isSolved(puzzle, solution):
		solution[-1] += 1

		if solution[-1] > 9:
			solution.pop()
		elif isValid(puzzle, solution):
			solution.append(0)

	print("Solved Puzzle:")
	printPuzzle(puzzleWithSolution(puzzle, solution))

	

if __name__ == "__main__":
	main()