
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
		column = [puzzle[0][i], puzzle[1][i], puzzle[2][i], puzzle[3][i], puzzle[4][i], puzzle[5][i], puzzle[6][i], puzzle[7][i], puzzle[8[i]]]
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

	puzzleWithSolution = [[], [], [], [], [], [], [], [], []]

	# Copying 2D array.
	for i in range(9):
		for j in range(9):
			puzzleWithSolution[i].append(puzzle[i][j])

	# Replacing each 0 in order with the solutions found.
	row = 0
	for value in solution:
		hasInserted = False

		for i in range(9):
			for j in range(9):
				if puzzleWithSolution[i][j] == 0:
					puzzleWithSolution[i][j] = value
					hasInserted = True
					break
			if hasInserted:
				break
	
	return puzzleWithSolution
	



# def isValid(puzzle, solution):
	

# def isSolved(puzzle, solution):




def main():
	# Hard-coded puzzle for testing:
	puzzle = [
		[5, 3, 0, 0, 7, 0, 0, 0, 0],
		[6, 0, 0, 1, 9, 5, 0, 0, 0],
		[0, 9, 8, 0, 0, 0, 0, 6, 0],
		[8, 0, 0, 0, 6, 0, 0, 0, 3],
		[4, 0, 0, 8, 0, 3, 0, 0, 1],
		[7, 0, 0, 0, 2, 0, 0, 0, 6],
		[0, 6, 0, 0, 0, 0, 2, 8, 0],
		[0, 0, 0, 4, 1, 9, 0, 0, 5],
		[0, 0, 0, 0, 8, 0, 0, 7, 9]
	]

	is_solved = False
	

	printPuzzle(sudoku)

if __name__ == "__main__":
	main()