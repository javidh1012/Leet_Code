# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node,curval):
            if not node:
                return 0
            curval = curval*10+node.val
            if not node.left and not node.right:
                return curval

            return dfs(node.left,curval) + dfs(node.right,curval)
        return dfs(root, 0)
        