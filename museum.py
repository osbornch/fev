from collections import deque

from collections import deque

def find_distance_to_guards(grid):
    if not grid: return []
    
    M, N = len(grid), len(grid[0])
    # Use -1 as the default for everything (Walls and Unreachable)
    # We'll use a separate 'visited' logic or a specific placeholder for 'Open'
    res = [[-1 for _ in range(N)] for _ in range(M)]
    queue = deque()

    for r in range(M):
        for c in range(N):
            if grid[r][c] == 'G':
                res[r][c] = 0
                queue.append((r, c))
            elif grid[r][c] == 'O':
                # Mark open rooms with a special value to denote "needs visiting"
                res[r][c] = float('inf')

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Only step into rooms marked as 'Open' (inf)
            if 0 <= nr < M and 0 <= nc < N and res[nr][nc] == float('inf'):
                res[nr][nc] = res[r][c] + 1
                queue.append((nr, nc))
    
    # Final pass: Convert any remaining 'inf' (unreachable) to -1
    for r in range(M):
        for c in range(N):
            if res[r][c] == float('inf'):
                res[r][c] = -1
                
    return res
test_cases = [
    {
        "name": "Standard Mix",
        "input": [['G', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'G']],
        "desc": "Multiple guards at opposite ends."
    },
    {
        "name": "Walls and Unreachable",
        "input": [['G', 'W', 'O'], ['W', 'W', 'O'], ['O', 'O', 'O']],
        "desc": "Rooms behind walls that cannot be reached."
    },
    {
        "name": "The Snake (Winding Path)",
        "input": [
            ['G', 'O', 'O'],
            ['W', 'W', 'O'],
            ['O', 'O', 'O'],
            ['O', 'W', 'W'],
            ['O', 'O', 'O']
        ],
        "desc": "Long path where physical proximity != shortest path."
    },
    {
        "name": "The Island (Isolated Room)",
        "input": [
            ['G', 'O', 'W'],
            ['W', 'W', 'O'],  # This 'O' is trapped by walls
            ['W', 'W', 'W']
        ],
        "desc": "A single room completely boxed in."
    },
    {
        "name": "No Guards",
        "input": [['O', 'O'], ['O', 'W']],
        "desc": "Valid museum but zero guards present."
    },
    {
        "name": "No Rooms (All Walls)",
        "input": [['W', 'W'], ['W', 'W']],
        "desc": "No traversable space."
    },
    {
        "name": "Corner Guard",
        "input": [['G', 'O'], ['O', 'O']],
        "desc": "Guard in a corner room."
    }
]

def run_suite():
    for case in test_cases:
        print(f"TEST: {case['name']} - ({case['desc']})")
        result = find_distance_to_guards(case['input'])
        for row in result:
            # Format: U for unreachable (inf), W for wall (-1)
            formatted = [str(v) if v != float('inf') else "U" for v in row]
            print("  " + "  ".join(f"{x:>2}" for x in formatted))
        print("-" * 30)

run_suite()