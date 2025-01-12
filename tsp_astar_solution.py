"""
File name: tsp_astar_solution.py

To run:
  1) Install simpleai if not installed:
     pip install simpleai

  2) Execute this file from the command line:
     python tsp_astar_solution.py

Description:
  This script defines and solves a TSP variant using the A* search algorithm
  from the simpleai library. The solution:
   - Demonstrates a TSPProblem class with states as tuples for hashability.
   - Computes a (possibly suboptimal) route visiting all cities once.
   - Illustrates how to check the path, the visited order, and the total cost.

Note:
  - By default, the heuristic is simple and may not yield an optimal TSP route.
    For true optimal solutions, consider using a zero heuristic or an
    admissible TSP-specific heuristic (e.g., MST-based).
"""

from simpleai.search import SearchProblem, astar

class TSPProblem(SearchProblem):
    def __init__(self, cities, distances):
        """
        :param cities: List of city names, e.g. ['A', 'B', 'C', 'D']
        :param distances: Dict of dict, distances[a][b] = cost from city a to b
        """
        self.cities = cities
        self.distances = distances
        # Use a tuple for initial state to ensure it's hashable
        self.initial_state = (cities[0],)

    def is_goal(self, state):
        """
        Returns True if all cities are visited.
        """
        return len(state) == len(self.cities)

    def actions(self, state):
        """
        Returns the list of unvisited cities.
        """
        return [city for city in self.cities if city not in state]

    def result(self, state, action):
        """
        Appends 'action' city to the current visited list (tuple).
        """
        return state + (action,)

    def cost(self, state, action, next_state):
        """
        Distance from the last visited city in 'state' to the new city 'action'.
        """
        last_city = state[-1]
        return self.distances[last_city][action]

    def heuristic(self, state):
        """
        Simple heuristic:
          - If goal, estimate cost to return to the initial city
          - Otherwise, estimate cost to the nearest unvisited city
        This may not always guide us to the optimal TSP route.
        """
        if self.is_goal(state):
            # Estimate cost to return to the start (making it a round trip)
            return self.distances[state[-1]][state[0]]
        else:
            current_city = state[-1]
            unvisited = [city for city in self.cities if city not in state]
            if not unvisited:
                # If nothing unvisited, cost is just returning to start
                return self.distances[current_city][state[0]]
            # Otherwise, pick minimum distance to an unvisited city
            return min(self.distances[current_city][city] for city in unvisited)

def main():
    # Example cities and distance matrix
    cities = ['A', 'B', 'C', 'D']
    distances = {
        'A': {'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'C': 5,  'D': 12},
        'C': {'A': 15, 'B': 5,  'D': 8},
        'D': {'A': 20, 'B': 12, 'C': 8}
    }

    # Create and solve the TSP problem using A*
    problem = TSPProblem(cities, distances)
    result = astar(problem)

    # Show the results
    print("Visited cities in order:", result.state)
    print("Total cost:", result.cost)
    print("Full path:", result.path())  # (action, resulting_state) pairs

if __name__ == "__main__":
    main()
