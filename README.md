# n-puzzleProblem
My project in **Python** to solve the first problem in **AI** domain. The problem is defined here: [15 puzzle - Wikipedia](https://en.wikipedia.org/wiki/15_puzzle)

## Authors
* Huy Mai TRUONG you can find my profile [**here**](https://nacriema.github.io/).

## Program

### Usage
In the command line:
$ python nPuzzleSolver.py [search_method] [puzzle]

where search_method: 'bfs', 'dfs' or 'ast'
where puzzle is a comma-seperated list of number from 0 to n^2 - 1.

eg.
$ python nPuzzleSolver.py bfs 0,1,2,3,4,5,6,7,8

Prepresent the puzzle

|   | 1 | 2 |
|---|---|---|
| 3 | 4 | 5 |
| 6 | 7 | 8 |

where 0 is the blankspace

This implementation treats the goal state as:

| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
| 7 | 8 |   |

### Returns:
* Path to the goal. In the next version, I will make some ccriterias to evaluate each type of algorithm.


## Why I do this ? 
* To learn Python syntaxes.
* To solve problem gived by my teacher at University - my first lesson is to learn about searching Algorithm.

## References
* Documentation about the Algorithm I learn from [**here**.](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
* Many thanks to [Andavie](https://github.com/andavies), who give me the way how to implement that in Python.


