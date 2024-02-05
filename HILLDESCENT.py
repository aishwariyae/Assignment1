import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR
import random


def energyfunction(maze, start, goal):
	'''
	Compute the energy as the sum of the shortest path length 
	from the start state to the goal state (computed using A*)
	and the number of cells that are not reachable from the 
	start state (computed using BFS).

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''
	# Use A* to find the shortest path length
	shortest_path_length = ASTAR(maze, start, goal)

	# Use BFS to find the number of unreachable cells
	path_matrix = BFS(maze, start)
	unreachable_cells_count = np.sum(path_matrix == -1)

	# Compute energy as the sum of path length and unreachable cells
	energy = shortest_path_length[0] + unreachable_cells_count
	return energy



def HILLDESCENT(maze, start_cell, goal_state, iterations):
	'''
	Fill in this function to implement Hill Descent local search.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze 
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''
	bestSolution = np.copy(maze)
	bestEnergy = energyfunction(bestSolution, start_cell, goal_state)

	# Perform hill descent for a specified number of iterations.
	for i in range(iterations):
		new_maze = np.copy(bestSolution)
		r, c = random.choice(np.argwhere(new_maze != 0))
		new_maze[r, c] = random.randint(1, len(new_maze) - 1)

		new_energy = energyfunction(new_maze, start_cell, goal_state)
		# If the new solution has lower energy, update the best solution.
		if new_energy < bestEnergy:
			bestSolution = new_maze
			bestEnergy = new_energy

	return (bestSolution, bestEnergy)



def HILLDESCENT_RANDOM_RESTART(maze, start_cell, goal_state, iterations, num_searches):
	'''
	Fill in this function to implement Hill Descent local search with Random Restarts.

	For a given number of searches (num_searches), run hill descent search.

	Keep track of the best solution through all restarts, and return that.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze 
	before making any changes to it.

	You will also need to keep a separate copy of the original maze
	to use when restarting the algorithm each time.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''
	best_maze = None
	best_energy = float("inf")

	# Perform hill descent with random restarts for a specified number of searches.
	for i in range(num_searches):

		current_maze = np.copy(maze)
		current_energy = (energyfunction(current_maze, start_cell, goal_state))

		current_maze, current_energy = HILLDESCENT(current_maze, start_cell, goal_state, iterations)

		# If the current solution has lower energy, update the best solution.
		if current_energy < best_energy:
			best_maze = current_maze
			best_energy = current_energy

	return (best_maze, best_energy)

def HILLDESCENT_RANDOM_UPHILL(maze, start_cell, goal_state, iterations, probability):
	'''
	Fill in this function to implement Hill Descent local search with Random uphill steps.

	At each iteration, with probability specified by the probability
	argument, allow the algorithm to move to a worse state.

	Your function should return the best solution found, 
	which should be a tuple containing 2 elements:

	1. The best maze found, which is a 2-dimensional numpy array.
	2. The energy of the best maze found.

	Note that you should make a local copy of the maze
	before making any changes to it.

	If using print statements to debug, please make sure
	to remove them before your final submisison.
	'''
	best_maze = np.copy(maze)
	best_energy = energyfunction(best_maze, start_cell, goal_state)

	# Perform hill descent with random uphill steps for a specified number of iterations.
	for i in range(iterations):
		new_maze = np.copy(best_maze)

		if random.random() < probability:
			r, c = random.choice(np.argwhere(new_maze != 0))
			new_maze[r, c] = random.randint(1, len(new_maze) - 1)
			new_energy = energyfunction(new_maze, start_cell, goal_state)
			if new_energy < best_energy:
			   best_maze = new_maze
			   best_energy = new_energy

	return (best_maze, best_energy)






