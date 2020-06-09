# Author
# Angelica ACOSTA ARTETA

# Structure that will represent the grid
class Grid:
	
	def __init__(self, matrix):
		self.matrix = matrix
		self.rows = len(matrix) 
		self.columns = len(matrix[0])

	# Function that will tell us if the cell exist
	def validCell(self, i, j):
		return (
			i>=0 and i<self.rows and 	# checks the row exists
			j>=0 and j<self.columns		# checks the column exists
		)
	
	def validMove(self, i, j, visitedCell):
		if self.validCell(i,j):
			return(
				self.matrix[i][j] and		# checks if it is not a wall
				not visitedCell[i][j]		# checks if it has not been visited
			)
		return(False)
		
	# Function that will let us modify the matrix by adding a wall
	def addWall(self, i, j):
		if self.validCell(i,j):
			self.matrix[i][j]=0
	
	# Function that will let us modify the matrix by removing a wall
	def removeWall(self, i, j):
		if self.validCell(i,j):
			self.matrix[i][j]=1

	# Function that will navigate the matrix as much as posible within the walls
	def DFS(self, i, j, visitedCell):
		# The neighbours of a cell i,j are represented by
		# the pairs of i+rowNeighbour[k], j+colNeighbour[k]
		rowNeighbours = [-1, 0, 0, 1] # Only four because we can only move up or down
		colNeighbours = [0, -1, 1, 0]

		# We are in cell i,j so we mark it as visited
		visitedCell[i][j] = 1

		for k in range(4):
			nRow = i+rowNeighbours[k] # The row of a neighbour
			nCol = j+colNeighbours[k] # The column of a neighbour
			
			if self.validMove(nRow, nCol, visitedCell):
				# If the movement is valid and we have not visited the cell, we keep moving
				self.DFS(nRow, nCol, visitedCell) 

	# Function that will calculate how many enclosed spaces we have. We will need one robot
	# space
	def calculateRobots(self):

		# We create a grid that will tell us if we heve been to a specific cell
		# We initialize it with 0 to represent we have not visited any cells
		visited=[[0 for j in range(self.columns)]for i in range(self.rows)] 

		spaces=0
		for i in range(self.rows):
			for j in range(self.columns):
				if not visited[i][j] and self.matrix[i][j]:
					self.DFS(i, j, visited)
					spaces+=1
		
		return spaces
