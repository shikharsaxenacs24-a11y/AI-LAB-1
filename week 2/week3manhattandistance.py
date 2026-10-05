import heapq

def manhattan_distance(state, goal):
    distance = 0

    for tile in range(1, 9):
        current_pos = state.index(tile)
        goal_pos = goal.index(tile)

        current_row, current_col = divmod(current_pos, 3)
        goal_row, goal_col = divmod(goal_pos, 3)

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = list(state)
            new_zero = nr * 3 + nc

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def print_path(parent, state):
    path = []

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    for i, s in enumerate(path):
        print("Step", i)
        for j in range(0, 9, 3):
            print(s[j:j+3])
        print()


def astar(initial, goal):
    pq = []

    # f(n), g(n), state
    h = manhattan_distance(initial, goal)
    heapq.heappush(pq, (h, 0, initial))

    parent = {initial: None}
    g_cost = {initial: 0}
    visited = set()

    while pq:
        f, g, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            print("Solution found!")
            print_path(parent, current)
            return

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g

                # Manhattan Distance
                h = manhattan_distance(neighbor, goal)

                # A* evaluation function
                f = new_g + h

                parent[neighbor] = current

                heapq.heappush(
                    pq,
                    (f, new_g, neighbor)
                )

    print("No solution found.")


# 0 represents blank
initial = (
    2, 8, 3,
    1, 6, 4,
    7, 5, 0
)

goal = (
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
)

astar(initial, goal)
print("1BF24CS280 , SHIKHAR SAXENA")
