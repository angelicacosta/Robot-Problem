# Author
# Angelica ACOSTA ARTETA

import unittest
from robot import Grid

class TestBalance(unittest.TestCase):

	def test_creationGrid(self):
		g=Grid([[1]])
		self.assertEqual(g.matrix,[[1]])
		self.assertEqual(g.rows,1)
		self.assertEqual(g.columns,1)
	
	def test_validCell(self):
		g=Grid([[1,1],
				[1,1]])
		self.assertEqual(g.validCell(0,0), True)
		self.assertEqual(g.validCell(1,1), True)
		self.assertEqual(g.validCell(-1,0), False)
		self.assertEqual(g.validCell(0,2), False)
		self.assertEqual(g.validCell(3,2), False)
	
	def test_addWall(self):
		g=Grid([[1,1],
				[1,1]])
		g.addWall(0,0)
		self.assertEqual(g.matrix[0][0], 0)
		g.addWall(1,1)
		self.assertEqual(g.matrix[1][1], 0)
	
	def test_removeWall(self):
		g=Grid([[0,0],
				[0,0]])
		g.removeWall(1,0)
		self.assertEqual(g.matrix[1][0], 1)
		g.removeWall(1,1)
		self.assertEqual(g.matrix[1][1], 1)

	def test_DFS(self):
		g=Grid([[1,0],
				[0,1]])
		visited=[[0,0],
				 [0,0]]
		g.DFS(0,0,visited)
		self.assertEqual(visited, [[1,0],[0,0]])

	def test_calculateRobots(self):
		g=Grid([[1,1,1,0,1,1,1,1,1,1],
				[1,0,1,0,1,1,1,1,1,1],
				[1,1,1,0,1,1,1,0,1,1],
				[0,0,0,0,1,1,1,1,1,1],
				[1,1,1,1,1,1,1,1,1,0],
				[1,1,1,1,1,0,1,1,0,1],
				[1,1,1,1,1,1,1,1,0,0],
				[1,1,1,1,1,1,1,1,1,1]])
		self.assertEqual(g.calculateRobots(), 3)


if __name__ == '__main__':
	unittest.main()