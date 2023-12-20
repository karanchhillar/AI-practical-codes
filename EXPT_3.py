from collections import deque

class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target_capacity):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target_capacity = target_capacity
        self.visited_states = set()

    def is_valid_state(self, jug1, jug2):
        return 0 <= jug1 <= self.jug1_capacity and 0 <= jug2 <= self.jug2_capacity

    def solve(self):
        initial_state = (0, 0)  
        queue = deque([(initial_state, 0)])  
        self.visited_states.add(initial_state)

        while queue:
            current_state, steps = queue.popleft()
            jug1, jug2 = current_state

            if jug1 == self.target_capacity or jug2 == self.target_capacity:
                return steps

            actions = [
                (self.jug1_capacity, jug2),
                (jug1, self.jug2_capacity),
                (0, jug2),
                (jug1, 0),
                (jug1 - min(jug1, self.jug2_capacity - jug2), jug2 + min(jug1, self.jug2_capacity - jug2)),
                (jug1 + min(self.jug1_capacity - jug1, jug2), jug2 - min(self.jug1_capacity - jug1, jug2)),
            ]

            for action in actions:
                if self.is_valid_state(*action) and action not in self.visited_states:
                    queue.append((action, steps + 1))
                    self.visited_states.add(action)

        return -1 
    
# usage:
jug_problem = WaterJugProblem(4 , 3 , 2)  # Jug capacities and target amount
steps_required = jug_problem.solve()

if steps_required != -1:
    print(f"Minimum steps required: {steps_required}")
else:
    print("No solution found.")
