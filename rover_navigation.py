
# rover_navigation.py

import heapq


# ============================================================
# 1. GET NEIGHBOURS
# ============================================================

def get_neighbors(grid, position):
    """
    Find all valid cells immediately adjacent to the current cell.

    STEP 1: Extract the current row and column.

    STEP 2: Define the four possible movement directions:
        Up    = (-1, 0)
        Down  = (1, 0)
        Left  = (0, -1)
        Right = (0, 1)

    STEP 3: Calculate the coordinates of each neighbour.

    STEP 4: Check whether each neighbour is inside the grid.

    STEP 5: Check whether the neighbour is an obstacle (0).

    STEP 6: Return only valid neighbours.

    GUIDE:
    https://docs.python.org/3/tutorial/controlflow.html
    """

    row, col = position

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        # Check grid boundaries.
        if (0 <= new_row < len(grid)
                and 0 <= new_col < len(grid[0])):

            # Ignore obstacles.
            if grid[new_row][new_col] != 0:
                neighbors.append((new_row, new_col))

    return neighbors


# ============================================================
# 2. HEURISTIC FUNCTION
# ============================================================

def heuristic(current, goal):
    """
    Estimate the remaining distance to the destination.

    We use Manhattan distance because movement is restricted
    to four directions.

    Formula:
        h = |row1 - row2| + |col1 - col2|

    This estimate never overestimates the minimum remaining
    movement cost when the minimum terrain cost is 1.

    STEP 1: Extract current and goal coordinates.

    STEP 2: Calculate the absolute row difference.

    STEP 3: Calculate the absolute column difference.

    STEP 4: Return their sum.
    """

    return (
        abs(current[0] - goal[0])
        + abs(current[1] - goal[1])
    )


# ============================================================
# 3. A* PATHFINDING
# ============================================================

def find_path(grid, start, goal):
    """
    Find the lowest-cost path from start to goal.

    A* uses:
        f(n) = g(n) + h(n)

        g(n): Actual cost from the starting point.
        h(n): Estimated cost to the destination.
        f(n): Total estimated cost.

    STEP 1: Validate the start and goal.
        - Both must be inside the grid.
        - Neither can be an obstacle.

    STEP 2: Initialize the priority queue.
        - Use heapq.
        - Store (estimated_total_cost, current_position).
        - The smallest estimated cost is processed first.

    STEP 3: Initialize dictionaries.
        - came_from: Records the previous cell.
        - cost_so_far: Records the cheapest known cost.

    STEP 4: Start the search.
        - Remove the lowest-cost position from the queue.
        - If it is the goal, stop searching.

    STEP 5: Examine all valid neighbours.
        - Calculate movement cost using the destination terrain.
        - Update the neighbour if a cheaper route is found.

    STEP 6: Reconstruct the route.
        - Follow came_from backwards from goal to start.
        - Reverse the resulting list.

    STEP 7: Return the route.
        - Return None if no valid route exists.

    GUIDE:
    https://www.redblobgames.com/pathfinding/a-star/introduction.html
    https://docs.python.org/3/library/heapq.html
    """

    rows = len(grid)
    cols = len(grid[0])

    # Validate coordinates.
    for position in (start, goal):
        r, c = position

        if not (0 <= r < rows and 0 <= c < cols):
            return None

        if grid[r][c] == 0:
            return None

    # Priority queue: (estimated cost, position).
    frontier = []

    heapq.heappush(
        frontier,
        (heuristic(start, goal), start)
    )

    # Store the previous cell for route reconstruction.
    came_from = {start: None}

    # Actual accumulated cost from the start.
    cost_so_far = {start: 0}

    while frontier:

        # Get the cell with the lowest estimated total cost.
        _, current = heapq.heappop(frontier)

        # Goal reached.
        if current == goal:
            break

        # Explore neighbouring cells.
        for neighbor in get_neighbors(grid, current):

            r, c = neighbor

            # Movement cost depends on terrain.
            new_cost = (
                cost_so_far[current] + grid[r][c]
            )

            # Check whether this route is cheaper.
            if (neighbor not in cost_so_far
                    or new_cost < cost_so_far[neighbor]):

                cost_so_far[neighbor] = new_cost

                priority = (
                    new_cost + heuristic(neighbor, goal)
                )

                heapq.heappush(
                    frontier,
                    (priority, neighbor)
                )

                came_from[neighbor] = current

    # No route was found.
    if goal not in came_from:
        return None

    # Reconstruct route from goal back to start.
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    # Reverse so the route starts at the rover.
    path.reverse()

    return path


# ============================================================
# 4. ROVER SIMULATION
# ============================================================

def simulate_rover(
    grid,
    path,
    battery=100.0,
    energy_per_cost=1.0,
    new_obstacles=None
):
    """
    Simulate the rover following its calculated route.

    Parameters:
        grid:
            Weighted terrain grid.

        path:
            Route returned by find_path().

        battery:
            Initial battery percentage (0 to 100).

        energy_per_cost:
            Battery percentage consumed per unit terrain cost.

        new_obstacles:
            Optional dictionary containing newly discovered
            obstacles, e.g. {3: (5, 6)}.

            This means a new obstacle is discovered before
            the rover's third movement.

    STEP 1: Copy the grid.
        - Do not modify the original terrain map.
        - Use list comprehensions to make a deep copy.

    STEP 2: Initialize simulation variables.
        - Current rover position.
        - Remaining battery.
        - Distance travelled.
        - Movement history.
        - Event messages.

    STEP 3: Begin moving.
        - The rover follows the next cell in its current route.
        - Each movement consumes energy.

    STEP 4: Check for newly discovered obstacles.
        - Mark the obstacle as impassable.
        - Check whether it blocks the remaining route.

    STEP 5: If the route is blocked:
        - Call find_path() again.
        - Use the rover's current position as the new start.
        - Keep the original destination.

    STEP 6: Check available battery.
        - If insufficient, stop the simulation.
        - Record a low-battery event.

    STEP 7: Update rover position and statistics.

    STEP 8: Stop when:
        - The destination is reached.
        - No route remains.
        - Battery is depleted.

    STEP 9: Return simulation results.

    GUIDE:
    https://docs.python.org/3/tutorial/datastructures.html
    """

    import copy

    # STEP 1: Copy terrain map.
    simulated_grid = copy.deepcopy(grid)

    # STEP 2: Initialize variables.
    current = path[0]
    goal = path[-1]

    battery = max(0.0, min(100.0, battery))

    distance = 0
    route_taken = [current]
    events = []

    # STEP 3: Handle optional obstacle events.
    if new_obstacles is None:
        new_obstacles = {}

    movement_count = 0

    # Continue until destination is reached.
    while current != goal:

        # STEP 4: Check for newly discovered obstacles.
        next_move_number = movement_count + 1

        if next_move_number in new_obstacles:

            obstacle = new_obstacles[next_move_number]

            r, c = obstacle

            # Only modify valid grid coordinates.
            if (0 <= r < len(simulated_grid)
                    and 0 <= c < len(simulated_grid[0])
                    and obstacle != current):

                simulated_grid[r][c] = 0

                events.append(
                    f"New obstacle detected at {obstacle}"
                )

                # STEP 5: Recalculate route.
                new_path = find_path(
                    simulated_grid,
                    current,
                    goal
                )

                if new_path is None:
                    events.append("No alternative route!")
                    break

                path = new_path

                events.append("Route successfully recalculated")

        # The next cell in the current route.
        next_position = path[1]

        r, c = next_position

        # STEP 6: Calculate energy consumption.
        energy_used = (
            simulated_grid[r][c] * energy_per_cost
        )

        # Stop if insufficient battery.
        if battery < energy_used:
            events.append("Battery depleted before next movement")
            break

        # STEP 7: Update simulation.
        battery -= energy_used

        distance += 1
        movement_count += 1

        current = next_position
        route_taken.append(current)

        # Remove the cell just visited from the planned route.
        path = path[1:]

    # STEP 8: Determine completion status.
    completed = (current == goal)

    if completed:
        events.append("Destination successfully reached")

    # STEP 9: Return all relevant results.
    return {
        "completed": completed,
        "final_position": current,
        "battery_remaining": battery,
        "distance_travelled": distance,
        "route_taken": route_taken,
        "events": events,
        "final_grid": simulated_grid
    }
