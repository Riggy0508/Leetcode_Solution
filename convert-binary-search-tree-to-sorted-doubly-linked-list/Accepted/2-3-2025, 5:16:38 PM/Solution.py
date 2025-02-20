// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        def inorder(node):
            nonlocal first,last
            if node:
                inorder(node.left)

                if last:
                    last.right=node
                    node.left=last
                else:
                    first=node
                last=node
                inorder(node.right)

        first,last=None,None
        inorder(root)

        first.left=last
        last.right=first

        return first