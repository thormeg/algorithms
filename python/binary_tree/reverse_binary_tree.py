graph_view = """
     1
   /   \\
  2     3
 / \   / \\
 4  6 5   7   
  \\
   8
"""
# This graph is directional so consider these nodes and arcs
g = {
    '1': ['2', '3'],
    '2': ['4', '6'],
    '3': ['5', '7'],
    '4': ['8'],
    '5': [],
    '6': [],
    '7': [],
    '8': []
}

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def reverse_tree(node):
    if not node:
        return None
    
    node.left, node.right = node.right, node.left
    reverse_tree(node.left)
    reverse_tree(node.right)
    return node


def dfs_print_tree(node):
    print(node.data, end='')
    if node.left:
        dfs_print_tree(node.left)
    if node.right:
        dfs_print_tree(node.right)


print(f'Reversing graph:\n {graph_view}\n'
    f'Graph: {g}')
tree = Node('1')
tree.left = Node('2')
tree.right = Node('3')
tree.left.left = Node('4')
tree.left.left.right = Node('8')
tree.left.right = Node('6')
tree.right.left = Node('5')
tree.right.right = Node('7')
dfs_print_tree(tree)
print('\n')
reversed = reverse_tree(tree)
dfs_print_tree(reversed)
print('\n')
