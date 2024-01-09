import graphviz


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = get_min_value(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


def get_min_value(root):
    while root.left is not None:
        root = root.left
    return root


def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.key, end=' ')
        in_order_traversal(root.right)


def pre_order_traversal(root):
    if root is not None:
        print(root.key, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def post_order_traversal(root):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.key, end=' ')


def visualize_binary_tree(root, counter):
    dot = graphviz.Digraph()
    dot.node(str(root.key))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(node.left.key))
            dot.edge(str(node.key), str(node.left.key))
            add_nodes_edges(node.left)
        if node.right:
            dot.node(str(node.right.key))
            dot.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    #dot.render('bt_'+str(counter), view=True, format='png')
    dot.render('bt_'+str(counter), view=False, format='png')    


if __name__ == "__main__":

    keys = [
        [None],
        # [5],
        # [5, 3],
        # [5, 3, 7],
        # [5, 3, 7, 9],
        [5, 3, 7, 9, 8],        
        [5, 3, 7, 8, 9],
        # [5, 3, 7, 2, 4, 6],
        # [5, 3, 7, 2, 4, 6, 8]
    ]

    figcounter = 0
    for k in keys:
        root = None
        for it in k:        
            root = insert(root, it)
        visualize_binary_tree(root, figcounter)
        figcounter += 1        
