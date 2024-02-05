import sys
import numpy as np
from BFS import BFS
from ASTAR import ASTAR
from HILLDESCENT import energyfunction
import random
# chatGPT was used for adding Comments and debugging the code.

# Define a function for Simulated Annealing algorithm
def SIMULATED_ANNEALING(maze, start_cell, goal_state, iterations, T, decay):
	'''
	    This function implements the Simulated Annealing algorithm to find a solution for a maze.

	    Parameters:
	    maze (numpy.ndarray): The maze represented as a 2-dimensional numpy array.
	    start_cell (tuple): The starting cell coordinates in the maze.
	    goal_state (int): The goal state in the maze.
	    iterations (int): The number of iterations for the algorithm.
	    T (float): The initial temperature for the annealing process.
	    decay (float): The rate at which temperature decreases in each iteration.

	    Returns:
	    tuple: A tuple containing the best maze found (as a numpy array) and its energy.

	    Note:
	    - The energy function used here is the same as used for Hill Descent and is provided in HILLDESCENT.py.
	    - The algorithm makes use of probability to decide whether to move to a new state or stay in the current state.
	    - The temperature 'T' decreases at each iteration by multiplying it by the decay rate 'decay'.
	    - The best solution found is returned as a tuple with the maze and its energy.
	    - It is recommended to remove any debug print statements before final submission.
	    '''

	# Initialize the best maze and its energy with the current maze
	bestMaze = np.copy(maze)
	bestEnergy = energyfunction(bestMaze, start_cell, goal_state)

	# Initialize the current maze and its energy with the best maze
	currentMaze = np.copy(maze)
	currentEnergy = bestEnergy

	# Iterate for the specified number of iterations
	for iteration in range(iterations):
		# Randomly select a cell to modify
		row, col = random.choice(np.argwhere(currentMaze != 0))
		# Modify the cell with a random value between 1 and the maze size minus one
		currentMaze[row, col] = random.randint(1, len(currentMaze) - 1)

		# Calculate the energy of the new maze
		newEnergy = energyfunction(currentMaze, start_cell, goal_state)

		# Calculate the change in energy (delta_energy)
		deltaEnergy = currentEnergy - newEnergy

		# Check if the new state should be accepted based on energy and probability
		if deltaEnergy < 0 or random.random() < math.exp(-deltaEnergy / T):
			# Update the current maze and its energy
			currentMaze = np.copy(currentMaze)
			currentEnergy = newEnergy

			# If the new energy is better than the best energy, update the best maze and best energy
			if new_energy < best_energy:
				bestMaze = np.copy(currentMaze)
				bestEnergy = newEnergy

		# Decrease the temperature for the next iteration
		T *= decay

	# Return the best solution found
	return (bestMaze, bestEnergy)
