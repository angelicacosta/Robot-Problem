# Project Title

The Robot Problem: A first requirements specification - source code file robot.py

This solution is based in the "Find the number of islands | Set 1 (Using DFS)" that can be found in https://www.geeksforgeeks.org/find-number-of-islands/

## Getting Started

### Prerequisites

The program is written in Python (version 3.5.2),
downloaded from https://www.python.org/downloads/

### Installing

Follow the instructions at the web site.

## About the Solution

A Grid class was created. It has the following attributes:
- Matrix: represents the grids with 0 and 1s. The 0s represent walls.
- Rows: number of rows on the grid.
- Columns: number of columns on the grid.

## Running the tests

You can test the functions by typing:
```
$ python test_robot.py
```

### Unit tests

In the file test_robot.py you can see the tests made for the following methods:

- validCell: determines if a cell is within the bounderies of the grid.
- validMove: determines if a cell hasn't been visited and is not a wall. 
- addWall: allows to modify the grid's matrix and add a wall in a specific cell.
- removeWall: allows to modify the grid's matrix and add a wall in a specific cell.
- DFS: given an initial position, will move through the grid as far away as it can. It cannot go through wall.
- calculateRobots: it counts how many closed spaces are in the grid, as we will need a robot for each closed space.

### Validation tests

To try the solution, import the class Grid from robot.py and create a grid. Eg:
```
g=Grid([[1,1,1,0,1,1,1,0,1,1],
		[1,0,1,0,1,1,1,0,1,1],
		[1,1,1,0,1,1,1,0,1,1],
		[0,0,0,1,1,1,1,0,1,1],
	    [1,1,1,0,1,1,1,0,1,1]])

```
Then, you can use the method calculateRobots() as follows:
```
g.calculateRobots()
# In this example, calculateRobots() will return 4
```

## Built With

```
python  --version
Python 3.5.2

```

## Versioning

You can find the program in the following GitHub repository
https://github.com/angelicacosta/Robot-Problem

Version 1 - robot.py - Functionalities complete. 
Version 1 - test_robot.py - Few tests

## Authors

### Primary Author

Angelica Acosta Arteta

## License

This project is licensed under the MIT License - see the license.txt file for details
