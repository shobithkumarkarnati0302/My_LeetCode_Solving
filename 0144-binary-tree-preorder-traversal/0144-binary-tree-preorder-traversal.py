# Definition for a binary tree root.
# class Treeroot(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        result = []

        def dfs(node):
            if node:
                result.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return result