## The Path to the Solution: A "Multi-Source" Mindset

When looking at this problem, the first instinct might be to start at an empty room and look for the nearest guard. However, that leads to redundant work. If you have 100 empty rooms, you’d perform 100 separate searches.

By reversing the logic and starting from the **guards**, we use a **Multi-Source Breadth-First Search (BFS)**.

* **Why BFS?** In an unweighted grid (where every step is exactly 1 unit), BFS is mathematically guaranteed to find the shortest path. Unlike Depth-First Search (DFS), which dives deep and might find a very long path before finding the short one, BFS expands in "layers"—exploring all rooms 1 step away, then all rooms 2 steps away, and so on.
* **Why Multi-Source?** By putting all guards into the queue at the very beginning, we treat them as a single collective starting point. The "ripples" of distance expand from every guard simultaneously. The first time a "ripple" hits an empty room, we know it came from the closest possible guard.

---

## Complexity Analysis

### Time Complexity: O(M*N)

* **Initialization:** We iterate through the  grid once to find guards and initialize the distance matrix.
* **The Search:** Each room (cell) is added to the queue at most once. When a cell is processed, we check its 4 neighbors.
* **Total:** Since each cell is visited a constant number of times, the time scales linearly with the number of rooms.

### Space Complexity: O(M*N)

* **Distance Matrix:** We need an  matrix to store the results.
* **The Queue:** In the worst-case scenario (like a "snake" pattern or a grid full of guards), the queue might hold a significant portion of the total cells (up to O(M*N)).
