#! /usr/bin/python
# -*- coding:UTF-8 -*-


class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self):
        self.root = None
        self.nodes = []
        self.queue = []
        self.stack = []

    def add_node(self, value):
        n = Node(value)
        self.nodes.append(n)
        if self.root is None:
            self.root = n
            return
        for i in self.nodes:
            if i.left is None:
                i.left = n
                return
            if i.right is None:
                i.right = n
                return

    def first_priority_visit(self, n):
        if n is None: return
        print n.value
        self.first_priority_visit(n.left)
        self.first_priority_visit(n.right)

if __name__ == "__main__":
    bt = BTree()
    bt.add_node(1)
    bt.add_node(2)
    bt.add_node(3)
    bt.add_node(4)
    bt.add_node(5)
    bt.add_node(6)
    # print bt.root.right.left.value
    bt.first_priority_visit(bt.root)

