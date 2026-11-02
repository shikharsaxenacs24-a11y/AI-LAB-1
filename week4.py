
# USN_Week4_HillClimbing_N_Queens.py
# Implement Hill Climbing Algorithm for 4-Queens Problem

import random

N = 4

# Function to calculate the cost (number of attacking queen pairs)
def calculate_cost(state):
    cost = 0

    for i in range(N):
        for j in range(i + 1, N):
            # Check whether queens are in the same row
            if state[i] == state[j]:
                cost += 1

            # Check whether queens are on the same diagonal
            elif abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


# Function to display the chessboard
def display_board(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()
    print()


# Generate all neighboring states
def generate_neighbors(state):
    neighbors = []

    for col in range(N):
        for row in range(N):
            if state[col] != row:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)

    return neighbors


# Hill Climbing Algorithm
def hill_climbing():
    # Initial configuration
    current_state = [random.randint(0, N - 1) for _ in range(N)]

    step = 1

    print("Initial State:")
    display_board(current_state)

    while True:
        current_cost = calculate_cost(current_state)

        print("Step:", step)
        print("Current State:", current_state)
        print("Current Cost:", current_cost)

        # Check goal state
        if current_cost == 0:
            print("\nGoal State Reached!")
            display_board(current_state)
            print("Final Configuration:", current_state)
            return

        neighbors = generate_neighbors(current_state)

        # Find the best neighboring state
        best_neighbor = None
        best_cost = current_cost

        for neighbor in neighbors:
            cost = calculate_cost(neighbor)

            print("Neighbor:", neighbor, "Cost:", cost)

            if cost < best_cost:
                best_cost = cost
                best_neighbor = neighbor

        # Stop if no better neighbor exists
        if best_neighbor is None:
            print("\nLocal Minimum Reached!")
            print("No better neighboring state found.")
            print("Restarting with a new initial state...\n")

            current_state = [
                random.randint(0, N - 1) for _ in range(N)
            ]
            continue

        # Move to the best neighbor
        current_state = best_neighbor

        print("Selected Neighbor:", current_state)
        print("New Cost:", best_cost)
        display_board(current_state)

        step += 1


# Main program
if __name__ == "__main__":
    hill_climbing()
