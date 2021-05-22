from typing import List

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return f'{self.data}'


def insert_node(node: Node, data: int) -> Node:
    if not node:
        node = Node(data)
    elif data < node.data:
        node.left = insert_node(node.left, data)
    else:
        node.right = insert_node(node.right, data)
    return node


def dfs_print_tree(node):
    print(node.data, end='')
    if node.left:
        dfs_print_tree(node.left)
    if node.right:
        dfs_print_tree(node.right)


# Sort of
def bfs_print_tree(node):
    print(node.data, end='')
    if node.left:
        print(node.left.data, end='')
    if node.right:
        print(node.right.data, end='')
    if node.left:
        dfs_print_tree(node.left)
    if node.right:
        dfs_print_tree(node.right)


#          6
#         /  \
#        4    8
#       / \   / \
#      3   5 7   9 
#     / \         \
#    1   2         10   
if __name__ == '__main__':
    values : List[int] = [4, 5, 8, 7, 3, 2, 1, 9, 10]
    root = None
    root = insert_node(root, 6)
    for i in values:
        insert_node(root, i)

    print('DFS tree print:')
    dfs_print_tree(root)
    print('\n')
    print('BFS tree print:')
    bfs_print_tree(root)
    print('\n')