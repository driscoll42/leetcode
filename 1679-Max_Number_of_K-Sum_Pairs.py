'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.



Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
'''

# Initial O(n log n + n) solution
class Solution(object):
    def maxOperations(self, nums, k):
        if len(nums) <= 1:
            return 0
        nums.sort()
        i = 0
        j = len(nums) - 1
        tot = 0
        while i != j:
            if i == j or i > j or j < i:
                break
            elif nums[i] + nums[j] == k:
                tot += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            elif nums[i] + nums[j] > k:
                j -= 1
        return tot

# After being suggested to use Hash Maps
from collections import defaultdict


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def def_value():
            return 0

        num_dict = defaultdict(def_value)
        tot = 0

        for n in nums:
            complement = k - n
            if num_dict[complement] > 0:
                num_dict[complement] -= 1
                tot += 1
            else:
                num_dict[n] += 1
        return tot

# Trying with Counter
from collections import Counter


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        c = Counter(nums)
        tot = 0

        for i in c:
            comp = k - i
            ci = c[i]
            if c[comp]:
                if comp == i:
                    tot += ci // 2
                else:
                    c_comp = c[comp]
                    tot += min(ci, c_comp)
                    c[comp] = 0

        return tot