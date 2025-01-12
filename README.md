# A* TSP Solver

This repository contains a self-contained Python script that demonstrates using the **A\*** search algorithm from the [simpleai](https://pypi.org/project/simpleai/) library to solve a Traveling Salesman Problem (TSP). The code and instructions below should help you run, understand, and potentially modify the solution.

---

## Overview

**A\* (A-star) Search**  
A* is a best-first search algorithm that is often used in pathfinding and graph traversal. It uses the formula \( f(n) = g(n) + h(n) \), combining:
- \( g(n) \): The actual cost from the start node to the current node \( n \).  
- \( h(n) \): A heuristic function that estimates the cost from \( n \) to the goal.

While A* can produce an optimal solution if the heuristic is _admissible_, be aware that a **simple** heuristic may lead to a valid but not necessarily minimal-cost route. For more rigorous solutions, consider using a zero heuristic (Dijkstra-like approach) or a more advanced admissible heuristic tailored to TSP.

---

## Features

- **Simple TSP Representation**: Cities are stored in a list, and distances between cities are represented by a dictionary of dictionaries.
- **Hashable States**: The search states are tuples, allowing `simpleai` to keep track of visited states without error.
- **Search Algorithm**: A* is used to navigate between states, guided by a heuristic function.
- **Heuristic**: By default, it estimates the cost to the closest unvisited city or, if all cities are visited, the cost to return to the initial city.  

> **Note**: This default heuristic does not guarantee the global optimum route (least total distance).

---

## Prerequisites

- Python 3.7 or higher
- [simpleai](https://pypi.org/project/simpleai/)

Install **simpleai** by running:

```bash
pip install simpleai
