graph_view = """
     1
   /   \\
  2     3
 / \   / \\
 4  6-5   7   
  \\
   9
"""
# This graph is directional so consider these nodes and arcs
g = {
    '1': ['2', '3'],
    '2': ['4', '6'],
    '3': ['5', '7'],
    '4': ['8'],
    '5': [],
    '6': ['5'],
    '7': [],
    '8': []
}

v = []
q = []

# Visit each level fully before nesting deeper into a graph.
def bfs(v, g, n):
    v.append(n)
    q.append(n)
    print(f'Executing a breadth first search on {g}')

    while q:
        m = q.pop(0)
        print(m, end=' ')

        for adjacent in g[m]:
            if adjacent not in v:
                v.append(adjacent)
                q.append(adjacent)

# Navigate down each node as we find it, getting deeply nested as a priority.
dfs_v = set()
def dfs(v, g, n):
    if n not in v:
        print(n, end = ' ')
        v.add(n)
        for adjacent in g[n]:
            dfs(v, g, adjacent)

print(f'Graph:\n {graph_view}')
bfs(v, g, '1')
print('\n')
print(f'Executing a Depth first search on {g}')
dfs(dfs_v, g, '1')
print('\n')