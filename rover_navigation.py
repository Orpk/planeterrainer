def get_neighbors(grid, position):
    """
    Find the four adjacent cells (up, down, left, right).
    Exclude cells outside the grid and cells containing obstacles.
    Return the valid neighboring positions.
    """


def heuristic(current, goal):
    """
    Calculate Manhattan distance between two positions.

    Manhattan distance:
    |x1 - x2| + |y1 - y2|

    This estimates the remaining distance to the destination.
    """


def find_path(grid, start, goal):
    """
    Implement the A* pathfinding algorithm.

    1. Initialize a priority queue with the starting position.
    2. Track the cost of reaching each position.
    3. Track each position's predecessor.
    4. Repeatedly explore the position with the lowest estimated
       total cost (actual distance + heuristic distance).
    5. Examine its valid neighbors.
    6. Update their costs and predecessors when a better route
       is discovered.
    7. Stop when the destination is reached.
    8. Reconstruct the path by following predecessors backwards.
    9. Return the path, or None if no route exists.

    Guides:
    - https://www.redblobgames.com/pathfinding/a-star/introduction.html
    - https://docs.python.org/3/library/heapq.html
    """