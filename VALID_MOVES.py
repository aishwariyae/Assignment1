def valid_moves(maze, node):
    '''
    This function returns a list of "valid" neighbors for the current node in the rook-jumping-maze.

    Parameters:
    maze (list[list[int]]): The rook-jumping-maze represented as a 2-dimensional list of integers.
    node (tuple): The coordinates (x, y) of the current node for which we want to find valid neighbors.

    Returns:
    list[tuple]: A list of tuples representing valid neighbor coordinates.

    Note:
    - Valid neighbors are determined based on the number of moves allowed from the current node, as indicated by 'numberOfMoves'.
    - The 'maze' parameter contains information about the maximum number of moves that can be made from each cell.
    - The function iterates through possible directions (up, down, left, right) and checks if the neighbor is within the maze boundaries.
    - If using print statements for debugging, please remove them before the final submission.
    '''
	#used chatgpt to generate comments and debug the code.

    # Extract the current node's coordinates (x, y)
    x, y = node
    numberOfMoves = maze[x][y]  # Get the number of moves allowed from the current node
    k = len(maze)  # Determine the size of the maze (assuming it's a square maze)

    # Define possible movement directions (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Initialize an empty list to store valid neighbors
    neighbors = []

    # Iterate through possible directions to check for valid neighbors
    for i, j in directions:
        # Calculate potential neighbor coordinates (m, n)
        m, n = x + i * numberOfMoves, y + j * numberOfMoves

        # Check if the potential neighbor is within the maze boundaries
        if 0 <= m < k and 0 <= n < k:
            neighbors.append((m, n))  # Add the valid neighbor coordinates to the list

    return neighbors  # Return the list of valid neighbors