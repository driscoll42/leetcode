'''
Difficulty: Easy

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diamFunc(self, root: TreeNode):
        leftlen, rightlen = 0, 0
        leftmax, rightmax = 0, 0

        if root.left is not None:
            leftdiam = Solution.diamFunc(self, root.left)
            leftmax, leftlen = leftdiam[0], leftdiam[1] + 1
        if root.right is not None:
            rightdiam = Solution.diamFunc(self, root.right)
            rightmax, rightlen = rightdiam[0], rightdiam[1] + 1
        # print(root.val, leftlen, rightlen)

        maxLen = max(leftlen, rightlen)
        return [max(leftlen + rightlen, leftmax, rightmax), maxLen]

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return Solution.diamFunc(self, root)[0]
