import heapq
import numpy as np
from VALID_MOVES import valid_moves

def H_score(node, goal, n):
	'''
	Fill in this function to return the heuristic value of the current node.

	Compute heuristic as the Manhattan distance between the 
	current node and the goal state, divided by 
	the largest possible jump value.

	n is the dimensionality of the maze (n x n).

	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''
	nodeX1, nodeX2 = node
	goalX1, goalX2 = goal
	#calc manhattan distance between current node and goal
	manhattan_distance = (abs(nodeX1 - goalX1) + abs(nodeX2 - goalX2))
	#calc heuristic value using manhattan distance
	heuristic = manhattan_distance / (n - 1)
	return heuristic

def reconstruct_path(node, node_info):
    path = []
    while node:
        path.append(node)
        node = node_info[node]['parent']
    return path[::-1]

def ASTAR(maze, start, goal):
	'''
	Fill in this function that uses A* search to find the shortest 
	path using the heuristic function H_score defined above.

	Return the length of the shortest path from the start state 
	to the goal state, and the path itself.

	Your return statement should be of the form:
	return len(path)-1, path

	where path is a list of tuples, corresponding to the 
	path and includes the start state.

	If using print statements to debug, please make sure 
	to remove them before your final submisison.
	'''
	#Initialize an open list
	n = len(maze)
	open_list = []
	#Initialize closed list to keep track of nodes visited
	closed_list = set()

	#Priority queue for open list starting with the 'start' node and cost 0.
	heapq.heappush(open_list, (0, start))
	node_info = {start: {'parent': None, 'g': 0}}

	while open_list:
		# Pop the node with the lowest total cost 'f' from the open list.
		f, node = heapq.heappop(open_list)
		#if current node is the goal, reconstruct the path and return the path
		if node == goal:
			path = reconstruct_path(current_node, node_info)
			return len(path)-1, path
		# Add the current node to the closed list to mark it as visited.
		closed_list.add(node)
		adjacent = valid_moves(maze, node)

		for adj in adjacent:
			g = node_info[node]['g'] + 1

			#if the next element already in closed list, skip it
			if adj in closed_list:
				continue
			# If the next element is not in the node_info dictionary or has a lower cost 'g',
			# push the updated information to the open list with a new 'f' value.
			if adj not in node_info or g < node_info[adj]['g']:
				node_info[adj] = {'parent': node, 'g': g}
				f = g + H_score(adj, goal, n)
				heapq.heappush(open_list, (f, adj))
    #if path not found return a tuple indicating failure
	return (-1, ())








