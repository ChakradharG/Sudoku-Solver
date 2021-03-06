board = [[0 for i in range(9)] for j in range(9)]
moves = {}	#To keep track of the moves made to solve the board

def checkList(l):
	'''
	Checks if there are no duplicates (except for 0) in a list
	'''
	numCnt = {0:0}
	for i in l:
		numCnt[i] = numCnt.get(i, 0) + 1
	del numCnt[0]
	for i in numCnt.values():
		if i > 1:
			return False
	return True


def checkRow(r):
	return checkList(board[r][:])


def checkCol(c):
	column = []
	for i in range(9):
		column.append(board[i][c])
	return checkList(column)


def checkBox(r, c):
	box = []
	for i in range(r, r+3):
		for j in range(c, c+3):
			box.append(board[i][j])
	return checkList(box)


def solve(r, c):
	'''
	Recursive function that scans the board row wise starting from location r,c 
	and tries to put a number between 1 and 9 where it finds a 0
	'''
	i, j = r, c
	while i < 9:
		while j < 9:
			if board[i][j] == 0:
				for x in range(1, 10):
					board[i][j] = x
					if checkRow(i) and checkCol(j) and checkBox(i-i%3, j-j%3):
						#if placing digit x at i,j doesn't violate the property then call self to solve for next 0
						if solve(i, j):
							moves[(i, j)] = x
							break
				else:
					#No valid value found for i,j so backtrack
					board[i][j] = 0
					return False
				#Valid value found for i,j
				return True
			j += 1
		i += 1
		j = 0
	#No more 0s in the board to solve
	return True
