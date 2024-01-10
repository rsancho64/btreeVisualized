#! /usr/bin/env python3

import graphviz

# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None

# def insert(root, key):
#     if root is None:
#         return TreeNode(key)
#     else:
#         if key < root.key:
#             root.left = insert(root.left, key)
#         else:
#             root.right = insert(root.right, key)
#     return root

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


# def visualize_binary_tree(root, counter):
#     dot = graphviz.Digraph()
#     dot.node(str(root.key))

#     def add_nodes_edges(node):
#         if node.left:
#             dot.node(str(node.left.key))
#             dot.edge(str(node.key), str(node.left.key))
#             add_nodes_edges(node.left)
#         if node.right:
#             dot.node(str(node.right.key))
#             dot.edge(str(node.key), str(node.right.key))
#             add_nodes_edges(node.right)

#     add_nodes_edges(root)
#     # dot.render('bt_'+str(counter), view=True, format='png')
#     dot.render('bt_'+str(counter), view=False, format='png')

# ----------------------
# POO:

class Bt:
    """binary tree"""

    def __init__(self, key=None):
        self.key = key
        self.left = self.right = None

    def __str__(self):
        # return f"[{self.key},{self.left},{self.right}]"
        keyOut = self.key
        if not keyOut:
            keyOut = "·"
        leftOut = self.left
        if not self.left:
            leftOut = "-"
        rightOut = self.right
        if not self.right:
            rightOut = "-"
        return f"[{leftOut},{keyOut},{rightOut}]"

    # LEGACY
    # def insert(root, key):
    #     if root is None:
    #         return TreeNode(key)
    #     else:
    #         if key < root.key:
    #             root.left = insert(root.left, key)
    #         else:
    #             root.right = insert(root.right, key)
    #     return root

    def insert(self, key):

        if not self.key: # is None:
            self.key = key
            return

        if key < self.key:
            if not self.left: # == None
                self.left = Bt(key)
                return
            if isinstance(self.left, Bt):
                self.left.insert(key)
                return

        if self.key < key:
            if not self.right: # == None
                self.right = Bt(key)
                return
            if isinstance(self.right, Bt):
                self.right.insert(key)
                return

    # LEGACY
    # def visualize_binary_tree(root, counter):
    #     dot = graphviz.Digraph()
    #     dot.node(str(root.key))

    #     def add_nodes_edges(node):
    #         if node.left:
    #             dot.node(str(node.left.key))
    #             dot.edge(str(node.key), str(node.left.key))
    #             add_nodes_edges(node.left)
    #         if node.right:
    #             dot.node(str(node.right.key))
    #             dot.edge(str(node.key), str(node.right.key))
    #             add_nodes_edges(node.right)

    #     add_nodes_edges(root)
    #     # dot.render('bt_'+str(counter), view=True, format='png')
    #     dot.render('bt_'+str(counter), view=False, format='png')

    def visu(self):

        # - [??] TODO introspeccion del nombre
        # https://stackoverflow.com/questions/1690400/getting-an-instance-name-inside-class-init
        # selfName = self.retrieveName() ...
        selfName = "aName"

        dot = graphviz.Digraph()
        dot.node(str(self.key))

        def add_nodes_edges(aBt):
            if aBt.left:
                dot.node(str(aBt.left.key))
                dot.edge(str(aBt.key), str(aBt.left.key))
                add_nodes_edges(aBt.left)
            if aBt.right:
                dot.node(str(aBt.right.key))
                dot.edge(str(aBt.key), str(aBt.right.key))
                add_nodes_edges(aBt.right)

        add_nodes_edges(self)
        # dot.render('bt_' + str(counter), view=True, format='png')
        dot.render('bt_' + selfName, view=False, format='png')


if __name__ == "__main__":

    bt = Bt()
    print(bt)
    # bt.visu()

    bt.insert(22)
    print(bt)
    # bt.visu()

    bt.insert(11)
    print(bt)
    bt.visu()

    bt.insert(33)  
    print(bt)
    bt.visu()

    bt.insert(23)  
    print(bt)
    bt.visu()

    bt.insert(44)  
    print(bt)
    bt.visu()
