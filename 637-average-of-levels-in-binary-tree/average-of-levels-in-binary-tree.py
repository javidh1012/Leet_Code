# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []

        while q:
            q_size = len(q)
            sum_level = 0
            for i in range(q_size):
                node = q.popleft()
                sum_level+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(sum_level/q_size)

        return res





        