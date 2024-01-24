import heapq

class Node:

    def __init__(self, state, parent=None, cost=0):

        self.state = state
        self.parent = parent
        self.cost = cost # The cost to reach this node from the starting node

    def __lt__(self, other):
        return self.cost < other.cost
    

def greedy_best_first_search(start, goal, state_graph, heuristic):
    frontier = []
    heapq.heappush(frontier, (0, start)) # Priority queue
    explored = set()

    while frontier:
        _, current_node = heapq.heappop(frontier)

        if current_node.state == goal:
            return reconstruct_path(current_node)
        
        explored.add(current_node.state)

        for child_state, cost in state_graph[current_node.state].items():
            child_node = Node(child_state, current_node, cost)
            if child_state not in explored and child_node not in frontier:
                heapq.heappush(frontier, (heuristic[child_state], child_node))

    return None # No path found


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1] # Return reversed path


# Example usage
if __name__ == "__main__":

    # Define your graph here. For example, a dictionary of dictionaries with structure: graph[state] = {neighbor1: cost1, neighbor2: cost2, ...}

    graph = {
        'A': {'B': 1, 'C': 3, 'D': 7},
        'B': {'D': 5},
        'C': {'D': 12},
        'D': {}
    }

    # Define your heuristic here. For example, a dictionary with estimated costs to reach the goal from each node

    heuristic = {

        'A': 7,
        'B': 5,
        'C': 12,
        'D': 0 # Assuming 'D' is the goal
    }

    start_node = Node('A')
    goal = 'D'
    path = greedy_best_first_search(start_node, goal, graph, heuristic)

    if path:
        print(f"Path found: {' -> '.join(path)}")

    else:
        print("No path found")