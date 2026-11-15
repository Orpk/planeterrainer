from queue import PriorityQueue


def get_neighbors(grid, position):
    ava = [0, 0, 0, 0]
    x = position[0]
    y = position[1]

    try:
        if y - 1 >= 0:
            ava[0] = grid[y - 1][x]
    except IndexError:
        ava[0] = 0

    try:
        ava[1] = grid[y + 1][x]
    except IndexError:
        ava[1] = 0

    try:
        if x - 1 >= 0:
            ava[2] = grid[y][x - 1]
    except IndexError:
        ava[2] = 0

    try:
        ava[3] = grid[y][x + 1]
    except IndexError:
        ava[3] = 0

    return ava


def heuristic(current, goal):

    distance = abs(current[0] - goal[0]) + abs(current[1] - goal[1])
    return distance


def find_path(grid, start, goal):
    i = 0

    came_from = {}
    cost_so_far = {}
    came_from: dict[int, int] = dict()
    cost_so_far: dict[int, float] = dict()
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        priority, current = frontier.get()
        if current == goal:
            break

        neighbors = get_neighbors(grid, current)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for i in range(4):
            weight = neighbors[i]
            if weight == 0:
                continue
            next = (current[0] + directions[i][0],
                    current[1] + directions[i][1])
            new_cost = cost_so_far[current] + weight
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put((priority, next))
                came_from[next] = current

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    p = [[], []]
    for i in range(len(path)):
        p[0].append(path[i][0])
        p[1].append(path[i][1])

    return p

if __name__=="__main__":
    print(find_path([
        [1, 1, 2, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 2, 1, 1, 1]
    ], (0, 0), (4, 4)))
