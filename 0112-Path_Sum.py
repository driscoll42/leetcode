'''
Difficulty: Easy

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # print(sum, root.val)
        if not root:
            return False

        if root.val == sum and not root.left and not root.right:
            return True

        sum -= root.val

        return Solution.hasPathSum(self, root.left, sum) or Solution.hasPathSum(self, root.right, sum)


'''        if not root:
            return False
        returnval = False
        if root.left:
            returnval = returnval or Solution.hasPathSum(self, root.left, sum - root.val)
        if returnval:
            return True
        if root.right:
            returnval = returnval or Solution.hasPathSum(self, root.right, sum - root.val)
        if root.val == sum and not root.left and not root.right:
            return True
        else:
            return returnval'''
