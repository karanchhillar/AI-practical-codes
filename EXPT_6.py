import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0, f=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start to this node
        self.h = h  # Heuristic estimate to the goal
        self.f = f  # f = g + h

    def __lt__(self, other):
        return self.f < other.f

def aostar(graph, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    start_node.g = 0
    start_node.h = heuristic_cost(start, goal)
    start_node.f = start_node.g + start_node.h

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal:
            return reconstruct_path(current_node)

        closed_set.add(current_node.state)

        for neighbor, cost in graph[current_node.state]:
            if neighbor in closed_set:
                continue

            tentative_g = current_node.g + cost
            neighbor_node = Node(neighbor)

            if neighbor_node not in open_list or tentative_g < neighbor_node.g:
                neighbor_node.parent = current_node
                neighbor_node.g = tentative_g
                neighbor_node.h = heuristic_cost(neighbor, goal)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if neighbor_node not in open_list:
                    heapq.heappush(open_list, neighbor_node)

    return None  # No path found

def heuristic_cost(node, goal):
    # Example heuristic: Manhattan distance
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent
    return path

# Example usage:
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((0, 2), 1), ((1, 1), 1)],
    (0, 2): [((0, 1), 1), ((1, 2), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((1, 0), 1), ((0, 1), 1), ((1, 2), 1), ((2, 1), 1)],
    (1, 2): [((0, 2), 1), ((1, 1), 1)],
    (2, 0): [((2, 1), 1)],
    (2, 1): [((2, 0), 1), ((1, 1), 1), ((2, 2), 1)],
    (2, 2): [((2, 1), 1)]
}


start = (0, 0)
goal = (2, 2)

path = aostar(graph, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")
