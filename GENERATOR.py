import sys
import numpy as np
from BFS import BFS


def generator(k):
	#chatgpt used for comments debugging and refactoring
	"""
    Generate a k * k maze with random integers between 1 and k-1 in each cell.
    Generate random start and goal states, ensuring they are not the same.
    Set the entry in the maze corresponding to the goal state to 0.

    Parameters:
    - k: Size of the maze

    Returns:
    - init_board: Generated maze
    - start_cell: Random start state
    - goal_state: Random goal state
    """
	# Generate a random k * k maze
	init_board = np.random.randint(1, k, size=(k, k))

	# Generate random start and goal states
	start_cell = tuple(np.random.randint(0, k, size=2))
	goal_state = tuple(np.random.randint(0, k, size=2))

	if start_cell == goal_state:
		# Regenerate goal state until it's different from start state
		while start_cell == goal_state:
			goal_state = tuple(np.random.randint(0, k, size=2))

	# Set the entry in the maze for the goal state to 0
	init_board[goal_state] = 0

	return init_board, start_cell, goal_state


def generator_pathcheck(k):
	"""
    Generate a maze, a start state, and a goal state, ensuring a valid path exists between start and goal.

    Parameters:
    - k: Size of the maze

    Returns:
    - init_board: Generated maze
    - start_cell: Random start state
    - goal_state: Random goal state
    """
	while True:
		# Generate maze, start, and goal
		init_board, start_cell, goal_state = generator(k)

		# Check if there is a valid path from start state to goal state using BFS
		path_lengths = breadth_first_search(init_board, start_cell)

		# If a valid path exists, return maze, start state, and goal state
		if np.any(path_lengths != -1):
			return init_board, start_cell, goal_state