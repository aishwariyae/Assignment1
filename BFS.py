import numpy as np
from VALID_MOVES import valid_moves

def BFS(maze, start):

    '''
    Fill in this function that uses Breadth First Search to find the shortest path 
    from the start state to the goal state.
    
    Return the matrix (a 2-dimensional numpy array) of shortest path 
    distances from the start cell to each cell. 
    
    If no path exists from the start state to a given cell, that cell should be assigned -1.
    
    The start state should be assigned a path lenght of 0.
    
    If using print statements to debug, please make sure 
    to remove them before your final submisison.
    '''
    #Get the size of maze (square maze)
    size = len(maze)
    #Initialize a 2D numpy array to store short distances
    path_matrix = np.full((size, size), -1)
    # Initialize a deque for BFS with (cell, distance) tuples
    queue = deque([(start, 0)])
    # Set the starting cell's path length to 0.
    path_matrix[start[0]][start[1]] = 0
    #sourced chatgpt for comments, debugging code and refactoring

    # Execute BFS traversal.
    while queue:
        current_cell, distance = queue.popleft()

        # Find valid moves (neighbors) from the current cell using the valid_moves function.
        neighbors = valid_moves(maze, current_cell)

        # Explore each valid neighbor
        for neighbor in neighbors:
            x1, x2 = neighbor

            # Check if the cell is unvisited or a shorter path is found.
            if path_matrix[x1][x2] == -1 or path_lengths[x1][x2] > distance + 1:
                path_matrix[x1][x2] = distance + 1

                # Add the neighbor cell to the queue with an updated distance.
                queue.append(((x1, x2), distance + 1))

    # Return the matrix of shortest path distances.
    return path_matrix




