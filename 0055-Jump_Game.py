'''
Difficulty: Medium

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
from typing import List



# Below is too slow, looked on Stack Overflow, this makes more sense...

class Solution:
    def canJump(self, nums):
        maximum_reachable_index = 0

        for index, max_jump in enumerate(nums):
            #print(f"{index}", end=' ')
            if index > maximum_reachable_index:
                #print(f"> {maximum_reachable_index} and is unreachable.")
                return False

            #print(f"+ {max_jump} => {index + max_jump} : {maximum_reachable_index} ")
            maximum_reachable_index = max(index + max_jump, maximum_reachable_index)

        return True



class Solution:
    checked = []
    numsLen = 0

    def jumpcheck(self, nums, currindex):
        print(currindex, Solution.numsLen, Solution.checked)
        if currindex == Solution.numsLen:
            return True
        else:
            if currindex > Solution.numsLen or Solution.checked[currindex] == 1:
                return False
            elif nums[currindex] == 0:
                Solution.checked[currindex] = 1
                return False
            else:
                for i in range(nums[currindex], 0, -1):
                    returnval = Solution.jumpcheck("", nums, min(currindex + i, Solution.numsLen))
                    if not returnval:
                        Solution.checked[currindex] = 1
                    else:
                        return True
        return False

    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        Solution.numsLen = len(nums) - 1
        Solution.checked = [0] * Solution.numsLen
        if Solution.numsLen == 0:
            return True

        for i in range(nums[0], 0, -1):
            if Solution.jumpcheck("", nums, i):
                return True
        return False



print(Solution.canJump("", [2,0]))

'''print(Solution.canJump("", [0]))
print(Solution.canJump("", [2, 3, 1, 1, 4]))
print(Solution.canJump("", [2, 3, 1, 1, 4]))
print(Solution.canJump("", [4, 3, 1, 1, 4]))
print(Solution.canJump("", [2, 0, 2, 0, 4, 0, 0, 2, 0, 1]))
print(Solution.canJump("", [1, 3, 0, 0, 4, 0, 0, 2, 0, 1]))
print(Solution.canJump("", [3, 2, 1, 0, 4]))
print(Solution.canJump("", [0, 2, 1, 0, 4]))'''
